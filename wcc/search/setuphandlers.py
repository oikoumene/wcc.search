from collective.grok import gs
from wcc.search import MessageFactory as _

@gs.importstep(
    name=u'wcc.search', 
    title=_('wcc.search import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.search.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
