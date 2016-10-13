#-*- coding: UTF-8 -*-
from plone import api
from five import grok
from zope.event import notify
from zope.component import adapter
from Acquisition import aq_parent
from zope.component import getMultiAdapter
from zope.site.hooks import getSite
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from zope.lifecycleevent.interfaces import IObjectAddedEvent
from shuiwu.baoshui.content.nashuiren import Inashuiren
from shuiwu.baoshui.content.nashuiku import Inashuiku
from shuiwu.baoshui.interfaces import ICreateNashuirenEvent


#fire todoitemwillcreated event for every designer when add or modified product designer on project node
#@adapter(ITeam, IObjectAddedEvent)
def initObjectTree(obj,event):
    "init all child objects for the nashuiren object that had been created by front end UI"

    id = 'zichanfuzaibiao1'
    title = u'资产负债表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.zichanfuzaibiao',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)    
    id = 'lirunbiao1'
    title = u'利润表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.lirunbiao',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)     
    id = 'xianjinliuliangbiao1'
    title = u'现金流量表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.xianjinliuliangbiao',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)    
  
    id = 'chengjianjiaoyudifangfujia'
    title = u'城建、教育、地方教育附加申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.chengjianjiaoyudifangfujia',id=id,title=title,container=obj)
    # add month records
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)
    id = 'gerensuodeshui1'
    title = u'个人所得税扣缴表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.gerensuodeshui',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)         
    id = 'zhifugongzimingxi1'
    title = u'支付工资明细'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.zhifugongzimingxi',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)
    id = 'yinhuashuianyue1'
    title = u'印花税申报表（按月）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.yinhuashuianyue',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)    
    id = 'canbaojinshenbaobiao'
    title = u'残保金申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.canbaojinshenbaobiao',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)    
   
    id = 'gonghuijingfei1'
    title = u'工会经费申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.gonghuijingfei',id=id,title=title,container=obj)
    for i in range(4):
        j = str(i + 1)
        id = "jidujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)    
    id = 'shuilijijin1'
    title = u'水利基金申报表（月报）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.shuilijijin',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)    
    id = 'shebaofei1'
    title = u'社保费申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.shebaofei',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)
    id = 'fangchanshui1'
    title = u'房产税申报表（租金收入）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.fangchanshui',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)    
    id = 'tudizengzhishui1'
    title = u'土地增值税申报表（按月）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.tudizengzhishuianyue',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)
    id = 'anyueqita1'
    title = u'其他1'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.anyueqita1',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)    
    id = 'anyueqita2'
    title = u'其他2'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.anyueqita2',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.yuedujilu',id=id,title=id,container=item)    
    
    

#季度    
    id = 'qiyesuodeshuialeiblei'
    title = u'企业所得税预缴表（A类、B类）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.qiyesuodeshuialeiblei',id=id,title=title,container=obj)
    for i in range(4):
        j = str(i + 1)
        id = "jidujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.jidujilu',id=id,title=id,container=item)    
    id = 'fangchanshuifangchanyuanzhi1'
    title = u'房产税申报表（房产原值）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.fangchanshuifangchanyuanzhi',id=id,title=title,container=obj)
    for i in range(4):
        j = str(i + 1)
        id = "jidujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.jidujilu',id=id,title=id,container=item)    
 
    id = 'chengzhentudishiyongshui1'
    title = u'城镇土地使用税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.chengzhentudishiyongshui',id=id,title=title,container=obj)
    for i in range(4):
        j = str(i + 1)
        id = "jidujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.jidujilu',id=id,title=id,container=item)    
    id = 'anjiqita1'
    title = u'按季其他1'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.anjiqita1',id=id,title=title,container=obj)
    for i in range(4):
        j = str(i + 1)
        id = "jidujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.jidujilu',id=id,title=id,container=item)    
    id = 'anjiqita2'
    title = u'按季其他2'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.anjiqita2',id=id,title=title,container=obj)
    for i in range(4):
        j = str(i + 1)
        id = "jidujilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.jidujilu',id=id,title=id,container=item)    

#按次
    id = 'yinhuashuizijinzhangbo1'
    title = u'印花税申报表（资金帐薄）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.yinhuashuizijinzhangbo',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "ancijilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.ancijilu',id=id,title=id,container=item)    
    id = 'ziyuanshui1'
    title = u'资源税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.ziyuanshui',id=id,title=title,container=obj)                                
    for i in range(12):
        j = str(i + 1)
        id = "ancijilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.ancijilu',id=id,title=id,container=item)    
    id = 'gengdizhanyongshui1'
    title = u'耕地占用税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.gengdizhanyongshui',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "ancijilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.ancijilu',id=id,title=id,container=item)    
    id = 'anciqita'
    title = u'其他'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.anciqita',id=id,title=title,container=obj)
    for i in range(12):
        j = str(i + 1)
        id = "ancijilu%s" % (j)        
        tmp = api.content.create(type='shuiwu.baoshui.ancijilu',id=id,title=id,container=item)    
                                                                           
 
# @grok.subscribe(ICreateNashuirenEvent)
def CreateNashuirenEvent(event):
    """this event be fired by import nashuiren ui"""

    site = getSite()
     
    catalog = getToolByName(site,'portal_catalog')
    try:
        newest = catalog.unrestrictedSearchResults({'object_provides': Inashuiku.__identifier__})
    except:
        return      

    memberfolder = newest[0].getObject()
    memberid = event.id        
    try:
        item = api.content.create(
                                  type="shuiwu.baoshui.nashuiren",
                                  container=memberfolder,
                                  id = memberid,
                                  safe_id = True)
#         item =createContentInContainer(memberfolder,"shuiwu.baoshui.nashuiren",checkConstraints=False,id=memberid)

        item.title = event.title
        item.description = event.description
        item.guanlidaima = event.guanlidaima
#         item.dengjiriqi = event.dengjiriqi 
        item.shuiguanyuan = event.shuiguanyuan
        item.danganbianhao = event.danganbianhao
        
        import datetime

        datearray = event.dengjiriqi.split('-')
        if len(datearray) >= 3:
            val = map(int,datearray)
               
            item.dengjiriqi = datetime.date(*val)  
        else:
            item.dengjiriqi = datetime.date.today()
#set default view        
#         item.setLayout('nashuiren_view')
        item.reindexObject()                
        
    except:
        return    
