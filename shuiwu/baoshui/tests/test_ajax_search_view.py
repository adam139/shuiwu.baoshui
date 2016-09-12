#-*- coding: UTF-8 -*-
import json
import hmac
from hashlib import sha1 as sha
from Products.CMFCore.utils import getToolByName
from shuiwu.baoshui.testing import FUNCTIONAL_TESTING 

from zope.component import getUtility
from plone.keyring.interfaces import IKeyManager
from shuiwu.baoshui.tests.test_contents import InitContents

from plone.app.testing import TEST_USER_ID, login, TEST_USER_NAME, \
    TEST_USER_PASSWORD, setRoles
from plone.testing.z2 import Browser
import unittest
from plone.namedfile.file import NamedImage
import os



class TestView(InitContents):
    
    layer = FUNCTIONAL_TESTING      
                  
        
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
                        'tag':'0',                                             
                        'sortcolumn':'created',
                        'sortdirection':'reverse',
                        'searchabletext':'',
                                                                       
                        }
# Look up and invoke the view via traversal
        view = self.portal.restrictedTraverse('@@ajaxsearch')
        result = view()


        self.assertEqual(json.loads(result)['size'],10)

              

