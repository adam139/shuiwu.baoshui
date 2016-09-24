#-*- coding: UTF-8 -*-
"""refer  the plone.app.discussion catalog indexes
"""
import unittest

import transaction
from zope import event

from datetime import datetime

from zope.component import createObject
from zope.annotation.interfaces import IAnnotations

from Products.CMFCore.utils import getToolByName

from plone.app.testing import TEST_USER_ID, setRoles

from shuiwu.baoshui.testing import INTEGRATION_TESTING

from shuiwu.baoshui import indexer as catalog
from plone.indexer.delegate import DelegatingIndexerFactory
from shuiwu.baoshui.tests.test_contents import InitContents

class CatalogSetupTest(InitContents):

    layer = INTEGRATION_TESTING

         
    
    def test_catalog_installed(self):
        self.assertTrue('guanlidaima' in self.portal.portal_catalog.indexes())
        self.assertTrue('dengjiriqi' in self.portal.portal_catalog.indexes())        
        


    def test_indexer(self):
        self.assertTrue(isinstance(catalog.indexer_guanlidaima,
                                DelegatingIndexerFactory))
        
        p1 = self.portal['nashuiku1']['nashuiren1']
        self.assertEqual(catalog.indexer_guanlidaima(p1)(), "888201")
        self.assertEqual(catalog.indexer_dengjiriqi(p1)(), "2015-12-21")

                  

#     def test_catalogsearch(self):   
#         catalog2 = getToolByName(self.portal, 'portal_catalog')     
# 
#         results2 = list(catalog2({'guanlidaima': "888201"}))
# 
#         self.assertEqual(len(results2), 2)

                 

