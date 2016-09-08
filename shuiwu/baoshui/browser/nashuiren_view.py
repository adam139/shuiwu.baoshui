#-*- coding: UTF-8 -*-
# from five import grok
from z3c.form import field
from Acquisition import aq_inner
from plone.directives import dexterity
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from Products.Five.browser import BrowserView

from shuiwu.baoshui.content.jidujilu import Ijidujilu
from shuiwu.baoshui.content.ancijilu import Iancijilu
from shuiwu.baoshui.content.yuedujilu import Iyuedujilu
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
                out = """<td class="col-md-%(width)s text-center"><input type="checkbox" /></td>""" \
                % dict(width=width)
            else:
                out = """<td class="col-md-%(width)s text-center"><input type="checkbox" checked="checked" /></td>""" \
                % dict(width=width)                                  
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
    
                    


