#-*- coding: UTF-8 -*-
import unittest
import datetime
from shuiwu.baoshui.testing import INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, setRoles

currentyear = datetime.datetime.today().strftime("%Y")
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
                             year=currentyear)
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.niandu', currentyear)                                                                         
      
        self.portal = portal    
    
class Allcontents(InitContents):
    layer = INTEGRATION_TESTING   
                
    def test_folder_types(self):
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'].id,'nashuiren1')
#         import pdb
#         pdb.set_trace()
#按月
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['zichanfuzaibiao'].id,'zichanfuzaibiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['xianjinliuliangbiao'].id,'xianjinliuliangbiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['lirunbiao'].id,'lirunbiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['chengjianjiaoyudifangfujia'].id,'chengjianjiaoyudifangfujia')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['gerensuodeshui'].id,'gerensuodeshui')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['zhifugongzimingxi'].id,'zhifugongzimingxi')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['yinhuashuianyue'].id,'yinhuashuianyue')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['canbaojinshenbaobiao'].id,'canbaojinshenbaobiao')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['gonghuijingfei'].id,'gonghuijingfei')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['shuilijijin'].id,'shuilijijin') 
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['shebaofei'].id,'shebaofei')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['fangchanshui'].id,'fangchanshui')                                        
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['tudizengzhishui'].id,'tudizengzhishui') 
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['rukupingzheng'].id,'rukupingzheng')        
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['anyueqita1'].id,'anyueqita1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['anyueqita2'].id,'anyueqita2')
#按季度

        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['qiyesuodeshuialeiblei'].id,'qiyesuodeshuialeiblei')                                                      
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['fangchanshuifangchanyuanzhi'].id,'fangchanshuifangchanyuanzhi')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['chengzhentudishiyongshui'].id,'chengzhentudishiyongshui')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['anjiqita1'].id,'anjiqita1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['anjiqita2'].id,'anjiqita2')          
# 按次
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['yinhuashuizijinzhangbo'].id,'yinhuashuizijinzhangbo')                                                      
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['gengdizhanyongshui'].id,'gengdizhanyongshui')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['anciqita'].id,'anciqita')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'][currentyear]['ziyuanshui'].id,'ziyuanshui')                    

         
        