
from zope import schema

from plone.directives import form

from shuiwu.baoshui import _

class Iyuedu(form.Schema):
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
    
class Ijidu(form.Schema):
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
    
class Ianci(form.Schema):
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