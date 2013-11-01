# -*- coding: iso-8859-1 -*-
# IMPORTANT! This encoding (charset) setting MUST be correct! If you live in a
# western country and you don't know that you use utf-8, you probably want to
# use iso-8859-1 (or some other iso charset). If you use utf-8 (a Unicode
# encoding) you MUST use: coding: utf-8
# That setting must match the encoding your editor uses when you modify the
# settings below. If it does not, special non-ASCII chars will be wrong.

"""
This is a sample config for a wiki that is part of a wiki farm and uses
farmconfig for common stuff. Here we define what has to be different from
the farm's common settings.
"""

# we import the FarmConfig class for common defaults of our wikis:
from farmconfig import FarmConfig

from MoinMoin.auth import MoinAuth
from MoinMoin.auth.openidrp import OpenIDAuth



# now we subclass that config (inherit from it) and change what's different:
class Config(FarmConfig):
    logo_string = u'<img src="/images/noctis-logo-100.png" alt="Noctis logo">'
    #logo_string = u'<a href="http://www.homeworld2complex.com/index1.htm"><img src="http://www.homeworld2complex.com/images/H2C700x525.jpg" width="350" height="263" alt="April Fools!"></a>'

    # basic options (you normally need to change these)
    sitename = u'AlopexWiki' # [Unicode]
    interwikiname = u'AlopexWiki' # [Unicode]

    # name of entry page / front page [Unicode], choose one of those:

    # a) if most wiki content is in a single language
    #page_front_page = u"MyStartingPage"

    # b) if wiki content is maintained in many languages
    page_front_page = u"FrontPage"

    data_dir = '/srv/www/alopex.li/moindata/'
    data_underlay_dir = '/usr/share/moin/underlay/'
    #acl_rights_default = u'Known:read TrustedEditorGroup:read,write,delete,revert All:read AdminGroup:read,write,delete,revert,admin'
    acl_rights_default = u'AdminGroup:read,write,delete,revert,admin TrustedEditorGroup:read,write,delete,revert Known:read All:read'
 
    #auth = [MoinAuth()]
    auth = [MoinAuth(), OpenIDAuth()]
    # Must be >0 for openid
    cookie_lifetime = (1,12)

    # Fast search
    xapian_search = True

    # Favicon
    html_head = '''<link rel="shortcut icon" href="/noctis-favicon.ico"> '''

    # Textchas
    #textchas_disabled_group = u"TrustedEditorGroup"
    #textchas = {
    #   'en': {
          #u"What is the answer to life, the universe, and everything?" : ur"42"
	#u"What is the next color in the sequence?  Red, orange, yellow, green..." : ur"blue"
#	u"Only authorized users can post to this wiki.  Ask Simon or David to authorize you.  Spammers can FOAD." : ur"c021983ea291ea3f8cd663d7b902a8130ec12649125cb29e054b8"
#        }
#    }
    
