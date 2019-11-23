"""
WSGI config for yueeeeeeee project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# start adding settings
import sys                                                                                                                                                    
from os.path import dirname, abspath                                                                                                                    
from django.core.wsgi import get_wsgi_application                                                                                                             
PROJECT_DIR = dirname(dirname(abspath(__file__)))                                                                                                             
sys.path.insert(0, PROJECT_DIR)                                                                                                                               
                                                                                                                                                              
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yueeeeeeee.settings')                                                                                   
os.environ["DJANGO_SETTINGS_MODULE"] = "yueeeeeeee.settings"                                                                                               
# end

application = get_wsgi_application()
