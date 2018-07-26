from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$', login_views, name='login'),
    url(r'^register/$', register_views, name='register'),
    url(r'^page/$', page_views, name='page'),
    url(r'^history/$', history_views, name='history'),
]
