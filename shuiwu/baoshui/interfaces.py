#-*- coding: UTF-8 -*-
from zope.interface import Interface
# event
class  ICreateNashuirenEvent(Interface):
    """新增一个纳税人对象"""
class  IUpdateNashuirenEvent(Interface):
    """更新纳税人对象，添加几个新增字段"""    
