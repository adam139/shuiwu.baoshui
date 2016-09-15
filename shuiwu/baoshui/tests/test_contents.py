import unittest

from shuiwu.baoshui.testing import INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, setRoles
from plone.namedfile.file import NamedImage

class InitContents(unittest.TestCase):
    """for test create all content objects"""
    def setUp(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ('Manager',))
        portal.invokeFactory('shuiwu.baoshui.nashuiku', 'nashuiku1',
                             title=u'nashuiku1')        
        portal['nashuiku1'].invokeFactory('shuiwu.baoshui.nashuiren', 'nashuiren1',
                             guanlidaima='888201',
                             year='2016')                                                          

        
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.chengjianshui','chengjianshui1',
#                                                    title="chengjianshui1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.jiaoyufeifujia','jiaoyufeifujia1',
#                                                    title=u"jiaoyufeifujia1")              
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.gerensuodeshui','gerensuodeshui1')
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.yinhuashuianyue','yinhuashuianyue1')
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.qiyesuodeshuiblei','qiyesuodeshuiblei1',
#                                                    title=u"qiyesuodeshuiblei1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.fangchanshui','fangchanshui1',
#                                                    title=u"fangchanshui1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.tudizengzhishui','tudizengzhishui1',
#                                                    title=u"tudizengzhishui1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.shuilijijin','shuilijijin1',
#                                                    title=u"shuilijijin1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.shebaofei','shebaofei1',
#                                                    title=u"shebaofei1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.touzizhegerensuodeshui','touzizhegerensuodeshui1',
#                                                    title=u"touzizhegerensuodeshui1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.zichanfuzaibiao','zichanfuzaibiao1',
#                                                    title=u"zichanfuzaibiao1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.xianjinliuliangbiao','xianjinliuliangbiao1',
#                                                    title=u"xianjinliuliangbiao1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.lirunbiao','lirunbiao1',
#                                                    title=u"lirunbiao1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.baobiaofuzhu','baobiaofuzhu1',
#                                                    title=u"baobiaofuzhu1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.zhifugongzimingxi','zhifugongzimingxi1',
#                                                    title=u"zhifugongzimingxi1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.qiyesuodeshuialei','qiyesuodeshuialei1',
#                                                    title=u"qiyesuodeshuialei1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.fangchanshuifangchanyuanzhi','fangchanshuifangchanyuanzhi1',
#                                                    title=u"fangchanshuifangchanyuanzhi1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.shuilijijinjibao','shuilijijinjibao1',
#                                                    title=u"shuilijijinjibao1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.tudishiyongshui','tudishiyongshui1',
#                                                    title=u"tudishiyongshui1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.yinhuashuianji','yinhuashuianji1',
#                                                    title=u"yinhuashuianji1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.tudizengzhishuianji','tudizengzhishuianji1',
#                                                    title=u"tudizengzhishuianji1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.gonghuijingfei','gonghuijingfei1',
#                                                    title=u"gonghuijingfei1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.yinhuashuizijinzhangbo','yinhuashuizijinzhangbo1',
#                                                    title=u"yinhuashuizijinzhangbo1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.yinhuashuianci','yinhuashuianci1',
#                                                    title=u"yinhuashuianci1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.gengdizhanyongshui','gengdizhanyongshui1',
#                                                    title=u"gengdizhanyongshui1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.qishui','qishui1',
#                                                    title=u"qishui1")
#         portal['nashuiku1']['nashuiren1'].invokeFactory('shuiwu.baoshui.ziyuanshui','ziyuanshui1',
#                                                    title=u"ziyuanshui1")                                                      
# # add month records
#         for i in range(11):
#             j = str(i + 1)
#             id = "yuedujilu%s" % (j)            
#             portal['nashuiku1']['nashuiren1']['chengjianshui1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['jiaoyufeifujia1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['gerensuodeshui1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['yinhuashuianyue1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['qiyesuodeshuiblei1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['fangchanshui1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['tudizengzhishui1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['shuilijijin1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)      
#             portal['nashuiku1']['nashuiren1']['shebaofei1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['touzizhegerensuodeshui1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['zichanfuzaibiao1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['xianjinliuliangbiao1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['lirunbiao1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['baobiaofuzhu1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['zhifugongzimingxi1'].invokeFactory('shuiwu.baoshui.yuedujilu',id,title=id)
# # add anci records
#         for i in range(11):
#             j = str(i + 1)
#             id = "ancijilu%s" % (j)             
#             portal['nashuiku1']['nashuiren1']['yinhuashuizijinzhangbo1'].invokeFactory('shuiwu.baoshui.ancijilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['yinhuashuianci1'].invokeFactory('shuiwu.baoshui.ancijilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['gengdizhanyongshui1'].invokeFactory('shuiwu.baoshui.ancijilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['qishui1'].invokeFactory('shuiwu.baoshui.ancijilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['ziyuanshui1'].invokeFactory('shuiwu.baoshui.ancijilu',id,title=id)                                                
# # add jidu records
#         for i in range(3):
#             j = str(i + 1)
#             id = "jidujilu%s" % (j)
#             portal['nashuiku1']['nashuiren1']['qiyesuodeshuialei1'].invokeFactory('shuiwu.baoshui.jidujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['fangchanshuifangchanyuanzhi1'].invokeFactory('shuiwu.baoshui.jidujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['shuilijijinjibao1'].invokeFactory('shuiwu.baoshui.jidujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['tudishiyongshui1'].invokeFactory('shuiwu.baoshui.jidujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['yinhuashuianji1'].invokeFactory('shuiwu.baoshui.jidujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['tudizengzhishuianji1'].invokeFactory('shuiwu.baoshui.jidujilu',id,title=id)
#             portal['nashuiku1']['nashuiren1']['gonghuijingfei1'].invokeFactory('shuiwu.baoshui.jidujilu',id,title=id)              
       
        self.portal = portal    
    
class Allcontents(InitContents):
    layer = INTEGRATION_TESTING   
                
    def test_folder_types(self):
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'].id,'nashuiren1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['gonghuijingfei1'].id,'gonghuijingfei1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['tudizengzhishuianji1'].id,'tudizengzhishuianji1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['yinhuashuianji1'].id,'yinhuashuianji1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['tudishiyongshui1'].id,'tudishiyongshui1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['shuilijijinjibao1'].id,'shuilijijinjibao1')                                

        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['yinhuashuianci1'].id,'yinhuashuianci1')                                                      
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['gengdizhanyongshui1'].id,'gengdizhanyongshui1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['qishui1'].id,'qishui1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['ziyuanshui1'].id,'ziyuanshui1')                    

    
    def test_item_types(self):
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['tudizengzhishuianji1']['jidujilu1'].id,'jidujilu1')
        
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['ziyuanshui1']['ancijilu1'].id,'ancijilu1')           
        