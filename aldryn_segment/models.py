# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from aldryn_snake.template_api import registry
from django.conf import settings


# from https://segment.com/docs/libraries/analytics.js/quickstart/#step-1-copy-the-snippet
SEGMENT_SCRIPT = """<script type="text/javascript">
  !function(){var analytics=window.analytics=window.analytics||[];if(!analytics.initialize)if(analytics.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{analytics.invoked=!0;analytics.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","group","track","ready","alias","page","once","off","on"];analytics.factory=function(t){return function(){var e=Array.prototype.slice.call(arguments);e.unshift(t);analytics.push(e);return analytics}};for(var t=0;t<analytics.methods.length;t++){var e=analytics.methods[t];analytics[e]=analytics.factory(e)}analytics.load=function(t){var e=document.createElement("script");e.type="text/javascript";e.async=!0;e.src=("https:"===document.location.protocol?"https://":"http://")+"cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(e,n)};analytics.SNIPPET_VERSION="3.0.1";
  analytics.load("%(write_key)s");
  analytics.page()
  }}();
</script>"""


def get_script(request):
    write_key = getattr(settings, 'SEGMENT_WRITE_KEY', None)
    if not write_key:
        return ''
    return SEGMENT_SCRIPT % dict(write_key=write_key)

registry.add_to_tail(get_script)
