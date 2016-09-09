#-*- coding: UTF-8 -*-
from zope import interface
from shuiwu.baoshui.interfaces import ICreateNashuirenEvent

class CreateNashuirenEvent(object):
    interface.implements(ICreateNashuirenEvent)
    
    def __init__(self,id,title,guanlidaima,dengjiriqi,description,
                                                shuiguanyuan,danganbianhao):
        """导入数据"""
        self.id = id
        self.title = title
        self.guanlidaima = guanlidaima 
        self.dengjiriqi = dengjiriqi        
        self.description = description
        self.shuiguanyuan = shuiguanyuan 
        self.danganbianhao = danganbianhao