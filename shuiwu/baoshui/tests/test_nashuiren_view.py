#-*- coding: UTF-8 -*-
from Products.CMFCore.utils import getToolByName
from shuiwu.baoshui.testing import FUNCTIONAL_TESTING 

from plone.app.testing import TEST_USER_ID, login, TEST_USER_NAME, \
    TEST_USER_PASSWORD, setRoles
from plone.testing.z2 import Browser
from shuiwu.baoshui.tests.test_contents import InitContents
import unittest

import os
import datetime


class TestNashuirenView(InitContents):
    
    layer = FUNCTIONAL_TESTING    

        
    def test_view(self):

        app = self.layer['app']
        portal = self.layer['portal']
       
        browser = Browser(app)
        browser.handleErrors = False
        browser.addHeader('Authorization', 'Basic %s:%s' % (TEST_USER_NAME, TEST_USER_PASSWORD,))
        
        import transaction
        transaction.commit()
        obj = portal.absolute_url() + '/nashuiku1/nashuiren1'        
        page = obj + '/@@nashuiren_view'
        browser.open(page)
#        open('/tmp/test.html', 'w').write(browser.contents)


        outstr = '<span>888202</span>'        
        self.assertTrue(outstr in browser.contents)

        outstr = 'data-property="yinhuashui"'
        self.assertTrue(outstr in browser.contents)
        outstr = '<td class="col-md-1 text-center">0</td>'
        self.assertTrue(outstr in browser.contents)        
        
