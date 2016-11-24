#-*- coding: UTF-8 -*-
from five import grok
from zope import schema
import datetime
from plone.directives import form, dexterity
from plone.app.dexterity.behaviors.metadata import IBasic
from collective import dexteritytextindexer

from shuiwu.baoshui import _

class Inashuiren(form.Schema,IBasic):
    """
    na shui ren niandu sheshui shenbao jilu
    """
# 纳税人名称/所属科室/税管员、税务登记日期
    dexteritytextindexer.searchable('title')
    title = schema.TextLine(title=_(u"nashuiren mingcheng"),
                             default=u"",
                             required=True,)
#主管税务所（科、分局）    
    description = schema.TextLine(title=_(u"nashuiren suoshu keshi"),
                             default=u"",
                             required=True,)
#   税务登记日期 
    dengjiriqi = schema.Date(
        title=_(u"dengji riqi"),
        description=u'',
        required=True,)        
#主管税务机关
    zhuguanshuiwujiguan = schema.TextLine(title=_(u"zhu guan shuiwu jiguan"),
                             default=u"",
                             required=False,)


#税收管理员
    shuiguanyuan = schema.TextLine(title=_(u"shuishou guanlirenyuan"),
                             default=u"",
                             required=False,)

#当前报表年度           
    year = schema.TextLine(title=_(u"niandu"),
                             default=u"2012",
                             required=False,)
#管理代码    
    dexteritytextindexer.searchable('guanlidaima')
    guanlidaima = schema.ASCIILine(
            title=_(u"guanli daima"),
            description=_(u"shehui xingren daima (nashuiren shibiehao)"),
            required=True)
#档案编号     
    danganbianhao = schema.ASCIILine(
            title=_(u"dangan bianhao"),
            required=False)
#小规模认定
    xiaoguimo = schema.Bool(title=_(u"xiao guimo nashuiren rending"),
                       required=False,
                      default=False)
#状态    
    status = schema.TextLine(title=_(u"nashui ren zhuangtai"),
                       required = True,
                       default=u"")
#登记注册类型
    type = schema.TextLine(title=_(u"nashui dengji zhuce leixing"),
                       required = True,
                       default=u"")
#财务负责人    
    caiwufuzeren = schema.TextLine(title=_(u"caiwu fuze ren"),
                       required=False,
                       default=u"")
#财务负责人电话    
    caiwufuzerendianhua = schema.TextLine(title=_(u"caiwu fuze ren dianhua"),
                       required=False,
                       default=u"")

#办税人    
    banshuiren = schema.TextLine(title=_(u"banshui ren"),
                       required=False,
                       default=u"")
#办税人电话    
    banshuirendianhua = schema.TextLine(title=_(u"banshui ren dianhua"),
                       required=False,
                       default=u"")
            
#年度记录
    yinhuashui = schema.Bool(title=_(u"yinhuashui shenbaobiao(yingyezhangbo)"),
                       required=False,
                       default=False)
    chechuanshui = schema.Bool(title=_(u"chechuanshui shenbaobiao"),
                       required=False,
                       default=False)
    canjirenbaozhengjin = schema.Bool(title=_(u"canjirenbaozhengjin shenbaobiao"),
                       required=False,
                       default=False)
    difangshuihuisuan = schema.Bool(title=_(u"difang geshui huisuan qingjiaobiao"),
                       required=False,
                       default=False)    
    gerensuodeshuiniandu = schema.Bool(title=_(u"geren suodeshui niandu shenbaobiao"),
                       required=False,
                       default=False)
    qiyesuodeshuiniandu = schema.Bool(title=_(u"qiye suodeshui niandu shenbaobiao ji huisuan qinjiao fudaojilu"),
                       required=False,
                       default=False)
    zhuxiaoshuiwudengji = schema.Bool(title=_(u"zhuxiao shuiwu dengjibiao"),
                       required=False,
                       default=False)
    feizhenghurending = schema.Bool(title=_(u"fei zhenghu rending biao"),
                       required=False,
                       default=False)

    
    
    form.omitted('year','zhuguanshuiwujiguan','feizhenghurending','zhuxiaoshuiwudengji'
                 ,'qiyesuodeshuiniandu','gerensuodeshuiniandu','difangshuihuisuan',
                 'canjirenbaozhengjin','chechuanshui','yinhuashui')
    
@form.default_value(field=Inashuiren['dengjiriqi'])
def dengjiriqiDefaultValue(data):
    # To get hold of the folder, do: context = data.context
    return datetime.datetime.today()

@form.default_value(field=Inashuiren['year'])
def YearDefaultValue(data):
    # To get hold of the folder, do: context = data.context
#     return (datetime.datetime.today() + datetime.timedelta(-365)).strftime("%Y")
    return datetime.datetime.today().strftime("%Y")                                        