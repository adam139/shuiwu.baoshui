#-*- coding: UTF-8 -*-
import json
import hmac
from hashlib import sha1 as sha
from Products.CMFCore.utils import getToolByName
from shuiwu.baoshui.testing import FUNCTIONAL_TESTING 

from zope.component import getUtility
from plone.keyring.interfaces import IKeyManager

from plone.app.testing import TEST_USER_ID, login, TEST_USER_NAME, \
    TEST_USER_PASSWORD, setRoles
from plone.testing.z2 import Browser
import unittest
from plone.namedfile.file import NamedImage
import os

def getFile(filename):
    """ return contents of the file with the given name """
    filename = os.path.join(os.path.dirname(__file__), filename)
    return open(filename, 'r')

class TestView(unittest.TestCase):
    
    layer = FUNCTIONAL_TESTING

    def setUp(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ('Manager',))

        portal.invokeFactory('shuiwu.baoshui.orgnizationfolder', 'orgnizationfolder1',
                             title="orgnizationfolder1",description="demo orgnizationfolder")     
     
        portal['orgnizationfolder1'].invokeFactory('shuiwu.baoshui.orgnization','orgnization1',
                                                   title="orgnization1",
                                                   description=u"运输业",
                                                   address=u"建设北路",
                                                   register_code="8341",
                                                   supervisor=u"交通局",
                                                   organization_type="shetuan",
                                                   announcement_type="chengli",
                                                   legal_person=u"张建明",
                                                   passDate="2013-09-16",
                                                   belondto_area='yuhuqu', 
                                                   )    
        portal['orgnizationfolder1'].invokeFactory('shuiwu.baoshui.orgnization','orgnization2',
                                                   title=u"宝庆商会2",
                                                   description=u"运输业",
                                                   address=u"建设北路",
                                                   register_code="8342",
                                                   supervisor=u"交通局",
                                                   organization_type="minfei",
                                                   announcement_type="biangeng",
                                                   legal_person=u"张建明",
                                                   passDate="2013-09-16" ,
                                                   belondto_area='yuhuqu',                                                   
                                                   ) 
        portal['orgnizationfolder1'].invokeFactory('shuiwu.baoshui.orgnization','orgnization3',
                                                   title=u"宝庆商会3",
                                                   description=u"运输业",
                                                   address=u"建设北路",
                                                   register_code="8343",
                                                   supervisor=u"交通局",
                                                   organization_type="jijinhui",
                                                   announcement_type="chexiao",
                                                   legal_person=u"张建明",
                                                   passDate="2013-09-16",
                                                   belondto_area='yuhuqu',                                                    
                                                   )                                  
        self.portal = portal
        
                  
        
    def test_ajax_search(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'start': 0,
                        'size':10 ,
                        'datetype':'1',                                                
                        'province': '1',
                        'type': '1',
                        'sortcolumn':'created',
                        'sortdirection':'reverse',
                        'searchabletext':'orgnization1',
                                                                       
                        }
# Look up and invoke the view via traversal
        view = self.portal.restrictedTraverse('@@oajaxsearch')
        result = view()


        self.assertEqual(json.loads(result)['size'],10)

    def test_yuhuquajax_search(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'start': 0,
                        'size':10 ,
                        'datetype':'1',                                                
                        'province': '1',
                        'type': '1',
                        'sortcolumn':'created',
                        'sortdirection':'reverse',
                        'searchabletext':'orgnization1',
                                                                       
                        }
# Look up and invoke the view via traversal
        view = self.portal.restrictedTraverse('@@yuhuqusearch')
        result = view()


        self.assertEqual(json.loads(result)['size'],10)               

