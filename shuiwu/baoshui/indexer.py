from plone.indexer.decorator import indexer
# from Products.ZCatalog.interfaces import IZCatalog
from shuiwu.baoshui.content.nashuiren import Inashuiren
from shuiwu.baoshui.content.niandu import Iniandu

def encode_utf8(value):
    # be sure that it is utf-8 encoded
    if isinstance(value, unicode):
        value = value.encode('utf-8')
            # only accept strings
    assert isinstance(value, str), 'expected converted ' + \
                'value of IDexterityTextIndexFieldConverter to be a str'
    return value

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

@indexer(Inashuiren)
def nashuiren_searchable_text_indexer(obj):
    """Dynamic searchable text indexer.
    """
    title = obj.title
    shibiehao = obj.guanlidaima
    if len(shibiehao) > 3:
        shibiehao = shibiehao[3:]
    indexed = []
    indexed.append(title)
    indexed.append(shibiehao)
    return ' '.join(map(encode_utf8,indexed))
    



