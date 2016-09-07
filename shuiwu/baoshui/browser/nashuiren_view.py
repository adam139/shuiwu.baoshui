#-*- coding: UTF-8 -*-
# from five import grok
from z3c.form import field
from plone.directives import dexterity
from plone.memoize.instance import memoize
from Products.Five.browser import BrowserView
from shuiwu.baoshui.content.jidujilu import IJidujilu
from shuiwu.baoshui.content.yuedujilu import Iyuedujilu
from shuiwu.baoshui.content.ziyuanshui import IZiyuanshui
from shuiwu.baoshui.content.qishui import IQishui
from shuiwu.baoshui.content.gengdizhanyongshui import IGengdizhanyongshui
from shuiwu.baoshui.content.yinhuashuianci import IYinhuashuianci
from shuiwu.baoshui.content.yinhuashuizijinzhangbo import IYinhuashuizijinzhangbo
from shuiwu.baoshui.content.gonghuijingfei import IGonghuijingfei
from shuiwu.baoshui.content.tudizengzhishuianji import ITudizengzhishuianji
from shuiwu.baoshui.content.yinhuashuianji import IYinhuashuianji
from shuiwu.baoshui.content.tudishiyongshui import ITudishiyongshui
from shuiwu.baoshui.content.shuilijijinjibao import IShuilijijinjibao
from shuiwu.baoshui.content.fangchanshuifangchanyuanzhi import IFangchanshuifangchanyuanzhi
from shuiwu.baoshui.content.qiyesuodeshuialei import IQiyesuodeshuialei
from shuiwu.baoshui.content.zhifugongzimingxi import IZhifugongzimingxi
from shuiwu.baoshui.content.baobiaofuzhu import IBaobiaofuzhu
from shuiwu.baoshui.content.lirunbiao import ILirunbiao
from shuiwu.baoshui.content.xianjinliuliangbiao import IXianjinliuliangbiao
from shuiwu.baoshui.content.zichanfuzaibiao import IZichanfuzaibiao
from shuiwu.baoshui.content.touzizhegerensuodeshui import ITouzizhegerensuodeshui
from shuiwu.baoshui.content.shebaofei import IShebaofei
from shuiwu.baoshui.content.shuilijijin import IShuilijijin
from shuiwu.baoshui.content.tudizengzhishui import ITudizengzhishui
from shuiwu.baoshui.content.fangchanshui import IFangchanshui
from shuiwu.baoshui.content.qiyesuodeshuiblei import IQiyesuodeshuiblei
from shuiwu.baoshui.content.yinhuashuianyue import IYinhuashuianyue
from shuiwu.baoshui.content.gerensuodeshui import IGerensuodeshui
from shuiwu.baoshui.content.jiaoyufeifujia import IJiaoyufeifujia
from shuiwu.baoshui.content.chengjianshui import IChengjianshui





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
    
    def getPathQuery(self): 
        "获取查询路径"
        query = {}
        query['path'] = "/".join(self.context.getPhysicalPath())
        return query    
    
    def getChildrensByMonth(self,objid):
        "依据按月度申报的内容对象id，提取其每个月申报记录（是否已申报）"
        
        query = self.getPathQuery()
        query['id'] = objid
        brains = self.catalog()(query)               
        return self.catalog()(query)
    
    def getChildrensByQuarter(self,objid):
        "依据按季度申报的内容对象id，提取其每个季度申报记录"
        return ""
    
    def getChildrensByNumber(self,objid):
        "依据按次申报的内容对象id，提取其每月的申报次数"
        return ""        
    
    def output(self,totalnum,braindata):
        "根据参数total,braindata,返回jason 输出"
        outhtml = ""      
        k = 0
        for i in braindata:          
            out = """<tr class="text-left">
                                <td class="col-md-1 text-center">%(num)s</td>
                                <td class="col-md-3 text-left"><a href="%(objurl)s">%(title)s</a></td>
                                <td class="col-md-7">%(description)s</td>
                                <td class="col-md-1 text-center">%(date)s</td>                                
                            </tr> """% dict(objurl="%s/view" % i.getURL(),
                                            num=str(k + 1),
                                            title=i.Title,
                                            description= i.Description,
                                            date = i.created.strftime('%Y-%m-%d'))           
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1 
           
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data 
    
                    


