from five import grok
from zope import schema

from plone.directives import form, dexterity

from shuiwu.baoshui import _

class Iyuedujilu(form.Schema):
    """
    gaiyue you shenbao ji dagou,fouze wei kong
    """
    shenbaofou = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 