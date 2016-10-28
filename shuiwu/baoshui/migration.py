# -*- coding: utf-8 -*-
from plone import api
from Products.CMFCore.utils import getToolByName
from shuiwu.baoshui.content.nashuiren import Inashuiren
from shuiwu.baoshui.subscriber import subids

def AddChild(context):
    "for nashuiren create sub-child-tree"
    #search all nashuiren objects that have not sub object
    pc = getToolByName(context, "portal_catalog")
    query = {"object_provides":Inashuiren.__identifier__}
    bns = pc(query)
    bns = filter(undoFilter,bns)
    if len(bns) > 3000:
        bns = bns[:2999]    
    finishlist = map(addf,bns)

def createChildTree(context):
    "for nashuiren create sub-child-tree"
    #search all nashuiren objects that have not sub object
    pc = getToolByName(context, "portal_catalog")
    query = {"object_provides":Inashuiren.__identifier__}
    bns = pc(query)
    bns = filter(pathsearchFilter,bns)
    if len(bns) > 3000:
        bns = bns[:2999]    
    finishlist = map(mapf,bns)
        
def undoFilter(brain):
    "search the specify brain, path of the brain,if the path has sub-object,return True" 
    context = brain.getObject()
    pc = getToolByName(context, "portal_catalog")
    query = {"path":"/".join(context.getPhysicalPath()),'id':"rukupingzheng"}
    bns = pc(query)
    if len(bns) < 1:
        return True
    else:
        return False 

def addf(brain):
    "copy & paster sub tree for the brain"
    
    target = brain.getObject()
    title = u'入库凭证（按月）'.encode("utf-8")
    subid = 'rukupingzheng'
    type="shuiwu.baoshui.%s" % subid
    directory = api.content.create(type=type,id=subid,title=title,container=target)

def getTargetobj(context,objid):
    "get target nashuiren object that has been created sub tree by object id"
    pc = getToolByName(context, "portal_catalog")
    query = {"object_provides":Inashuiren.__identifier__,'id':objid}
    bns = pc(query)
    return bns[0].getObject()
        
def mapf(brain):
    "copy & paster sub tree for the brain"

    target = brain.getObject()    
    for subid,title in subids:
        title = title.encode('utf-8')
        type="shuiwu.baoshui.%s" % subid
        directory = api.content.create(type=type,id=subid,title=title,container=target)


def pathsearchFilter(brain):
    "search the specify brain, path of the brain,if the path has sub-object,return True" 
    context = brain.getObject()
    pc = getToolByName(context, "portal_catalog")
    query = {"path":"/".join(context.getPhysicalPath())}
    bns = pc(query)
    if len(bns) <= 1:
        return True
    else:
        return False       


        
        
    
    
    


