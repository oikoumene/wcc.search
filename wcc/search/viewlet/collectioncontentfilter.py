from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets import interfaces as manager
from wcc.search.interfaces import IProductSpecific
from Products.ATContentTypes.interfaces.topic import IATTopic
from Products.statusmessages.interfaces import IStatusMessage
from wcc.search import MessageFactory as _
grok.templatedir('templates')

class CollectionContentFilter(grok.Viewlet):
    grok.context(IATTopic)
    grok.viewletmanager(manager.IHtmlHead)
    grok.layer(IProductSpecific)

    def available(self):
        return True

    def render(self):
        searchableText = self.request.get('contentFilterSearchableText', '')
        if searchableText:
            contentFilter = dict(self.request.get('contentFilter', {}))
            contentFilter['SearchableText'] = searchableText
            self.request.set('contentFilter', contentFilter)
            IStatusMessage(self.request).add(_(
                u'search_results_notification',
                default=u'Displaying search results for "${searchableText}"',
                mapping={'searchableText': searchableText}
            ))
        return ''
