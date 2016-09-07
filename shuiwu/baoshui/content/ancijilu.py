from five import grok
from zope import schema

from plone.directives import form, dexterity

from shuiwu.baoshui import _

class Iancijilu(form.Schema):
    """
    gai yue shenbao cishu
    """
    shenbaocishu = schema.Int(title=_(u"gaiyue shenbao cishu"),
                       required=False,
                       default= 0) 