#-*- coding: UTF-8 -*-
from zope.interface import Interface
from zope.interface import implementer
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory
from plone.registry.interfaces import IRegistry
from five import grok
import json
import datetime
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.CMFCore import permissions

# from plone.directives import dexterity
from plone.memoize.instance import memoize
from shuiwu.baoshui import _
from shuiwu.baoshui.content.nashuiku import Inashuiku
from shuiwu.baoshui.content.nashuiren import Inashuiren

from Products.Five.browser import BrowserView

# from collective.gtags.interfaces import ITagSettings
# from shuiwu.baoshui import viewReport
# from shuiwu.baoshui.interface import IUsersrolesProvider     


class sysAjaxListingView(BrowserView):
    """
    AJAX 查询，返回分页结果,for some contenttypes relative to project
    """
   
               
    @memoize    
    def catalog(self):
        context = aq_inner(self.context)
        pc = getToolByName(context, "portal_catalog")
        return pc
    
    @memoize    
    def pm(self):
        context = aq_inner(self.context)
        pm = getToolByName(context, "portal_membership")
        return pm         
    
    
    def splitTag(self,value):
            """Split a tag into (category, tag) parts. category may be None.
            input: value like abc-a1 or a1
            output:dict like  {'category':abc,'value':a1}
            """
            parts = value.split("-")
            output = {'category':'','value':''}        
    
            if len(parts) == 1:
                output['value'] = value
                return output
            else:
                output['category'] = parts[0]
                output['value'] = parts[1]
                return output
            
    @memoize
    def getTagregistryProxy(self):
        "input keywords vocabulary,\
        output all tags,compose a list,member of the list is unicode"
        factory = queryUtility(IVocabularyFactory, 'plone.app.vocabularies.Keywords')
#         import pdb
#         pdb.set_trace()
        if not factory:
            raise VocabLookupException(
                'No factory with name "%s" exists.' % factory_name)

        vocabulary = factory(self.context)
        tags = [ term.title for term in vocabulary]
#         settings = getUtility(IRegistry).forInterface(ITagSettings)
        return tags
    
    @memoize
    def getTagGroups(self):
        "fetch all tag groups ,it is category part of 'category-value'" 
        tagsets = self.getTagregistryProxy()
        if tagsets ==None:return None
#         import pdb
#         pdb.set_trace()
        # get rid of duplicate
        groups = set(self.splitTag(value)['category'] for value in tagsets if value != "")
        groups = list(groups)
        groups.sort(reverse=True)
        return groups           
    
    def getAllTags(self,category,start=0,size=None):
        """fetch all predefine  tags under the specify category"""
        tagsets = self.getTagregistryProxy()
#         import pdb
#         pdb.set_trace()
#         out = []
        if tagsets ==None:return None
        def cfilter(tag):
            loopc = self.splitTag(tag)
            return loopc['category'] == category and loopc['value'] != ""
        
        def mapf(tag):
            loopc = self.splitTag(tag)
            return loopc['value']
        
#         import pdb
#         pdb.set_trace()
        out = filter(cfilter,tagsets)
        out = map(mapf,out)

        out.sort()
        lth = len(out)        

        if size == None:
            if start == 0:
                tags = out
            else:                                
                tags = out[start:]
        else:
            size = min(size,lth)
            tags = out[start:size]            
        #set output dic
        o = dict()
        # this is total
        o['t'] = lth
        # this is output html
        o['h'] = tags                      
        return  o
            

    def getTagHtml(self,category,start=0,size=None):
        """
                        <span data-name="1"><a href="javascript:void(0)">分析</a></span>
                        <span data-name="2"><a href="javascript:void(0)">设计</a></span>

        """
        o = self.getAllTags(category,start,size)
        tags = o['h']
        max = o['t']
        if tags == None: return "no any tag"
        out = ""
        if start == 0:       
            i = 1
        else:
            i = start + 1              
        for tag in tags:
            num = str(i)                       
            out2 = """<span data-name="%s">\
            <a class="btn btn-default" href="javascript:void(0)" role="button">%s</a>\
            </span>""" % (num,tag)
            out = "%s%s" %(out,out2)
            i = i + 1
        if size != None and max > size:
            txt = u"更多".encode('utf-8')
            more = """<span class="%s" data-name="%s" data-group="%s" data-start="%s">\
            <a class="btn btn-default" href="javascript:void(0)" role="button">%s</a>\
            </span>""" % ('more',str(i),category,str(size),txt)             
            out = "%s%s" % (out,more) 
        return out    
    
    @memoize
    def getAllTagsHtml(self):
        "output all tag groups html"
        groups = self.getTagGroups()
#         i= 0
        out = ""
        prefix = """
                    <ul class="row tagSelectSearch list-inline">                    
                    <li class="title">按%s：</li>
                    <li class="hidden">
                        <input type="hidden" value="0" class="taggroup" data-category="%s-">                            
                    </li>                    
                    <li class="all">
                        <span class="over" data-name="0"><a class="btn btn-default" href="javascript:void(0)" role="button">所有</a></span><!-- 所有 -->
                    </li>
                    <li class="tag_list_div fenlei_a">
        """
        postfix = "</li></ul>"
        for group in groups:

            if group != "":                
                prefixing = prefix % (group,group)
            else:
                fixgroup = u"未分类".encode('utf-8')
                fixprefix = """
                    <ul class="row tagSelectSearch list-inline">                    
                    <li class="title">%s：</li>
                    <li class="hidden">
                        <input type="hidden" value="0" class="taggroup" data-category="%s-">                            
                    </li>                    
                    <li class="all">
                        <span class="over" data-name="0"><a class="btn btn-default" href="javascript:void(0)" role="button">所有</a></span><!-- 所有 -->
                    </li>
                    <li class="tag_list_div fenlei_a">
        """
                prefixing = fixprefix % (fixgroup,fixgroup)
            loopitem = self.getTagHtml(group,0,5)
            loopitem = "%s%s%s" % (prefixing,loopitem,postfix)
            out = "%s%s" % (out,loopitem)
        return out                                  
        
         
#     def canbeRead(self):
# #        status = self.workflow_state()
# # checkPermission function must be use Title style permission
#         canbe = self.pm().checkPermission(viewReport,self.context)
# 
#         return canbe is not None


    
       
        
    def getPathQuery(self):
 
        """返回 all organizations
        """
        query = {}
        query['path'] = "/".join(self.context.getPhysicalPath())
        return query

         
    def search_multicondition(self,query):  
        return self.catalog()(query)

# for render userslist viewlet
# @implementer(IUsersrolesProvider)
# class  ajaxListingView(sysAjaxListingView):
#     """
#     ajax listing view for system content types
#     """
#     @memoize
#     def getTagregistryProxy(self):
#         settings = getUtility(IRegistry).forInterface(ITagSettings)
#         return settings.tags    
    

  

 # ajax load more tags       
class sysloadMore(grok.View):
    """AJAX action for loardmore.
    """    
    grok.context(Interface)
    grok.name('sysloadmore_tags')
    grok.require('zope2.View')
    
    def queryview(self):
        searchview = getMultiAdapter((self.context, self.request),name=u"sysajax_listings")
        return searchview
        
    def render(self):
        searchview = self.queryview()    
#        self.portal_state = getMultiAdapter((self.context, self.request), name=u"plone_portal_state")
                
 # datadic receive front ajax post data       
        datadic = self.request.form
        start = int(datadic['start']) # batch search start position
        group = datadic['category']  # 对应 tag category
#         import pdb
#         pdb.set_trace()
        out = searchview.getTagHtml(group,start,None)
#         getTagHtml(self,category,start=0,size=None)

        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(out)   

class loadMore(sysloadMore):
    """AJAX action for loardmore.
    """    
    grok.context(Interface)
    grok.name('loadmore_tags')
    grok.require('zope2.View')
    
    def queryview(self):
        searchview = getMultiAdapter((self.context, self.request),name=u"ajax_listings")
        return searchview

 # ajax multi-condition search       
class ajaxsearch(grok.View):
    """AJAX action for search.
    """    
    grok.context(Interface)
    grok.name('ajaxsearch')
    grok.require('zope2.View')    
#     grok.require('shuiwu.baoshui.view_projectsummary')

    def Datecondition(self,key):        
        "构造日期搜索条件"
        end = datetime.datetime.today()
#最近一周        
        if key == 1:  
            start = end - datetime.timedelta(7) 
#最近一月             
        elif key == 2:
            start = end - datetime.timedelta(30) 
#最近一年            
        elif key == 3:
            start = end - datetime.timedelta(365) 
#最近两年                                                  
        elif key == 4:
            start = end - datetime.timedelta(365*2) 
#最近五年               
        else:
            start = end - datetime.timedelta(365*5) 
#            return    { "query": [start,],"range": "min" }                                                             
        datecondition = { "query": [start, end],"range": "minmax" }
        return datecondition  
          
    def filter_category(self,value):
        if "-" not in value:return value
        return value.split('-')[1]    
    
    def render(self):    
#        self.portal_state = getMultiAdapter((self.context, self.request), name=u"plone_portal_state")
        searchview = getMultiAdapter((self.context, self.request),name=u"sysajax_listings")        
 # datadic receive front ajax post data       
        datadic = self.request.form
        start = int(datadic['start']) # batch search start position
        datekey = int(datadic['datetype'])  # 对应 最近一周，一月，一年……
        size = int(datadic['size'])      # batch search size          

        tag = datadic['tag'].strip()
        sortcolumn = datadic['sortcolumn']
        sortdirection = datadic['sortdirection']
        keyword = (datadic['searchabletext']).strip()     

        origquery = searchview.getPathQuery()
        origquery['object_provides'] = Inashuiren.__identifier__
        origquery['sort_on'] = sortcolumn  
        origquery['sort_order'] = sortdirection
                
 #模糊搜索       
        if keyword != "":
            origquery['SearchableText'] = '*'+keyword+'*'        

        if datekey != 0:
            origquery['created'] = self.Datecondition(datekey)           


        # remove repeat values 
        tag = tag.split(',')
        tag = set(tag)
        tag = list(tag)
        all = u"所有".encode("utf-8")
        unclass = u"未分类".encode("utf-8")        
# filter contain "u'所有'"
        tag = filter(lambda x: all not in x, tag)
# recover un-category tag (remove:u"未分类-")
        def recovery(value):
            if unclass not in value:return value
            return value.split('-')[1]
            
        tag = map(recovery,tag)        
        if '0' in tag and len(tag) > 1:
            tag.remove('0')
            rule = {"query":tag,"operator":"and"}
            origquery['Subject'] = rule
                      
#totalquery  search all 
        totalquery = origquery.copy()
#origquery provide  batch search        
        origquery['b_size'] = size 
        origquery['b_start'] = start
        # search all                         
        totalbrains = searchview.search_multicondition(totalquery)
        totalnum = len(totalbrains)
        # batch search         
        braindata = searchview.search_multicondition(origquery)
#        brainnum = len(braindata)         
        del origquery 
        del totalquery,totalbrains
#call output function        
        data = self.output(start,size,totalnum, braindata)
        self.request.response.setHeader('Content-Type', 'application/json')
        return json.dumps(data)       
       
    def output(self,start,size,totalnum,braindata):
        "根据参数total,braindata,返回jason 输出"
        outhtml = ""      
        k = 0
        for i in braindata:
          
            out = """<tr>
                                <td class="col-md-1 text-center">%(num)s</td>
                                <td class="col-md-3 text-left"><a href="%(objurl)s">%(title)s</a></td>
                                <td class="col-md-3">%(shibiehao)s</td>
                                <td class="col-md-4">%(description)s</td>
                                <td class="col-md-1 text-center">%(date)s</td>                                
                            </tr> """% dict(objurl="%s" % i.getURL(),
                                            num=str(k + 1),
                                            title=i.Title,
                                            shibiehao = i.id,
                                            description= i.Description,
                                            date = i.dengjiriqi)           
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1 
           
        data = {'searchresult': outhtml,'start':start,'size':size,'total':totalnum}
        return data      
