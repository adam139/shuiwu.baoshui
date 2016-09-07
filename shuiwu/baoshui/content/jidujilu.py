# from five import grok
from zope import schema

from plone.directives import form

from shuiwu.baoshui import _

class Ijidujilu(form.Schema):
    """
    gai jidu you shenbao ji dagou,fouze wei kong
    """
    shenbaofou = schema.Bool(title=_(u"shifou yi shenbao?"),
                       required=False,
                       default=False) 