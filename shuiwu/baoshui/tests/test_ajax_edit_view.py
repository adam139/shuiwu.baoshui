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

import os



class TestView(InitContents):
    
    layer = FUNCTIONAL_TESTING                        
        
    def test_edit(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'shenbaofou': 'true',
                                                                       
                        }
# Look up and invoke the view via traversal
        obj = self.portal['nashuiku1']['nashuiren1']['chengjianshui1']['yuedujilu1']

        view = obj.restrictedTraverse('@@modify_yuedujilu')
        result = view()
        self.assertEqual(obj.shenbaofou,True)

    def test_anciedit(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'shenbaocishu': '3',
                                                                       
                        }
# Look up and invoke the view via traversal
        obj = self.portal['nashuiku1']['nashuiren1']['ziyuanshui1']['ancijilu1']
 

        view = obj.restrictedTraverse('@@modify_ancijilu')
        result = view()
        self.assertEqual(obj.shenbaocishu,3)
# modify property        
    def test_propertyedit(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'shenbaofou': 'true',
                        'property':'yinhuashui'
                                                                       
                        }
# Look up and invoke the view via traversal
        obj = self.portal['nashuiku1']['nashuiren1']
 

        view = obj.restrictedTraverse('@@modify_property')
        result = view()
        self.assertEqual(obj.yinhuashui,True)        
                      
    def test_batchedit(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'action': 'selectall',
                        'objid':'chengjianshui1'
                        }
# Look up and invoke the view via traversal
        obj = self.portal['nashuiku1']['nashuiren1']
 

        view = obj.restrictedTraverse('@@batch_modify')
        result = view()
        self.assertEqual(obj['chengjianshui1']['yuedujilu1'].shenbaofou,True)
