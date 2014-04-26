import os

SETTINGS = 'dev'

if 'SERVER_SOFTWARE' in os.environ:
    SETTINGS = 'production'
exec 'from %s import *' % SETTINGS

if not 'SERVER_SOFTWARE' in os.environ:
    from local import *

#try:
#    from pre import SETTINGS
#except:
#    pass
#exec 'from %s import *' % SETTINGS
#
#try:
#    from local import *
#except ImportError:
#    pass
