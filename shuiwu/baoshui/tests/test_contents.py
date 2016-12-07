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
                             danganbianhao='888202',
                             dengjiriqi=datetime.datetime.today(),
                             year='2016')
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.niandu', '2016')                                                                         
      
        self.portal = portal    
    
class Allcontents(InitContents):
    layer = INTEGRATION_TESTING   
                
    def test_folder_types(self):
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'].id,'nashuiren1')
        import pdb
        pdb.set_trace()
#按月
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['zichanfuzaibiao'].id,'zichanfuzaibiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['xianjinliuliangbiao'].id,'xianjinliuliangbiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['lirunbiao'].id,'lirunbiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['chengjianjiaoyudifangfujia'].id,'chengjianjiaoyudifangfujia')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['gerensuodeshui'].id,'gerensuodeshui')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['zhifugongzimingxi'].id,'zhifugongzimingxi')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['yinhuashuianyue'].id,'yinhuashuianyue')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['canbaojinshenbaobiao'].id,'canbaojinshenbaobiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['gonghuijingfei'].id,'gonghuijingfei')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['shuilijijin'].id,'shuilijijin') 
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['shebaofei'].id,'shebaofei')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['fangchanshui'].id,'fangchanshui')                                        
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['tudizengzhishui'].id,'tudizengzhishui') 
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['rukupingzheng'].id,'rukupingzheng')        
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['anyueqita1'].id,'anyueqita1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['anyueqita2'].id,'anyueqita2')
#按季度

        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['qiyesuodeshuialeiblei'].id,'qiyesuodeshuialeiblei')                                                      
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['fangchanshuifangchanyuanzhi'].id,'fangchanshuifangchanyuanzhi')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['chengzhentudishiyongshui'].id,'chengzhentudishiyongshui')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['anjiqita1'].id,'anjiqita1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['anjiqita2'].id,'anjiqita2')          
# 按次
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['yinhuashuizijinzhangbo'].id,'yinhuashuizijinzhangbo')                                                      
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['gengdizhanyongshui'].id,'gengdizhanyongshui')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['anciqita'].id,'anciqita')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['2016']['ziyuanshui'].id,'ziyuanshui')                    

         
        