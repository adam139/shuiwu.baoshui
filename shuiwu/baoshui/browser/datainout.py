#-*- coding: UTF-8 -*-
import csv
from StringIO import StringIO
from zope import event
from zope.interface import implements

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
# from plone.i18n.normalizer.interfaces import IUserPreferredFileNameNormalizer

from shuiwu.baoshui.content.nashuiren import Inashuiren
from shuiwu.baoshui.events import CreateNashuirenEvent,UpdateNashuirenEvent

from shuiwu.baoshui import _

# field names will be imported
data_PROPERTIES = [
    'title',
    'guanlidaima',
    'regtype',
    'status',
    'dengjiriqi',
    'description',
    'shuiguanyuan',        
    'danganbianhao',
    'caiwufuzeren',
    'caiwufuzerendianhua',
    'banshuiren',
    'banshuirendianhua'
    ] 
# need byte string
data_VALUES = [
               u"纳税人名称".encode('utf-8'),
               u"社会信用代码".encode('utf-8'),
               u"登记注册类型".encode('utf-8'),
               u"纳税人状态".encode('utf-8'),
               u"登记日期".encode('utf-8'),
#                u"主管税务机关".encode('utf-8'),
               u"主管税务所（科、分局）".encode('utf-8'),
               u"税收管理员".encode('utf-8'),               
               u"税收档案编号".encode('utf-8'),
               u"财务负责人".encode('utf-8'),
               u"财务负责人电话".encode('utf-8'),
               u"办税人".encode('utf-8'),
               u"办税人电话".encode('utf-8')
               ]

model = u'湖南省湘潭高新技术产业开发区地方税务局'.encode('utf-8')
class DataInOut (BrowserView):
    """Data import and export as CSV files.
    """

    def __call__(self):
        method = self.request.get('REQUEST_METHOD', 'GET')
        if (method != 'POST') or not int(self.request.form.get('form.submitted', 0)):
            return self.index()

        if self.request.form.get('form.button.Cancel'):
            return self.request.response.redirect('%s/plone_control_panel' \
                                                  % self.context.absolute_url())

        if self.request.form.get('form.button.Import'):
            return self.importData()

        if self.request.form.get('form.button.CSVErrors'):
            return self.getCSVWithErrors()

        if self.request.form.get('form.button.Export'):
            return self.exportData()
        

    def getCSVTemplate(self):
        """Return a CSV template to use when importing members."""
        datafile = self._createCSV([])
        return self._createRequest(datafile.getvalue(), "nashuiren_sheet_template.csv")     

    def IdIsExist(self,Id):
        catalog = getToolByName(self.context, "portal_catalog")
        brains = catalog(object_provides=Inashuiren.__identifier__,id=Id)
        guanlidaima_brains =  catalog(object_provides=Inashuiren.__identifier__,guanlidaima=Id)
        return bool(brains) or bool(guanlidaima_brains)
            
    def importData(self):
        """Import Data from CSV file.

        In case of error, return a CSV file filled with the lines where
        errors occured.
        """

        file_upload = self.request.form.get('csv_upload', None)
        if file_upload is None or not file_upload.filename:
            return
        reader = csv.reader(file_upload)

        header = reader.next()
        if header != data_VALUES:
            msg = _('Wrong specification of the CSV file. Please correct it and retry.')
            type = 'error'
            IStatusMessage(self.request).addStatusMessage(msg, type=type)
            return

        validLines = []
        invalidLines = []
        for line in reader:
#            datas = dict(zip(header, line))
            validLines.append(line)
        usersNumber = 0
        
        for line in validLines:
            datas = dict(zip(data_PROPERTIES, line)) 
            try:
#                映射数据到纳税人字段
                title = datas['title']                
#                 if not isinstance(title, unicode):
#                     title = unicode(title, 'utf-8')
#                 id = IUserPreferredFileNameNormalizer(self.request).normalize(filename)
                id = datas['guanlidaima']
                id = self.float2str(id,"E+")
#                 title = name
                guanlidaima = id                
                dengjiriqi = datas.pop('dengjiriqi')
                if ' ' in dengjiriqi:
                    dengjiriqi = dengjiriqi.split(' ')[0]
                description = datas.pop('description')
                if isinstance(description, unicode):
                    description = description.encode('utf-8')
                if model in description:
                    description = description.replace(model,'')
                shuiguanyuan = datas['shuiguanyuan']
                danganbianhao = ""                
                status = datas.pop('status')
                regtype = datas.pop('regtype')
                caiwufuzeren = datas.pop('caiwufuzeren')
                caiwufuzerendianhua = datas.pop('caiwufuzerendianhua')
                banshuiren = datas.pop('banshuiren')
                banshuirendianhua = datas.pop('banshuirendianhua')
                if self.IdIsExist(id):
# send a update nashuiren event
                    try:
                        event.notify(UpdateNashuirenEvent(
                                                id,status,regtype,
                                                caiwufuzeren,caiwufuzerendianhua,banshuiren,
                                                banshuirendianhua))
#                         usersNumber += 1
                        continue
                    
                    except:
                        continue                                              
# send a add nashuiren event
                try:
                    event.notify(CreateNashuirenEvent(
                                                id,title,guanlidaima,dengjiriqi,description,
                                                shuiguanyuan,danganbianhao,status,regtype,
                                                caiwufuzeren,caiwufuzerendianhua,banshuiren,
                                                banshuirendianhua))
                except (AttributeError, ValueError), err:
                    logging.exception(err)
                    IStatusMessage(self.request).addStatusMessage(err, type="error")
                    return
                usersNumber += 1
            except:
                invalidLines.append(line)
                print "Invalid line: %s" % line
        if invalidLines:
            datafile = self._createCSV(invalidLines)
            self.request['csverrors'] = True
            self.request.form['nashuiren_sheet_errors'] = datafile.getvalue()
            msg = _('Some errors occured. Please check your CSV syntax and retry.')
            type = 'error'
        else:
            msg, type = _('Data successfully imported.'), 'info'

        IStatusMessage(self.request).addStatusMessage(msg, type=type)
        self.request['users_results'] = usersNumber
        return self.index()

    def getCSVWithErrors(self):
        """Return a CSV file that contains lines witch failed."""

        users_sheet_errors = self.request.form.get('nashuiren_sheet_errors', None)
        if users_sheet_errors is None:
            return # XXX
        return self._createRequest(users_sheet_errors, "nashuiren_sheet_errors.csv")

    def exportData(self,**kw):
        """Export Data within CSV file."""

        datafile = self._createCSV(self._getDataInfos(**kw))
        return self._createRequest(datafile.getvalue(), "sheet_export.csv")

    def tranVoc(self,value):
        """ translate vocabulary value to title"""
        translation_service = getToolByName(self.context,'translation_service')
        title = translation_service.translate(
                                                  value,
                                                  domain='shuiwu.baoshui',
                                                  mapping={},
                                                  target_language='zh_CN',
                                                  context=self.context,
                                                  default=u"未填写")
        return title 

    def float2str(self,input,patern):
        "float to string"
        
        if patern in input:
            output = str(int(float(input)))
            return output
        else:
            return input
        
    
    def _getDataInfos(self,**kw):
        """Generator filled with the orgs data."""

        catalog = getToolByName(self.context, "portal_catalog")
        query = kw
        query.update({"object_provides":Inashuiren.__identifier__})
        
        brains = catalog(query)
        
        for i in brains:
            dataobj = i.getObject()                                
            props = []
            if dataobj is not None:
                for p in data_PROPERTIES: # data properties 
#                    import pdb
#                    pdb.set_trace()                   
                    if p == "organization_type" or p == "announcement_type" or p == "belondto_area":
                        props.append(self.tranVoc(getattr(dataobj,p)))
                    else:
                        props.append(getattr(dataobj,p))                    
            yield props


    def _createCSV(self, lines):
        """Write header and lines within the CSV file."""
        datafile = StringIO()
        writor = csv.writer(datafile)
        writor.writerow(data_VALUES)
        map(writor.writerow, lines)
        return datafile

    def _createRequest(self, data, filename):
        """Create the request to be returned.

        Add the right header and the CSV file.
        """
        self.request.response.addHeader('Content-Disposition', "attachment; filename=%s" % filename)
        self.request.response.addHeader('Content-Type', "text/csv;charset=utf-8")
        self.request.response.addHeader("Content-Transfer-Encoding", "8bit")        
        self.request.response.addHeader('Content-Length', "%d" % len(data))
        self.request.response.addHeader('Pragma', "no-cache")
        self.request.response.addHeader('Cache-Control', "must-revalidate, post-check=0, pre-check=0, public")
        self.request.response.addHeader('Expires', "0")
        return data
