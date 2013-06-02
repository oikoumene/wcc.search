from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.search import MessageFactory as _

class IContentFilterPortlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    portlet_title = schema.TextLine(title=_(u'Title'))

    placeholder_text = schema.TextLine(
        title=_('Placeholder text'),
        required=False,
        default=u'Search'
    )

class Assignment(base.Assignment):
    implements(IContentFilterPortlet)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return self.portlet_title

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/contentfilterportlet.pt')

    @property
    def available(self):
        return True

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentFilterPortlet)
    label = _(u"Add Content Filter Portlet")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentFilterPortlet)
    label = _(u"Edit Content Filter Portlet")
    description = _(u"")
