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
from threading import Thread
from queue import Queue

class CreateSubobjWorker(Thread):
   def __init__(self, queue):
       Thread.__init__(self)
       self.queue = queue

   def run(self):
       while True:
           # Get the work from the queue and expand the tuple
           directory, type, num  = self.queue.get()
           create_subobj(directory,type,num)
           self.queue.task_done()

def create_subobj(directory,type,num):
    type = "shuiwu.baoshui.%s" % type
    import pdb
    pdb.set_trace()    
    for i in range(num):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
        tmp = api.content.create(type=type,id=id,title=id,container=directory)

def initObjectTreeWithThread(obj,event):
    "init all child objects for the nashuiren object that had been created by front end UI"
       
#     directory = obj
    subids = [('zichanfuzaibiao1','yuedujilu',u'资产负债表',12),
               ('lirunbiao1','yuedujilu',u'利润表',12),
               ('xianjinliuliangbiao1','yuedujilu',u'现金流量表',12),
               ('chengjianjiaoyudifangfujia','yuedujilu',u'城建、教育、地方教育附加申报表',12),
               ('gerensuodeshui1','yuedujilu',u'个人所得税扣缴表',12),
               ('zhifugongzimingxi1','yuedujilu',u'支付工资明细',12),
               ('yinhuashuianyue1','yuedujilu',u'印花税申报表（按月）',12),
               ('canbaojinshenbaobiao','yuedujilu',u'残保金申报表',12),
               ('gonghuijingfei1','yuedujilu',u'工会经费申报表',12),
               ('shuilijijin1','yuedujilu',u'水利基金申报表（月报）',12),
               ('shebaofei1','yuedujilu',u'社保费申报表',12),
               ('fangchanshui1','yuedujilu',u'房产税申报表（租金收入）',12),
               ('tudizengzhishui1','yuedujilu',u'土地增值税申报表（按月）',12),
               ('anyueqita1','yuedujilu',u'其他1',12),
               ('anyueqita2','yuedujilu',u'其他2',12),
               ('qiyesuodeshuialeiblei','jidujilu',u'企业所得税预缴表（A类、B类）',4),
               ('fangchanshuifangchanyuanzhi1','jidujilu',u'房产税申报表（房产原值）',4),
               ('chengzhentudishiyongshui1','jidujilu',u'城镇土地使用税申报表',4), 
               ('anjiqita1','jidujilu',u'按季其他1',4),
               ('anjiqita2','jidujilu',u'按季其他2',4),
               ('yinhuashuizijinzhangbo1','ancijilu',u'印花税申报表（资金帐薄）',12),
               ('ziyuanshui1','ancijilu',u'资源税申报表',12),
               ('gengdizhanyongshui1','ancijilu',u'耕地占用税申报表',12),
               ('anciqita','ancijilu',u'其他',12)                                                                                                           
               ]
   # Create a queue to communicate with the worker threads
    queue = Queue()

   # Put the tasks into the queue as a tuple
    for subid,subtype,title,num in subids:
        title = title.encode('utf-8')
        if subid.endswith('1') or subid.endswith('2'):
            type1 = subid[:-1]
        else:
            type1 = subid
        type="shuiwu.baoshui.%s" % type1
        directory = api.content.create(type=type,id=subid,title=title,container=obj)                  
        queue.put((directory,subtype,num))
   # Create 8 worker threads
    for x in range(7):
        import pdb
        pdb.set_trace()        
        worker = CreateSubobjWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
#         worker.run()
        worker.start()                 
   # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
   
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
    for i in range(12):
        j = str(i + 1)
        id = "yuedujilu%s" % (j)        
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
#         item.title = event.title
#         item.description = event.description
#         item.guanlidaima = event.guanlidaima
# #         item.dengjiriqi = event.dengjiriqi 
#         item.shuiguanyuan = event.shuiguanyuan
#         item.danganbianhao = event.danganbianhao               

#         datearray = event.dengjiriqi.split('-')
#         if len(datearray) >= 3:
#             val = map(int,datearray)
#                
#             item.dengjiriqi = datetime.date(*val)  
#         else:
#             item.dengjiriqi = datetime.date.today()
        item.reindexObject()                
        
    except:
        return    
