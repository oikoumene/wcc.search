from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets import interfaces as manager
from wcc.search.interfaces import IProductSpecific
from Products.ATContentTypes.interfaces.topic import IATTopic
grok.templatedir('templates')

class CollectionContentFilter(grok.Viewlet):
    grok.context(IATTopic)
    grok.viewletmanager(manager.IHtmlHead)
    grok.layer(IProductSpecific)

    def available(self):
        return True

    def render(self):
        if self.request.get('contentFilterSearchableText', ''):
            contentFilter = dict(self.request.get('contentFilter', {}))
            contentFilter['SearchableText'] = self.request.get(
                    'contentFilterSearchableText', '')
            self.request.set('contentFilter', contentFilter)
        return ''
