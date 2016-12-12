#-*- coding: UTF-8 -*-
from zope import interface
from shuiwu.baoshui.interfaces import ICreateNashuirenEvent

class CreateNashuirenEvent(object):
    interface.implements(ICreateNashuirenEvent)
    
    def __init__(self,id,title,guanlidaima,dengjiriqi,description,
                                                shuiguanyuan,danganbianhao,status,regtype,
                                                caiwufuzeren,caiwufuzerendianhua,banshuiren,
                                                banshuirendianhua):
        """导入数据"""
        self.id = id
        self.title = title
        self.guanlidaima = guanlidaima 
        self.dengjiriqi = dengjiriqi        
        self.description = description
        self.shuiguanyuan = shuiguanyuan 
        self.danganbianhao = danganbianhao
        self.status = status
        self.regtype = regtype
        self.caiwufuzeren = caiwufuzeren
        self.caiwufuzerendianhua = caiwufuzerendianhua
        self.banshuiren = banshuiren
        self.banshuirendianhua = banshuirendianhua
        
        