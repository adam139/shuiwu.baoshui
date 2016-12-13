#-*- coding: UTF-8 -*-
from five import grok
import json
from z3c.form import field
from zope.interface import Interface
from Acquisition import aq_inner
from plone.directives import dexterity
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from Products.Five.browser import BrowserView
from datetime import datetime

# from shuiwu.baoshui.content.jidujilu import Ijidujilu
# from shuiwu.baoshui.content.ancijilu import Iancijilu
# from shuiwu.baoshui.content.yuedujilu import Iyuedujilu
from shuiwu.baoshui.content.nashuiren import Inashuiren
from shuiwu.baoshui.content.niandu import Iniandu
from shuiwu.baoshui import _


class ArchivedView(BrowserView):
    "archived nashuiren  view"
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
            
    @property
    def isEditable(self):
        return self.pm().checkPermission(permissions.ManagePortal,self.context)
    
    def getPathQuery(self): 
        "获取查询路径"
        query = {}
        path = "/".join(self.context.getPhysicalPath())
        query['path'] = path
        return query    
    
    def getAllArchived(self):
        "get all archived nashuiren shenbao ziliao"
        query = self.getPathQuery()
        query['object_provides'] = Iniandu.__identifier__
        brains = self.catalog()(query)
        outhtml = ""
        k = 0
        for i in brains:
            out = """<tr><td class="col-md-1 text-center">%(num)s</td>
                         <td class="col-md-3 text-left"><a href="%(objurl)s">%(Id)s</a></td>
                         <td class="col-md-3">%(date)s</td></tr>""" % dict(
                                            objurl="%s/@@nashuiren_view" % i.getURL(),
                                            num=str(k + 1),
                                            Id=i.id,                                            
                                            date = i.dengjiriqi)           
            outhtml = "%s%s" %(outhtml ,out)
            k = k + 1
            
        return outhtml                    
        


        
    def currentYear(self):
        return datetime.now().strftime('%Y')
                 
  
     

    