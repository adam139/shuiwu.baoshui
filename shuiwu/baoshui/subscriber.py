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
import datetime

subids = [('zichanfuzaibiao',u'资产负债表'),
               ('lirunbiao',u'利润表'),
               ('xianjinliuliangbiao',u'现金流量表'),
               ('chengjianjiaoyudifangfujia',u'城建、教育、地方教育附加申报表'),
               ('gerensuodeshui',u'个人所得税扣缴表'),
               ('zhifugongzimingxi',u'支付工资明细'),
               ('yinhuashuianyue',u'印花税申报表（按月）'),
               ('canbaojinshenbaobiao',u'残保金申报表'),
               ('gonghuijingfei',u'工会经费申报表'),
               ('shuilijijin',u'水利基金申报表（月报）'),
               ('shebaofei',u'社保费申报表'),
               ('fangchanshui',u'房产税申报表（租金收入）'),
               ('tudizengzhishui',u'土地增值税申报表（按月）'),
               ('rukupingzheng',u'入库凭证（按月）'),
               ('anyueqita1',u'其他1'),
               ('anyueqita2',u'其他2'),
               ('qiyesuodeshuialeiblei',u'企业所得税预缴表（A类、B类）'),
               ('fangchanshuifangchanyuanzhi',u'房产税申报表（房产原值）'),
               ('chengzhentudishiyongshui',u'城镇土地使用税申报表'), 
               ('anjiqita1',u'按季其他'),
               ('anjiqita2',u'按季其他'),
               ('yinhuashuizijinzhangbo',u'印花税申报表（资金账簿）'),
               ('ziyuanshui',u'资源税申报表'),
               ('gengdizhanyongshui',u'耕地占用税申报表'),
               ('anciqita',u'其他')                                                                                                           
               ]

def initObjectTreeWithThread(obj,event):
    "init all child objects for the nashuiren object that had been created by front end UI"      

   # Put the tasks into the queue as a tuple
    for subid,title in subids:
        title = title.encode('utf-8')
        type="shuiwu.baoshui.%s" % subid
        directory = api.content.create(type=type,id=subid,title=title,container=obj)                  


   
#fire todoitemwillcreated event for every designer when add or modified product designer on project node
#@adapter(ITeam, IObjectAddedEvent)
def initObjectTree(obj,event):
    "init all child objects for the nashuiren object that had been created by front end UI"

    id = 'zichanfuzaibiao'
    title = u'资产负债表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.zichanfuzaibiao',id=id,title=title,container=obj)
    
    id = 'lirunbiao'
    title = u'利润表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.lirunbiao',id=id,title=title,container=obj)
    
    id = 'xianjinliuliangbiao'
    title = u'现金流量表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.xianjinliuliangbiao',id=id,title=title,container=obj)
   
  
    id = 'chengjianjiaoyudifangfujia'
    title = u'城建、教育、地方教育附加申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.chengjianjiaoyudifangfujia',id=id,title=title,container=obj)
    # add month records

    id = 'gerensuodeshui'
    title = u'个人所得税扣缴表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.gerensuodeshui',id=id,title=title,container=obj)
        
    id = 'zhifugongzimingxi'
    title = u'支付工资明细'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.zhifugongzimingxi',id=id,title=title,container=obj)

    id = 'yinhuashuianyue'
    title = u'印花税申报表（按月）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.yinhuashuianyue',id=id,title=title,container=obj)
   
    id = 'canbaojinshenbaobiao'
    title = u'残保金申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.canbaojinshenbaobiao',id=id,title=title,container=obj)
    
   
    id = 'gonghuijingfei'
    title = u'工会经费申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.gonghuijingfei',id=id,title=title,container=obj)
    
    id = 'shuilijijin'
    title = u'水利基金申报表（月报）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.shuilijijin',id=id,title=title,container=obj)
   
    id = 'shebaofei'
    title = u'社保费申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.shebaofei',id=id,title=title,container=obj)

    id = 'fangchanshui'
    title = u'房产税申报表（租金收入）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.fangchanshui',id=id,title=title,container=obj)
   
    id = 'tudizengzhishuianyue'
    title = u'土地增值税申报表（按月）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.tudizengzhishuianyue',id=id,title=title,container=obj)
    id = 'tudizengzhishuianyue'
    title = u'入库凭证（按月）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.rukupingzheng',id=id,title=title,container=obj)
    id = 'anyueqita'
    title = u'其他'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.anyueqita',id=id,title=title,container=obj)
   
    id = 'anyueqita'
    title = u'其他'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.anyueqita',id=id,title=title,container=obj)
   
    
    

#季度    
    id = 'qiyesuodeshuialeiblei'
    title = u'企业所得税预缴表（A类、B类）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.qiyesuodeshuialeiblei',id=id,title=title,container=obj)
   
    id = 'fangchanshuifangchanyuanzhi'
    title = u'房产税申报表（房产原值）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.fangchanshuifangchanyuanzhi',id=id,title=title,container=obj)
   
 
    id = 'chengzhentudishiyongshui'
    title = u'城镇土地使用税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.chengzhentudishiyongshui',id=id,title=title,container=obj)
   
    id = 'anjiqita'
    title = u'按季其他'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.anjiqita',id=id,title=title,container=obj)
   
    id = 'anjiqita'
    title = u'按季其他'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.anjiqita',id=id,title=title,container=obj)
   

#按次
    id = 'yinhuashuizijinzhangbo'
    title = u'印花税申报表（资金账簿）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.yinhuashuizijinzhangbo',id=id,title=title,container=obj)
   
    id = 'ziyuanshui'
    title = u'资源税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.ziyuanshui',id=id,title=title,container=obj)                                
   
    id = 'gengdizhanyongshui'
    title = u'耕地占用税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.gengdizhanyongshui',id=id,title=title,container=obj)
   
    id = 'anciqita'
    title = u'其他'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.anciqita',id=id,title=title,container=obj)
    
                                                                           
 
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
    datearray = event.dengjiriqi.split('-')
    if len(datearray) >= 3:
        val = map(int,datearray)
               
        dengjiriqi = datetime.date(*val)  
    else:
        dengjiriqi = datetime.date.today()    
    try:
        item = api.content.create(
                                  type="shuiwu.baoshui.nashuiren",
                                  container=memberfolder,
                                  id = memberid,
                                  title = event.title,
                                  description = event.description,
                                  guanlidaima = event.guanlidaima,
                                  shuiguanyuan = event.shuiguanyuan,
                                  danganbianhao = event.danganbianhao,
                                  dengjiriqi = dengjiriqi,
                                  safe_id = False)

        item.reindexObject()                
        
    except:
        return    
