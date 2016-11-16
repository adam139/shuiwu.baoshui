# -*- coding: utf-8 -*-
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider
from shuiwu.baoshui import _


@provider(IFormFieldProvider)
class INashuirenStatus(model.Schema):

#状态    
    status = schema.Choice(title=_(u"nashui ren zhuangtai"),
#                        required = True,
                       default="zhengchang",
                       vocabulary = 'shuiwu.baoshui.nashuirenstatus')


@implementer(INashuirenStatus)
@adapter(IDexterityContent)
class NashuirenStatus(object):

    def __init__(self, context):
        self.context = context