from .base import *

# comment it in the production servers.
try:
	from .dev import *
except:
	pass

# we will uncomment it in production server just to make sure this get activated in production.
# try:
# 	from .prod import *
# except:
# 	pass