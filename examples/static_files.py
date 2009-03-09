from itty import *
import os

# By default, by calling serve_media() itty will serve static media out of the
# ``media`` folder for all requests coming from ``/media``.

# So in your browser, you should be able to hit ``/media/default.css`` or
# ``/media/itty.png``.

# Both the path and the root can be overridden as arguments to serve_media
# serve_media(path="/public", root="/my/file/path/on/disk")

serve_media()

@get('/')
def index(request):
    return 'An image: <img style="vertical-align:middle" src="/media/itty.png">'

run_itty()
