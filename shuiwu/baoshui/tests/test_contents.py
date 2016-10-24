#-*- coding: UTF-8 -*-
import unittest
import datetime
from shuiwu.baoshui.testing import INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, setRoles


class InitContents(unittest.TestCase):
    """for test create all content objects"""
    def setUp(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ('Manager',))
        portal.invokeFactory('shuiwu.baoshui.nashuiku', 'nashuiku1',
                             title=u'nashuiku1')        
        portal['nashuiku1'].invokeFactory('shuiwu.baoshui.nashuiren', 'nashuiren1',
                             guanlidaima='888201',
                             dengjiriqi=datetime.datetime.today(),
                             year='2016')                                                                 
      
        self.portal = portal    
    
class Allcontents(InitContents):
    layer = INTEGRATION_TESTING   
                
    def test_folder_types(self):
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'].id,'nashuiren1')
#         import pdb
#         pdb.set_trace()
#按月
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['zichanfuzaibiao'].id,'zichanfuzaibiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['xianjinliuliangbiao'].id,'xianjinliuliangbiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['lirunbiao'].id,'lirunbiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['chengjianjiaoyudifangfujia'].id,'chengjianjiaoyudifangfujia')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['gerensuodeshui'].id,'gerensuodeshui')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['zhifugongzimingxi'].id,'zhifugongzimingxi')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['yinhuashuianyue'].id,'yinhuashuianyue')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['canbaojinshenbaobiao'].id,'canbaojinshenbaobiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['gonghuijingfei'].id,'gonghuijingfei')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['shuilijijin'].id,'shuilijijin') 
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['shebaofei'].id,'shebaofei')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['fangchanshui'].id,'fangchanshui')                                        
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['tudizengzhishuianyue'].id,'tudizengzhishuianyue') 
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['anyueqita1'].id,'anyueqita1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['anyueqita2'].id,'anyueqita2')
#按季度

        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['qiyesuodeshuialeiblei'].id,'qiyesuodeshuialeiblei')                                                      
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['fangchanshuifangchanyuanzhi'].id,'fangchanshuifangchanyuanzhi')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['chengzhentudishiyongshui'].id,'chengzhentudishiyongshui')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['anjiqita1'].id,'anjiqita1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['anjiqita2'].id,'anjiqita2')          
# 按次
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['yinhuashuizijinzhangbo'].id,'yinhuashuizijinzhangbo')                                                      
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['gengdizhanyongshui'].id,'gengdizhanyongshui')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['anciqita'].id,'anciqita')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['ziyuanshui'].id,'ziyuanshui')                    

         
        