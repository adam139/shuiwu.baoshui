#-*- coding: UTF-8 -*-
from plone.directives import form
from zope import schema
from shuiwu.baoshui import _

class Iniandu(form.Schema):
    """
    niandu container
    """
#年度记录
    yinhuashui = schema.Bool(title=_(u"yinhuashui shenbaobiao(yingyezhangbo)"),
                       required=False,
                       default=False)
    chechuanshui = schema.Bool(title=_(u"chechuanshui shenbaobiao"),
                       required=False,
                       default=False)
#     canjirenbaozhengjin = schema.Bool(title=_(u"canjirenbaozhengjin shenbaobiao"),
#                        required=False,
#                        default=False)
#     difangshuihuisuan = schema.Bool(title=_(u"difang geshui huisuan qingjiaobiao"),
#                        required=False,
#                        default=False)    
#     gerensuodeshuiniandu = schema.Bool(title=_(u"geren suodeshui niandu shenbaobiao"),
#                        required=False,
#                        default=False)
    qiyesuodeshuiniandu = schema.Bool(title=_(u"qiye suodeshui niandu shenbaobiao ji huisuan qinjiao fudaojilu"),
                       required=False,
                       default=False)
#     zhuxiaoshuiwudengji = schema.Bool(title=_(u"zhuxiao shuiwu dengjibiao"),
#                        required=False,
#                        default=False)    