from .base import *

# you need to comment this block in production server.
try:
	from .dev import *
except:
	pass

# you need to uncommment this block in production server.
# try:
# 	from .prod import *
# except:
# 	pass

