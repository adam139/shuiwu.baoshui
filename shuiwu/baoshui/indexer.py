from plone.indexer.decorator import indexer
# from Products.ZCatalog.interfaces import IZCatalog
from shuiwu.baoshui.content.nashuiren import Inashuiren
from shuiwu.baoshui.content.niandu import Iniandu

@indexer(Inashuiren)
def indexer_guanlidaima(obj, **kw):
    return obj.guanlidaima

@indexer(Inashuiren)
def indexer_dengjiriqi(obj, **kw):
    return obj.dengjiriqi.strftime("%Y-%m-%d")

@indexer(Inashuiren)
def indexer_status(obj, **kw):
    return obj.status

@indexer(Inashuiren)
def indexer_regtype(obj, **kw):
    return obj.regtype
@indexer(Inashuiren)
def indexer_danganbianhao(obj, **kw):
    return obj.danganbianhao

@indexer(Inashuiren)
def indexer_shuiguanyuan(obj, **kw):
    return obj.shuiguanyuan

@indexer(Inashuiren)
def indexer_caiwufuzeren(obj, **kw):
    return obj.caiwufuzeren
@indexer(Inashuiren)
def indexer_caiwufuzerendianhua(obj, **kw):
    return obj.caiwufuzerendianhua
@indexer(Inashuiren)
def indexer_banshuiren(obj, **kw):
    return obj.banshuiren
@indexer(Inashuiren)
def indexer_banshuirendianhua(obj, **kw):
    return obj.banshuirendianhua
@indexer(Iniandu)
def indexer_guidangzhuangtai(obj, **kw):
    return obj.guidangzhuangtai
