#-*- coding: UTF-8 -*-
from five import grok
import json
from z3c.form import field
from zope.interface import Interface
from Acquisition import aq_inner
from plone.directives import dexterity
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from plone.memoize import ram
from Products.Five.browser import BrowserView
from datetime import datetime

from shuiwu.baoshui.content.nashuiren import Inashuiren
from shuiwu.baoshui.content.niandu import Iniandu
from shuiwu.baoshui.subscriber import yuedu_subjects,jidu_subjects,ling_subjects
from shuiwu.baoshui.subscriber import subids,niandugouduiziduan
from shuiwu.baoshui.subscriber import tagroup
from shuiwu.baoshui import _

fmt = '%Y/%m/%d %H:%M:%S'

def _render_output_cachekey(method, self, obj,width):
    "generator cache key"
    mf = getattr(obj,"mflag",0)
#     import pdb
#     pdb.set_trace()
    return (obj.absolute_url(),mf)
    
class NashuirenView(BrowserView):
    "nashuiren  view"
    @memoize    
    def catalog(self):
        context = aq_inner(self.context)
        pc = getToolByName(context, "portal_catalog")
        return pc
    
    @memoize    
    def pm(self):
        context = aq_inner(self.context)
        pm = getToolByName(context, "portal_membership")
        return pm    
            
    @property
    def isEditable(self):
        return self.pm().checkPermission(permissions.ManagePortal,self.context)
    
    def getPathQuery(self,id): 
        "获取查询路径"
        query = {}
        path = "/".join(self.context.getPhysicalPath())
        query['path'] = "%s/%s" % (path,id)
        return query    
    
    def needInit(self,objid):
        query = self.getPathQuery(objid)
        query['object_provides'] = Iyuedujilu.__identifier__
        brains = self.catalog()(query)
        return not bool(brains)        
        
    def getChildrensByMonth(self,objid):
        "依据按月度申报的内容对象id，提取其每个月申报记录（是否已申报）"      

        obj = self.context[objid]              
        return self.outputcheckbox(obj,width=1)
    
    def getChildrensByQuarter(self,objid):
        "依据按季度申报的内容对象id，提取其每个季度申报记录"
        obj = self.context[objid]              
        return self.outputcheckbox(obj,width=3)
    
    def getChildrensByNumber(self,objid):
        "依据按次申报的内容对象id，提取其每月的申报次数"
        obj = self.context[objid]               
        return self.outputnumber(obj,width=1)               
    
    @ram.cache(_render_output_cachekey)
    def outputcheckbox(self,obj,width=1):
        "根据参数total,braindata,返回jason 输出"
        outhtml = """<table class="table table-condensed inner"><tr class="row">"""     
        nums = 12/width
        for i in range(nums):
            field = "shenbaofou%s" % str(i+1)
            if getattr(obj,field,False) == False:           
                out = """<td class="col-md-%(width)s checkbox">
                <input  type="checkbox" />
                <span class="switch-style off">&nbsp;</span></td>""" \
                % dict(width=width)
            else:
                out = """<td class="col-md-%(width)s checkbox">
                <input  type="checkbox" checked="checked" />
                <span class="switch-style on">&nbsp;</span></td>""" \
                % dict(width=width)                                  
            outhtml = "%s%s" %(outhtml ,out)           
        data = """%s</tr></table>"""  % outhtml
        return data
    
    @ram.cache(_render_output_cachekey)
    def outputnumber(self,obj,width=1):
        "根据参数输出html"
        outhtml = """<table class="table table-condensed inner"><tr class="row">"""     
        nums = 12/width
        for i in range(nums):
            field = "shenbaocishu%s" % str(i+1)
            num = getattr(obj,field,0)
            out = """<td class="col-md-%(width)s">%(num)s</td>""" \
                % dict(width=width,num=num)                                  
            outhtml = "%s%s" %(outhtml ,out)           
        data = """%s</tr></table>""" % outhtml
        return data
    
    def propertyChecked(self,property):
        "check narenren object,if the property is True"
        obj = self.context
        pro = getattr(obj,property)
        if pro:
            return True
        else:
            return False
        
    def parentobj_propertyChecked(self,property):
        "check niandu object,if the property is True,using for niandu"        
        obj = self.context.aq_parent
        pro = getattr(obj,property)
        if pro:
            return True
        else:
            return False        
        
    def getChildDesByName(self,child):
        "get child description by child's id"
        query = self.getPathQuery(child)
        brains = self.catalog()(query)
        des = brains[0].Description.strip()
        default = '\xe6\xb9\x98\xe6\xbd\xad\xe9\xab\x98\xe6\x96\xb0\xe5\x8c\xba\xe5\x9c\xb0\xe7\xa8\x8e\xe5\xb1\x80\xe7\xa8\x8e\xe5\x8a\xa1\xe7\xae\xa1\xe7\x90\x86\xe4\xbf\xa1\xe6\x81\xaf'
        if des == default:
            return ""
        return des
    
    def getProcessor(self):
        "get processor"
        obj = self.context
        if obj.shuiguanyuan !="":
            return obj.shuiguanyuan
        else:
            return obj.creators[0]
        
    def currentDate(self):
        return datetime.now().strftime('%Y-%m-%d')
                 
  
class NashuirenEdit(NashuirenView):
    """nashuiren edit view"""
    @ram.cache(_render_output_cachekey)
    def outputcheckbox(self,obj,width=1):
        "根据参数total,braindata,返回jason 输出"
        outhtml = """<table class="table table-condensed bordered inner"><tr class="row">"""        
        nums = 12/width
        for i in range(nums):
            j = str(i+1)
            field = "shenbaofou%s" % j
            objurl = obj.absolute_url()
            if nums == 12:
                objurl = "%s/@@modify_yuedujilu" % objurl
            else:
                objurl = "%s/@@modify_jidujilu" % objurl
            if getattr(obj,field,False) == False:          
                out = """<td class="col-md-%(width)s checkbox">
                <input type="checkbox" />
                <span data-url="%(objurl)s" data-num="%(tdnumber)s" class="switch-style off">&nbsp;</span></td>""" \
                % dict(width=width,objurl=objurl,tdnumber=j)
            else:
                out = """<td class="col-md-%(width)s checkbox">
                <input  type="checkbox" checked="checked" />
                <span data-url="%(objurl)s" data-num="%(tdnumber)s" class="switch-style on">&nbsp;</span></td>""" \
                % dict(width=width,objurl=objurl,tdnumber=j)                                 
            outhtml = "%s%s" %(outhtml ,out)           
        data = """%s</tr></table>"""  % outhtml
        return data  
        
    @ram.cache(_render_output_cachekey)
    def outputnumber(self,obj,width=1):
        "根据参数输出html"
        outhtml = """<table class="table table-condensed bordered inner"><tr class="row number-row">"""    
        nums = 12/width
        for i in range(nums):
            j = str(i+1)
            field = "shenbaocishu%s" % j
            num = getattr(obj,field,0)
            out = """<td class="col-md-%(width)s">
            <span class="number" data-num="%(tdnumber)s" data-url="%(objurl)s">%(num)s</span></td>""" \
                % dict(width=width,objurl=obj.absolute_url(),tdnumber=j,num=num)                                  
            outhtml = "%s%s" %(outhtml ,out)           
        data = """%s</tr>
        <tr class="row form" style=" display:none;">
        <td class="col-md-4 text-center">
        <form class="ajaxform">                          
                         <div class="form-group">
                             <label for="InputComment">输入申报次数</label>
                            <input class="form-control" type="text" value="1"/>
                        </div>
                        <button class="btn btn-default" name="ok">确定</button>
                        <button class="btn btn-default" name="cancel">取消</button>
                     </form>
        </td></tr></table>""" % outhtml
        return data
    
    def getChildDesByName(self,child):
        "get child description by child's id"
        query = self.getPathQuery(child)
        brains = self.catalog()(query)
        num = self.getNumId(child)
        des = brains[0].Description.strip()
        if des =="":
            des = u"点击设置描述".encode("utf-8")        
        out = """<div class="modifydes">
        <form class="ajaxdes" style=" display:none;">                          
                         <div class="form-group">
                             <label for="InputComment">输入详细描述</label>
                            <input class="form-control" type="text" value="%(des)s"/>
                        </div>
                        <button class="btn btn-default" name="ok">确定</button>
                        <button class="btn btn-default" name="cancel">取消</button>
                     </form>
                     <div class="other">其他%(num)s(<span data-id="%(id)s" class="description">%(des)s</span>)</div>
                </div>                                        
        """ % dict(des=des,num=num,id=child)
        return out
    
    def getNumId(self,id):
        "get right's number for the specify id"
        rightchar = id[-1]
        if rightchar == '1' or rightchar == '2':
            return rightchar
        else:
            return ''            
                    
class BaseEdit(dexterity.EditForm):
    grok.name('ajaxedit')
    grok.context(Inashuiren)    
    label = _(u'Edit nashuiren base info')
# avoid autoform functionality
    def updateFields(self):
        pass
    @property
    def fields(self):
        return field.Fields(Inashuiren).select('title','guanlidaima', 'description','dengjiriqi',
                                                 'shuiguanyuan','danganbianhao','status',
                                                 'regtype','caiwufuzeren','caiwufuzerendianhua',
                                                 'banshuiren','banshuirendianhua')

def auto_increment(obj,property):
    "when call the function ,obj 's property auto increment 1"

    old = getattr(obj,property,0)
    setattr(obj,property,old + 1)
    return

# ajax modify nashuiren properties,using setattr
class ModifyProperty(grok.View):
    """AJAX action for modify niandu properties .
    """    
    grok.context(Iniandu)
    grok.name('modify_property')
    grok.require('zope2.View')
    
    def isallfinished(self,obj):
        "统计按年申报的所有税种在该时间段是否都钩对，如果都钩对，返回True"
       
        fd = niandugouduiziduan[0]
        if not getattr(obj,fd,False):
            return False
        else:
            return True 
        
#         for fd in niandugouduiziduan[:2]:
#             if not getattr(obj,fd,False):
#                 return False
#             else:
#                 continue
#         return True
            
    def render(self):    
        datadic = self.request.form
        property = datadic['property']
        shenbaofou = datadic['shenbaofou']
        # get niandu object
        context = self.context
        oldtag = set(context.Subject())       
        # properties in niandu
        niandu_fd = niandugouduiziduan
        niandu_fd.append('guidangzhuangtai')
        if property not in niandu_fd:
            # properties in nashuiren
            obj =context.aq_parent        
        else:
            obj = context                    
        #年度未申报标签
        thetag = ling_subjects[1].encode('utf-8')
        def instring(item):
            pattern = tagroup[0].encode("utf-8")
            if pattern in item:
                return False
            else:
                return True          
        if shenbaofou =="true":
            setattr(obj,property,True)
            if property == "feizhenghurending":
                # remove old nashuiren status tag
                sbs = filter(instring,oldtag)
                newtag = u"%s-%s" % (tagroup[0],u"非正常")
                newtag = newtag.encode("utf-8")
                setattr(obj,"status",newtag.split("-")[-1])
                obj.reindexObject(idxs=["status"])
                sbs.append(newtag)
                oldtag = set(sbs)                
            if property == "zhuxiaoshuiwudengji":
                # remove old nashuiren status tag
                sbs = filter(instring,oldtag)
                newtag = u"%s-%s" % (tagroup[0],u"注销")
                newtag = newtag.encode("utf-8")
                setattr(obj,"status",newtag.split("-")[-1])
                obj.reindexObject(idxs=["status"])
                sbs.append(newtag)
                oldtag = set(sbs)
            if property == "guidangzhuangtai":
                obj.setLayout("nashuiren_view")                
                obj.reindexObject(idxs=["guidangzhuangtai"])
                                 
            #如果所有年报税种已申报，删除年报未申报tag
            if self.isallfinished(obj):                                                                                                        
                if thetag in oldtag:
                    oldtag.remove(thetag)
            # remove 零申报标签
            weishenbao = ling_subjects[0].encode('utf-8')
            if weishenbao in oldtag:
                oldtag.remove(weishenbao)                     
        else:
            setattr(obj,property,False)
            if property == "guidangzhuangtai":
                obj.setLayout("nashuiren_edit")             
            if thetag not in oldtag:
                oldtag.add(thetag)
                #todo 适当时机增加零申报
#                 if len(oldtag) == 1:
#                     oldtag.add(weishenbao)
        if oldtag != set(context.Subject()):
            context.setSubject(tuple(oldtag))
            context.reindexObject(idxs=["Subject"])            
        
#         nobj = context.aq_parent        
        context.setModificationDate(datetime.now().strftime(fmt))
        context.reindexObject(idxs=['modified'])
        ajaxtext = u"<p class='text-success'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)     
 
 # ajax modify yuedu jilu,jidu jilu
class BatchModify(grok.View):
    """AJAX action for batch modify yuedu jilu.
    """    
#     grok.context(Inashuiren)
    grok.context(Iniandu)
    grok.name('batch_modify')
    grok.require('zope2.View')
    
    @memoize    
    def catalog(self):
        context = aq_inner(self.context)
        pc = getToolByName(context, "portal_catalog")
        return pc

    def tagmap(self,num):
        yuedult = ['月份-一月',
                  '月份-二月',
                  '月份-三月',
                  '月份-四月',
                  '月份-五月',
                  '月份-六月',
                  '月份-七月',
                  '月份-八月',
                  '月份-九月',
                  '月份-十月',
                  '月份-十一月',
                  '月份-十二月'
                  ]
        jidult = ['季度-一季度',
                  '季度-二季度',
                  '季度-三季度',
                  '季度-四季度'
                  ]
        if num == 12:                    
            return yuedult
        else:
            return jidult
        
    def render(self):    
        datadic = self.request.form
        objid = datadic['objid']
        nums = int(datadic['number'])
        shenbaofou = datadic['action']
        if shenbaofou == 'selectall':
            shenbaofou = True            
            nianduobj = self.context
            oldtag = set(nianduobj.Subject())
            # remove 零申报标签
            weishenbao = ling_subjects[0].encode('utf-8')
            if weishenbao in oldtag:
                oldtag.remove(weishenbao)
            nianduobj.setSubject(tuple(oldtag))
            nianduobj.reindexObject(idxs=["Subject"])            
        else:
            shenbaofou = False

        o = self.context[objid]
        # update mflag
        old = getattr(o,"mflag",0)
        setattr(o,"mflag",old + 1)
        for num in range(nums):
            field = "shenbaofou%s" % str(num + 1)
            setattr(o,field,shenbaofou)
            
        nobj = self.context        
        nobj.setModificationDate(datetime.now().strftime(fmt))
        nobj.reindexObject(idxs=['modified'])        
        ajaxtext = u"<p class='text-success'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)                       

 
 # ajax modify yuedu jilu
class ModifyYuedujilu(grok.View):
    """AJAX action for yuedu jilu.
    """    
    grok.context(Interface)
    grok.name('modify_yuedujilu')
    grok.require('zope2.View')   
    
    def isallfinished(self,field):
        "统计所有税种在该时间段是否都钩对，如果都钩对，返回True"
        #年度对象
        nianduobj = self.context.aq_parent
        for subid,title in subids[:9]:
            #税种对象
            shuizhongobj = nianduobj[subid]
            yes = getattr(shuizhongobj,field,False)
            if yes == False:
                return False
            else:
                continue
        return True                                  
            
    def render(self):    
        datadic = self.request.form
        shenbaofou = datadic['shenbaofou'] 
        nums = str(datadic['number'])
        field = "shenbaofou%s" % nums
#         import pdb
#         pdb.set_trace()        
        nianduobj = self.context.aq_parent
        oldtag = set(nianduobj.Subject())
        rurl = self.request.getURL()
        if rurl.endswith('modify_yuedujilu'): 
            #该月度未申报标签
            thetag = yuedu_subjects[int(nums) - 1].encode('utf-8')
        else:
            #该季度未申报标签
            thetag = jidu_subjects[int(nums) - 1].encode('utf-8')            
        if shenbaofou =="true":
            setattr(self.context,field,True)            
            #如果该月所有税种已申报，删除该月未申报tag
            if self.isallfinished(field):                                                                                                        
                if thetag in oldtag:
                    oldtag.remove(thetag)
            # remove 零申报标签
            weishenbao = ling_subjects[0].encode('utf-8')
            if weishenbao in oldtag:
                oldtag.remove(weishenbao)           
#             self.context.shenbaofou = True
        else:
            setattr(self.context,field,False)
            if thetag not in oldtag:
                oldtag.add(thetag)
                #todo 适当时机增加零申报
#                 if len(oldtag) == 1:
#                     oldtag.add(weishenbao)
        old = getattr(self.context,"mflag",0)

        setattr(self.context,"mflag",old + 1)
        nianduobj.setSubject(tuple(oldtag))
        nianduobj.reindexObject(idxs=["Subject"])            
#             self.context.shenbaofou = False
#         nobj = nianduobj.aq_parent        
        nianduobj.setModificationDate(datetime.now().strftime(fmt))
        nianduobj.reindexObject(idxs=['modified'])        
        ajaxtext = u"<p class='text-success'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)


class ModifyJidujilu(ModifyYuedujilu):
    """AJAX action for jidu jilu.
    """    
    grok.context(Interface)
    grok.name('modify_jidujilu')
    grok.require('zope2.View')
    
    def isallfinished(self,field):
        "统计所有税种在该时间段是否都钩对，如果都钩对，返回True"
        #年度对象
        nianduobj = self.context.aq_parent
        subid = subids[16][0]
        title = subids[16][1]
        shuizhongobj = nianduobj[subid]
        yes = getattr(shuizhongobj,field,False)
        return yes
#         for subid,title in subids[16]:
#             #按季报税种对象
#             shuizhongobj = nianduobj[subid]
#             yes = getattr(shuizhongobj,field,False)
#             if yes == False:
#                 return False
#             else:
#                 continue
#         return True     
 
 # ajax modify anci jilu
class ModifyAncijlu(grok.View):
    """AJAX action for jidu jilu.
    """    
    grok.context(Interface)
    grok.name('modify_ancijilu')
    grok.require('zope2.View')
    
    def render(self):    
        datadic = self.request.form
        shenbaocishu = int(datadic['shenbaocishu'])
        nums = str(datadic['number'])
        field = "shenbaocishu%s" % nums
        setattr(self.context,field,shenbaocishu)        
#         self.context.shenbaocishu =  shenbaocishu

        old = getattr(self.context,"mflag",0)
        setattr(self.context,"mflag",old + 1)
        nobj = self.context.aq_parent        
        nobj.setModificationDate(datetime.now().strftime(fmt))
        nobj.reindexObject(idxs=['modified'])        
        ajaxtext = u"<p class='text-success'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)
# ajax modify qita description
class ModifyDescription(grok.View):
    """AJAX action for modify description.
    """    
    grok.context(Iniandu)
    grok.name('modify_description')
    grok.require('zope2.View')
    
    def render(self):    
        datadic = self.request.form
        des = datadic['description']

        id = datadic['subobj_id']
#         import pdb
#         pdb.set_trace()        
        subobj = getattr(self.context,id,None)
        if subobj != None:
            subobj.description = des
            subobj.reindexObject(idxs=['description'])

        ajaxtext = u"<p class='text-success'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)
    
# batch set tags, call by front end click. (ajax response)
class ResetSubject(BatchModify):
    """AJAX action for batch reset subject.
    """    
    grok.context(Iniandu)
    grok.name('resetsubject')
    grok.require('zope2.View')
    
    def render(self):    
        datadic = self.request.form
        des = datadic['description']
        
    def nomodifingFilter(brain):
        if brain.created == brain.modified:
            return True
        else:
            return False
    def hasnotsubmit(self):
        "统计未报税的纳税户"
        query = {"object_provides":Inashuiren.__identifier__}
        bns = pc(query)
#     import pdb
#     pdb.set_trace()
        bns = filter(nomodifingFilter,bns)        
        return bns       


class ModifyId(grok.View):
    """AJAX action for modify nashuiren properties .
    """    
    grok.context(Inashuiren)
    grok.name('modify_id')
    grok.require('zope2.View')
    
    def render(self):    
        datadic = self.request.form
        newid = datadic['id']
        context = self.context
        oldid = context.id
        parent = context.aq_parent
        parent.manage_renameObject(oldid, newid) 
        parent[newid].reindexObject()
        ajaxtext = u"<p class='text-success'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)
    