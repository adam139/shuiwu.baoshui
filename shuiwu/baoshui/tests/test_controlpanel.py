import unittest
from plone.testing.z2 import Browser
from plone.app.testing import SITE_OWNER_NAME, SITE_OWNER_PASSWORD
from shuiwu.baoshui.testing import FUNCTIONAL_TESTING

class TestControlPanel(unittest.TestCase):

    layer = FUNCTIONAL_TESTING

    def test_configlet(self):
        
        app = self.layer['app']
        portal = self.layer['portal']
        
        browser = Browser(app)
        browser.handleErrors = False
        
        # Simulate HTTP Basic authentication
        browser.addHeader('Authorization',
                'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,)
            )
        
        # Open Plone's site setup
        browser.open("%s/plone_control_panel" % portal.absolute_url())
        
        self.assertTrue('DataInOut' in browser.contents)
  
    def test_inoutview(self):

        app = self.layer['app']
        portal = self.layer['portal']
       
        browser = Browser(app)
        browser.handleErrors = False
        browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,))

        
        import transaction
        transaction.commit()
        
        page = portal.absolute_url() + '/@@datainout-controlpanel'

        browser.open(page)
        self.assertTrue('<input type="file" name="csv_upload" />' in browser.contents)
