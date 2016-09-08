#-*- coding: UTF-8 -*-
from plone import api
from zope.event import notify
from zope.component import adapter
from Acquisition import aq_parent
from zope.component import getMultiAdapter
from zope.site.hooks import getSite
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from zope.lifecycleevent.interfaces import IObjectAddedEvent
from shuiwu.baoshui.content.nashuiren import Inashuiren


#fire todoitemwillcreated event for every designer when add or modified product designer on project node
#@adapter(ITeam, IObjectAddedEvent)
def initObjectTree(obj,event):
    "init all child objects for the nashuiren object that had been created by front end UI"

  
    id = 'chengjianshui1'
    title = u'城建税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.chengjianshui',id=id,title=title,container=obj)
    id = 'jiaoyufeifujia1'
    title = u'教育费附加申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.jiaoyufeifujia',id=id,title=title,container=obj)
    id = 'gerensuodeshui1'
    title = u'个人所得税扣缴表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.gerensuodeshui',id=id,title=title,container=obj)
    id = 'yinhuashuianyue1'
    title = u'印花税申报表（按月）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.yinhuashuianyue',id=id,title=title,container=obj)
    id = 'qiyesuodeshuiblei1'
    title = u'企业所得税预缴表（B类）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.qiyesuodeshuiblei',id=id,title=title,container=obj)
    id = 'fangchanshui1'
    title = u'房产税申报表（租金收入）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.fangchanshui',id=id,title=title,container=obj)
    id = 'tudizengzhishui1'
    title = u'土地增值税申报表（按月）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.tudizengzhishui',id=id,title=title,container=obj)
    id = 'shuilijijin1'
    title = u'水利基金申报表（月报）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.shuilijijin',id=id,title=title,container=obj)
    id = 'shebaofei1'
    title = u'社保费申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.shebaofei',id=id,title=title,container=obj)
    id = 'touzizhegerensuodeshui1'
    title = u'投资者个人所得税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.touzizhegerensuodeshui',id=id,title=title,container=obj)
    id = 'zichanfuzaibiao1'
    title = u'资产负债表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.zichanfuzaibiao',id=id,title=title,container=obj)
    id = 'xianjinliuliangbiao1'
    title = u'现金流量表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.xianjinliuliangbiao',id=id,title=title,container=obj)
    id = 'lirunbiao1'
    title = u'利润表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.lirunbiao',id=id,title=title,container=obj)
    id = 'baobiaofuzhu1'
    title = u'报表附注'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.baobiaofuzhu',id=id,title=title,container=obj)
    id = 'zhifugongzimingxi1'
    title = u'支付工资明细'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.zhifugongzimingxi',id=id,title=title,container=obj)
#季度    
    id = 'qiyesuodeshuialei1'
    title = u'企业所得税预缴表（A类）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.qiyesuodeshuialei',id=id,title=title,container=obj)
    id = 'fangchanshuifangchanyuanzhi1'
    title = u'房产税申报表（房产原值）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.fangchanshuifangchanyuanzhi',id=id,title=title,container=obj)
    id = 'shuilijijinjibao1'
    title = u'水利基金申报表（季报）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.shuilijijinjibao',id=id,title=title,container=obj)
    id = 'tudishiyongshui1'
    title = u'土地使用税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.tudishiyongshui',id=id,title=title,container=obj)
    id = 'yinhuashuianji1'
    title = u'印花税申报表（按季）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.yinhuashuianji',id=id,title=title,container=obj)
    id = 'tudizengzhishuianji1'
    title = u'土地增值税申报表（按季）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.tudizengzhishuianji',id=id,title=title,container=obj)
    id = 'gonghuijingfei1'
    title = u'工会经费申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.gonghuijingfei',id=id,title=title,container=obj)

#按次
    id = 'yinhuashuizijinzhangbo1'
    title = u'印花税申报表（资金帐薄）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.yinhuashuizijinzhangbo',id=id,title=title,container=obj)
    id = 'yinhuashuianci1'
    title = u'印花税申报表（按次）'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.yinhuashuianci',id=id,title=title,container=obj)
    id = 'gengdizhanyongshui1'
    title = u'耕地占用税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.gengdizhanyongshui',id=id,title=title,container=obj)
    id = 'qishui1'
    title = u'契税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.qishui',id=id,title=title,container=obj)
    id = 'ziyuanshui1'
    title = u'资源税申报表'.encode("utf-8")
    item = api.content.create(type='shuiwu.baoshui.ziyuanshui',id=id,title=title,container=obj)                                
                                                                            
    
