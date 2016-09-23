from plone.indexer.decorator import indexer
# from Products.ZCatalog.interfaces import IZCatalog
from shuiwu.baoshui.content.nashuiren import Inashuiren

@indexer(Inashuiren)
def indexer_guanlidaima(obj, **kw):
    return obj.guanlidaima

@indexer(Inashuiren)
def indexer_dengjiriqi(obj, **kw):
    return obj.dengjiriqi