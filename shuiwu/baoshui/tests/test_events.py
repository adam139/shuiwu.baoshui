#-*- coding: UTF-8 -*-
import unittest
from zope import event
from shuiwu.baoshui.events import CreateNashuirenEvent
from shuiwu.baoshui.testing import INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, setRoles


class InitContents(unittest.TestCase):
    """for test create all content objects"""
    def setUp(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ('Manager',))
        portal.invokeFactory('shuiwu.baoshui.nashuiku', 'nashuiku1',
                             title=u'nashuiku1')                                                               

       
        id="a8001"
        guanlidaima = id
        title=u"某某公司"
        dengjiriqi = "2016-09-12"
        description = u"一科"
        shuiguanyuan = u"张三"
        danganbianhao = "dang%s" % id
        
        event.notify(CreateNashuirenEvent(
                                                id,title,guanlidaima,dengjiriqi,description,
                                                shuiguanyuan,danganbianhao))
        self.portal = portal    
    
class Allevents(unittest.TestCase):
    layer = INTEGRATION_TESTING
       
    def setUp(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ('Manager',))
        portal.invokeFactory('shuiwu.baoshui.nashuiku', 'nashuiku1',
                             title=u'nashuiku1')                                                               

       
        id="a8001"
        guanlidaima = id
        title=u"某某公司"
        dengjiriqi = "2016-09-12"
        description = u"一科"
        shuiguanyuan = u"张三"
        danganbianhao = "dang%s" % id
        
        event.notify(CreateNashuirenEvent(
                                                id,title,guanlidaima,dengjiriqi,description,
                                                shuiguanyuan,danganbianhao))
        self.portal = portal                
    
    
    def test_CreateNashuirenEvent(self):
        self.assertEqual(self.portal['nashuiku1']['a8001'].id,'a8001')
        self.assertEqual(self.portal['nashuiku1']['a8001'].guanlidaima,'a8001')
        self.assertEqual(self.portal['nashuiku1']['a8001'].title,u'某某公司')
        self.assertEqual(self.portal['nashuiku1']['a8001'].description,u'一科')
        self.assertEqual(self.portal['nashuiku1']['a8001'].shuiguanyuan,u'张三')
        self.assertEqual(self.portal['nashuiku1']['a8001'].danganbianhao,'danga8001')                                                

    
    def test_NashuirenObjectAddedEvent(self):
        self.assertEqual(self.portal['nashuiku1']['a8001']['gonghuijingfei1'].id,'gonghuijingfei1')
        self.assertEqual(self.portal['nashuiku1']['a8001']['tudizengzhishuianji1'].id,'tudizengzhishuianji1')
        self.assertEqual(self.portal['nashuiku1']['a8001']['yinhuashuianji1'].id,'yinhuashuianji1')
        self.assertEqual(self.portal['nashuiku1']['a8001']['tudishiyongshui1'].id,'tudishiyongshui1')
        self.assertEqual(self.portal['nashuiku1']['a8001']['shuilijijinjibao1'].id,'shuilijijinjibao1')                               
        self.assertEqual(self.portal['nashuiku1']['a8001']['yinhuashuianci1'].id,'yinhuashuianci1')                                                      
        self.assertEqual(self.portal['nashuiku1']['a8001']['gengdizhanyongshui1'].id,'gengdizhanyongshui1')
        self.assertEqual(self.portal['nashuiku1']['a8001']['qishui1'].id,'qishui1')
        self.assertEqual(self.portal['nashuiku1']['a8001']['ziyuanshui1'].id,'ziyuanshui1')
                 
        self.assertEqual(self.portal['nashuiku1']['a8001']['tudizengzhishuianji1']['jidujilu1'].id,'jidujilu1')        
        self.assertEqual(self.portal['nashuiku1']['a8001']['ziyuanshui1']['ancijilu1'].id,'ancijilu1')           
        