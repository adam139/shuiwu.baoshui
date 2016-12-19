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
#新增tag分组
tagroup = [u'纳税人状态',u'按税源科室',u'税务管理员']
#年度钩对字段
niandugouduiziduan = ["yinhuashui","chechuanshui","qiyesuodeshuiniandu"]
yuedu_subjects = [u'月度未申报-一月',u'月度未申报-二月',u'月度未申报-三月',u'月度未申报-四月',
               u'月度未申报-五月',u'月度未申报-六月',u'月度未申报-七月',u'月度未申报-八月',u'月度未申报-九月',
               u'月度未申报-十月',u'月度未申报-十一月',u'月度未申报-十二月']
jidu_subjects = [u'季度未申报-一季度',u'季度未申报-二季度',u'季度未申报-三季度',u'季度未申报-四季度']
ling_subjects = [u'其他未申报-零申报',u'其他未申报-年度未申报']

#using for yuedu sort
yuedudic = {u'一月':1,u'二月':2,u'三月':3,u'四月':4,u'五月':5,u'六月':6,u'七月':7,u'八月':8,
            u'九月':9,u'十月':10,u'十一月':11,u'十二月':12}
jidudic = {u'一季度':1,u'二季度':2,u'三季度':3,u'四季度':4}

def initObjectTreeWithThread(obj,event):
    "init all child objects for the nashuiren object that had been created by front end UI"
    
    currentyear = datetime.datetime.today().strftime("%Y")
    target = api.content.create(
    id = currentyear,
    type='shuiwu.baoshui.niandu',
    title=u'%s年度记录' % currentyear,
    container=obj)
    status = obj.status
    description = obj.description
    shuiguanyuan = obj.shuiguanyuan
    init_tags = []
    if status != "":
        group = tagroup[0].encode("utf-8")
        tag = "%s-%s" %(group,status)
        init_tags.append(tag)
    if description != "":
        group = tagroup[1].encode("utf-8")
        tag = "%s-%s" %(group,description)
        init_tags.append(tag)
    if shuiguanyuan != "":
        group = tagroup[2].encode("utf-8")
        tag = "%s-%s" %(group,shuiguanyuan)
        init_tags.append(tag)
    subjects = yuedu_subjects + jidu_subjects + ling_subjects + init_tags   
    obj.setSubject(tuple(subjects))                        
    obj.reindexObject()
   # Put the tasks into the queue as a tuple
    for subid,title in subids:
        title = title.encode('utf-8')
        type="shuiwu.baoshui.%s" % subid
        directory = api.content.create(type=type,id=subid,title=title,container=target)                                                                                                        
 
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
    shuiguanyuan = event.shuiguanyuan
    # 税源科室
    description = event.description
    status = event.status
    try:
        item = api.content.create(
                                  type="shuiwu.baoshui.nashuiren",
                                  container=memberfolder,
                                  id = memberid,
                                  title = event.title,
                                  description = description,
                                  guanlidaima = event.guanlidaima,
                                  shuiguanyuan = shuiguanyuan,
                                  danganbianhao = event.danganbianhao,
                                  dengjiriqi = dengjiriqi,
                                  status = status,
                                  regtype = event.regtype,
                                  caiwufuzeren = event.caiwufuzeren,
                                  caiwufuzerendianhua = event.caiwufuzerendianhua,
                                  banshuiren = event.banshuiren,
                                  banshuirendianhua = event.banshuirendianhua,                                  
                                  safe_id = False)                       
    except:
        return    

def UpdateNashuirenEvent(event):
    """this event be fired by import nashuiren ui
    id,status,regtype,caiwufuzeren,caiwufuzerendianhua,banshuiren,banshuirendianhua
    """

    site = getSite()     
    catalog = getToolByName(site,'portal_catalog')
    try:
        newest = catalog.unrestrictedSearchResults({'object_provides': Inashuiku.__identifier__})
    except:
        return     
    memberfolder = newest[0].getObject()     
    try:
#         import pdb
#         pdb.set_trace()
        item = memberfolder[event.id]
        item.status = event.status
        item.regtype = event.regtype
        item.caiwufuzeren = event.caiwufuzeren
        item.caiwufuzerendianhua = event.caiwufuzerendianhua
        item.banshuiren = event.banshuiren
        item.banshuirendianhua = event.banshuirendianhua    
        description = item.description
        shuiguanyuan = item.shuiguanyuan
        init_tags = []
        if status != "":
            group = tagroup[0].encode("utf-8")
            tag = "%s-%s" %(group,status)
            init_tags.append(tag)
        if description != "":
            group = tagroup[1].encode("utf-8")
            tag = "%s-%s" %(group,description)
            init_tags.append(tag)
        if shuiguanyuan != "":
            group = tagroup[2].encode("utf-8")
            tag = "%s-%s" %(group,shuiguanyuan)
            init_tags.append(tag)
        subjects = yuedu_subjects + jidu_subjects + ling_subjects + init_tags   
        item.setSubject(tuple(subjects))                        
        item.reindexObject()                               
    except:
        return