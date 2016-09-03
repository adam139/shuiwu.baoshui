import os
import tempfile

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig

class Base(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import shuiwu.baoshui
#        import xtshzz.policy
#        self.loadZCML(package=xtshzz.policy)
  
        xmlconfig.file('configure.zcml', shuiwu.baoshui, context=configurationContext)        
#        xmlconfig.file('configure.zcml', xtshzz.policy, context=configurationContext)
                      
    def tearDownZope(self, app):
        pass
    
    def setUpPloneSite(self, portal):
     
        applyProfile(portal, 'shuiwu.baoshui:default')
#        applyProfile(portal, 'xtshzz.policy:default')
     

TEST_FIXTURE = Base()
INTEGRATION_TESTING = IntegrationTesting(bases=(TEST_FIXTURE,), name="Base:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(bases=(TEST_FIXTURE,), name="Base:Functional")
