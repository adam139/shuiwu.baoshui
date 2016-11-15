from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from shuiwu.baoshui import MessageFactory as _

nashuiren_status=[
('zhengchang','zheng chang',_(u'zheng chang')),
('fouzhengchang','fouzhengchang',_(u'fou zheng chang')),
('hexiaobaoyan','hexiaobaoyan',_(u'he xiao bao yan')),
('zhuxiao','zhuxiao',_(u'zhu xiao')),
  ]
nashuiren_status_terms = [
    SimpleTerm(value, token, title) for value, token, title in nashuiren_status
]
class StatusVocabulary(object):
    """ Ad Unit sizes """

    implements(IVocabularyFactory)
    def __call__(self, context):
        return SimpleVocabulary(nashuiren_status_terms)
    
StatusVocabularyFactory = StatusVocabulary()

nashuiren_type=[
('shiyedanwei','shiyedanwei',_(u'shi ye dan wei')),
('neizigeti','neizigeti',_(u'nei zi ge ti')),
('qitayouxianzeren','qitayouxianzeren',_(u'qi ta you xian ze ren gong si')),
('guoyouqiye','guoyouqiye',_(u'guo you qi ye')),
  ]
nashuiren_type_terms = [
    SimpleTerm(value, token, title) for value, token, title in nashuiren_type
]
class TypeVocabulary(object):
    """ Ad Unit sizes """

    implements(IVocabularyFactory)
    def __call__(self, context):
        return SimpleVocabulary(nashuiren_type_terms)
    
TypeVocabularyFactory = TypeVocabulary()
