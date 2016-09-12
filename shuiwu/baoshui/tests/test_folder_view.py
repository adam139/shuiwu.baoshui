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



class TestFolderView(InitContents):
    
    layer = FUNCTIONAL_TESTING                
        
    def test_view(self):

        app = self.layer['app']
        portal = self.layer['portal']
       
        browser = Browser(app)
        browser.handleErrors = False
        browser.addHeader('Authorization', 'Basic %s:%s' % (TEST_USER_NAME, TEST_USER_PASSWORD,))

        
        import transaction
        transaction.commit()
        
        page = portal.absolute_url() + '/nashuiku1/@@sysajax_listings'

        browser.open(page)


        self.assertTrue('<table class="row table table-striped table-bordered table-condensed listing">' in browser.contents)
        
                      