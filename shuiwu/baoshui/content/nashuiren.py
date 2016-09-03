#-*- coding: UTF-8 -*-
from five import grok
from zope import schema

from plone.directives import form, dexterity

from shuiwu.baoshui import _

class INashuiren(form.Schema):
    """
    na shui ren niandu sheshui shenbao jilu
    """
#年度           
    year = schema.TextLine(title=_(u"niandu"),
                             default=u"2012",
                             required=False,)
#管理代码    
    guanlidaima = schema.ASCIILine(
            title=_(u"guanli daima"),
            description=_(u"nashuiren guanli daima."),
            required=True)
#档案编号     
    danganbianhao = schema.ASCIILine(
            title=_(u"dangan bianhao"),
            required=False)
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
    
    form.omitted('year')
    
@form.default_value(field=INashuiren['year'])
def YearDefaultValue(data):
    # To get hold of the folder, do: context = data.context
#     return (datetime.datetime.today() + datetime.timedelta(-365)).strftime("%Y")
    return datetime.datetime.today().strftime("%Y")                                        