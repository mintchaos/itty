from itty import *
import os

@get('/')
def index(request):
    return 'An image: <img style="vertical-align:middle" src="/media/itty.png">'

# To serve static files, use the serve_media fuction to set your media path
# and your document root.

serve_media(path="/media", root=os.path.join(os.path.dirname(__file__), 'media'))

# Or simply setup a standard @get method. You should capture the filename/path
# and get the content-type. If your media root is different than where your
# ``itty.py`` lives, manually setup your root directory as well. Finally, use
# the ``static_file`` handler to serve up the file. (the serve_media shortcut
# does exactly this)

# @get('/media/(?P<filename>.+)')
# def my_media(request, filename):
#     my_media.content_type = content_type(filename)
#     my_root = os.path.join(os.path.dirname(__file__), 'media')
#     return static_file(request, filename=filename, root=my_root)

run_itty()
