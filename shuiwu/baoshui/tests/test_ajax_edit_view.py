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
        
    def test_anyueedit(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'shenbaofou': 'true',
                        'number':'2'                                                                       
                        }
# Look up and invoke the view via traversal
        obj = self.portal['nashuiku1']['nashuiren1']['zichanfuzaibiao']

        view = obj.restrictedTraverse('@@modify_yuedujilu')
        result = view()
        
        self.assertEqual(obj.shenbaofou2,True)

    def test_anjiedit(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'shenbaofou': 'true',
                        'number':'2'                                              
                        }
# Look up and invoke the view via traversal
        obj = self.portal['nashuiku1']['nashuiren1']['qiyesuodeshuialeiblei']

        view = obj.restrictedTraverse('@@modify_jidujilu')
        result = view()
        self.assertEqual(obj.shenbaofou2,True)
        
    def test_anciedit(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'shenbaocishu': '3',
                        'number':'2'                                              
                        }
# Look up and invoke the view via traversal
        obj = self.portal['nashuiku1']['nashuiren1']['ziyuanshui']
 

        view = obj.restrictedTraverse('@@modify_ancijilu')
        result = view()
        self.assertEqual(obj.shenbaocishu2,3)
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
                      
# modify property        
    def test_idedit(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'id':'8853427'                                                                       
                        }
# Look up and invoke the view via traversal
        obj = self.portal['nashuiku1']['nashuiren1']
        view = obj.restrictedTraverse('@@modify_id')
        result = view()
        self.assertEqual(obj.id,'8853427')

    def test_batchedit(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'action': 'selectall',
                        'objid':'xianjinliuliangbiao',
                        'number':'12'
                        }
# Look up and invoke the view via traversal
        obj = self.portal['nashuiku1']['nashuiren1']
 

        view = obj.restrictedTraverse('@@batch_modify')
        result = view()
        self.assertEqual(obj['xianjinliuliangbiao'].shenbaofou11,True)
        
    def test_desedit(self):
        request = self.layer['request']        
        keyManager = getUtility(IKeyManager)
        secret = keyManager.secret()
        auth = hmac.new(secret, TEST_USER_NAME, sha).hexdigest()
        request.form = {
                        '_authenticator': auth,
                        'description': 'special',
                        'subobj_id':'anyueqita1'
                        }
# Look up and invoke the view via traversal
        obj = self.portal['nashuiku1']['nashuiren1']
 

        view = obj.restrictedTraverse('@@modify_description')
        result = view()
        self.assertEqual(obj['anyueqita1'].description,'special')        
