#-*- coding: UTF-8 -*-
from five import grok
import json
from z3c.form import field
from Acquisition import aq_inner
from plone.directives import dexterity
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from Products.Five.browser import BrowserView

from shuiwu.baoshui.content.jidujilu import Ijidujilu
from shuiwu.baoshui.content.ancijilu import Iancijilu
from shuiwu.baoshui.content.yuedujilu import Iyuedujilu
from shuiwu.baoshui.content.nashuiren import Inashuiren
# from shuiwu.baoshui.content.ziyuanshui import IZiyuanshui
# from shuiwu.baoshui.content.qishui import IQishui
# from shuiwu.baoshui.content.gengdizhanyongshui import IGengdizhanyongshui
# from shuiwu.baoshui.content.yinhuashuianci import IYinhuashuianci
# from shuiwu.baoshui.content.yinhuashuizijinzhangbo import IYinhuashuizijinzhangbo
# from shuiwu.baoshui.content.gonghuijingfei import IGonghuijingfei
# from shuiwu.baoshui.content.tudizengzhishuianji import ITudizengzhishuianji
# from shuiwu.baoshui.content.yinhuashuianji import IYinhuashuianji
# from shuiwu.baoshui.content.tudishiyongshui import ITudishiyongshui
# from shuiwu.baoshui.content.shuilijijinjibao import IShuilijijinjibao
# from shuiwu.baoshui.content.fangchanshuifangchanyuanzhi import IFangchanshuifangchanyuanzhi
# from shuiwu.baoshui.content.qiyesuodeshuialei import IQiyesuodeshuialei
# from shuiwu.baoshui.content.zhifugongzimingxi import IZhifugongzimingxi
# from shuiwu.baoshui.content.baobiaofuzhu import IBaobiaofuzhu
# from shuiwu.baoshui.content.lirunbiao import ILirunbiao
# from shuiwu.baoshui.content.xianjinliuliangbiao import IXianjinliuliangbiao
# from shuiwu.baoshui.content.zichanfuzaibiao import IZichanfuzaibiao
# from shuiwu.baoshui.content.touzizhegerensuodeshui import ITouzizhegerensuodeshui
# from shuiwu.baoshui.content.shebaofei import IShebaofei
# from shuiwu.baoshui.content.shuilijijin import IShuilijijin
# from shuiwu.baoshui.content.tudizengzhishui import ITudizengzhishui
# from shuiwu.baoshui.content.fangchanshui import IFangchanshui
# from shuiwu.baoshui.content.qiyesuodeshuiblei import IQiyesuodeshuiblei
# from shuiwu.baoshui.content.yinhuashuianyue import IYinhuashuianyue
# from shuiwu.baoshui.content.gerensuodeshui import IGerensuodeshui
# from shuiwu.baoshui.content.jiaoyufeifujia import IJiaoyufeifujia
# from shuiwu.baoshui.content.chengjianshui import IChengjianshui





# grok.templatedir('templates')

class NashuirenView(BrowserView):
    "nashuiren  view"
#     grok.context(ITeam)
#     grok.template('team_view')
#     grok.name('view')
#     grok.require('emc.project.view_team') 

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
        
        query = self.getPathQuery(objid)
        query['object_provides'] = Iyuedujilu.__identifier__
        brains = self.catalog()(query)
              
        return self.outputcheckbox(brains,width=1)
    
    def getChildrensByQuarter(self,objid):
        "依据按季度申报的内容对象id，提取其每个季度申报记录"
        query = self.getPathQuery(objid)
        query['object_provides'] = Ijidujilu.__identifier__
        brains = self.catalog()(query)               
        return self.outputcheckbox(brains,width=3)
    
    def getChildrensByNumber(self,objid):
        "依据按次申报的内容对象id，提取其每月的申报次数"
        query = self.getPathQuery(objid)
        query['object_provides'] = Iancijilu.__identifier__
        brains = self.catalog()(query)               
        return self.outputnumber(brains,width=1)      
    
    def outputcheckbox(self,braindata,width=1):
        "根据参数total,braindata,返回jason 输出"
        outhtml = """<table class="table bordered inner"><tr class="row">"""      

        for i in braindata:
            o = i.getObject()
            if o.shenbaofou == False:           
                out = """<td class="col-md-%(width)s text-center">
                <input data-id="%(objid)s" type="checkbox" /></td>""" \
                % dict(width=width,objid=i.id)
            else:
                out = """<td class="col-md-%(width)s text-center">
                <input data-id="%(objid)s" type="checkbox" checked="checked" /></td>""" \
                % dict(width=width,objid=i.id)                                  
            outhtml = "%s%s" %(outhtml ,out)
           
        data = """%s</tr></table>"""  % outhtml

        return data
    
    def outputnumber(self,braindata,width=1):
        "根据参数输出html"
        outhtml = """<table class="table bordered inner"><tr class="row">"""      

        for i in braindata:
            o = i.getObject()
            out = """<td class="col-md-%(width)s text-center">%(num)s</td>""" \
                % dict(width=width,num=o.shenbaocishu)                                  
            outhtml = "%s%s" %(outhtml ,out)           
        data = """%s</tr></table>""" % outhtml
        return data
    
    def propertyChecked(self,property):
        "check narenren object,if the property is True"
        obj = self.context
#         import pdb
#         pdb.set_trace()
        pro = getattr(obj,property)
        if pro:
            return True
        else:
            return False
                 
  
class NashuirenEdit(NashuirenView):
    """nashuiren edit view"""

    def outputcheckbox(self,braindata,width=1):
        "根据参数total,braindata,返回jason 输出"
        outhtml = """<table class="table bordered inner"><tr class="row">"""      

        for i in braindata:
            o = i.getObject()
            if o.shenbaofou == False:           
                out = """<td class="col-md-%(width)s text-center checkbox">
                <input type="checkbox" />
                <span data-url="%(objurl)s" class="switch-style off">&nbsp;</span></td>""" \
                % dict(width=width,objurl=o.absolute_url())
            else:
                out = """<td class="col-md-%(width)s text-center checkbox">
                <input  type="checkbox" checked="checked" />
                <span data-url="%(objurl)s" class="switch-style on">&nbsp;</span></td>""" \
                % dict(width=width,objurl=o.absolute_url())                                  
            outhtml = "%s%s" %(outhtml ,out)
           
        data = """%s</tr></table>"""  % outhtml

        return data
    

        
    def outputnumber(self,braindata,width=1):
        "根据参数输出html"
        outhtml = """<table class="table bordered inner"><tr class="row number-row">"""      

        for i in braindata:
            o = i.getObject()
            out = """<td class="col-md-%(width)s text-center">
            <span class="number" data-url="%(objurl)s">%(num)s</span></td>""" \
                % dict(width=width,objurl=o.absolute_url(),num=o.shenbaocishu)                                  
            outhtml = "%s%s" %(outhtml ,out)           
        data = """%s</tr>
        <tr class="row form" style=" display:none;">
        <td class="col-md-4 text-center">
        <form class="ajaxform">                          
                         <div class="form-group">
                             <label for="InputComment">输入申报次数</label>
                            <input class="form-control" type="number" value=""/>
                        </div>
                        <button class="btn btn-default" name="ok">确定</button>
                        <button class="btn btn-default" name="cancel">取消</button>
                     </form>
        </td></tr></table>""" % outhtml
        return data        
                    
# ajax modify nashuiren properties,using setattr
class ModifyProperty(grok.View):
    """AJAX action for modify nashuiren properties .
    """    
    grok.context(Inashuiren)
    grok.name('modify_property')
    grok.require('zope2.View')
    
    def render(self):    
        datadic = self.request.form
        property = datadic['property']
        shenbaofou = datadic['shenbaofou']
        context = self.context 
        if shenbaofou =="true":
           setattr(context,property,True)
        else:
            setattr(context,property,False)
        ajaxtext = u"<p class='text-sccess'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)     
 # ajax modify yuedu jilu,jidu jilu
class BatchModify(grok.View):
    """AJAX action for batch modify yuedu jilu.
    """    
    grok.context(Inashuiren)
    grok.name('batch_modify')
    grok.require('zope2.View')
    
    @memoize    
    def catalog(self):
        context = aq_inner(self.context)
        pc = getToolByName(context, "portal_catalog")
        return pc
        
    def render(self):    
        datadic = self.request.form
        objid = datadic['objid']
        shenbaofou = datadic['action']
        if shenbaofou == 'selectall':
            shenbaofou = True
        else:
            shenbaofou = False
        path = "/".join(self.context.getPhysicalPath())
        path ="%s/%s" %(path,objid)
        query = {}
        query['path'] = path
        query['object_provides'] = [Iyuedujilu.__identifier__,Ijidujilu.__identifier__]
        brains = self.catalog()(query)
        for o in brains:
            obj = o.getObject()
            obj.shenbaofou = shenbaofou
        ajaxtext = u"<p class='text-sccess'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)            
        
        

 
 # ajax modify yuedu jilu
class ModifyYuedujlu(grok.View):
    """AJAX action for yuedu jilu.
    """    
    grok.context(Iyuedujilu)
    grok.name('modify_yuedujilu')
    grok.require('zope2.View')
    
    def render(self):    
        datadic = self.request.form
        shenbaofou = datadic['shenbaofou'] 
        if shenbaofou =="true":
            self.context.shenbaofou = True
        else:
            self.context.shenbaofou = False
        ajaxtext = u"<p class='text-sccess'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)
 # ajax modify yuedu jilu
class ModifyJidujlu(grok.View):
    """AJAX action for jidu jilu.
    """    
    grok.context(Ijidujilu)
    grok.name('modify_jidujilu')
    
    def render(self):    
        datadic = self.request.form
        shenbaofou = datadic['shenbaofou'] 
        if shenbaofou =="true":
            self.context.shenbaofou = True
        else:
            self.context.shenbaofou = False    
        ajaxtext = u"<p class='text-sccess'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)
 
 # ajax modify anci jilu
class ModifyAncijlu(grok.View):
    """AJAX action for jidu jilu.
    """    
    grok.context(Iancijilu)
    grok.name('modify_ancijilu')
    grok.require('zope2.View')
    
    def render(self):    
        datadic = self.request.form
        shenbaocishu = int(datadic['shenbaocishu'])
        self.context.shenbaocishu =  shenbaocishu

        ajaxtext = u"<p class='text-sccess'>更改已保存</p>"
        callback = {"result":True,'message':ajaxtext}
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(callback)
