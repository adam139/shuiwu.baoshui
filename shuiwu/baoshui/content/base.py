#-*- coding: UTF-8 -*-
from zope import schema

from plone.directives import form

from shuiwu.baoshui import _

class Ibase(form.Schema):
    """
    该字段是个标志字段，用来标明对象是否被修改 
    """
    mfloag = schema.Int(title=_(u"xiu gai biao ji"),
                       required=False,
                       default=0)


class Iyuedu(Ibase):
    """
    yuedu jilu base interface
    """
    shenbaofou1 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False)
    shenbaofou2 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 
    shenbaofou3 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 
    shenbaofou4 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 
    shenbaofou5 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 
    shenbaofou6 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False)
    shenbaofou7 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False)
    shenbaofou8 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 
    shenbaofou9 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 
    shenbaofou10 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 
    shenbaofou11 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 
    shenbaofou12 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False)
    
class Ijidu(Ibase):
    """
    jidu jilu base interface
    """
    shenbaofou1 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False)
    shenbaofou2 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 
    shenbaofou3 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 
    shenbaofou4 = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False)
    
class Ianci(Ibase):
    """
    anci base interface
    """
    shenbaocishu1 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0)
    shenbaocishu2 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0) 
    shenbaocishu3 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0) 
    shenbaocishu4 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0) 
    shenbaocishu5 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0) 
    shenbaocishu6 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0)
    shenbaocishu7 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0)
    shenbaocishu8 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0) 
    shenbaocishu9 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0) 
    shenbaocishu10 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0) 
    shenbaocishu11 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0) 
    shenbaocishu12 = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default=0)                                   