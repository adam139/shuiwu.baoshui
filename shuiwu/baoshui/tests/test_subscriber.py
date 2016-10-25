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



class TestView(unittest.TestCase):
    
    layer = FUNCTIONAL_TESTING

    def setUp(self):
        portal = self.layer['portal']
        setRoles(portal, TEST_USER_ID, ('Manager',))

        portal.invokeFactory('shuiwu.baoshui.nashuiku', 'nashuiku1',
                             title="nashuiku1",description="demo nashuiku ")     
     
        portal['nashuiku1'].invokeFactory('shuiwu.baoshui.nashuiren','nashuiren1',
                                                   title="orgnization1",
                                                   description=u"运输业",

                                                   )    

                                 
        self.portal = portal
        
                  
    def test_folder_types(self):
        self.assertEqual(self.portal['nashuiku1']['nashuiren1'].id,'nashuiren1')
        self.assertEqual(self.portal['nashuiku1']['nashuiren1']['gonghuijingfei'].id,'gonghuijingfei')        

          

