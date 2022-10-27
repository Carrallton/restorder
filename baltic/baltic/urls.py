from django.contrib import admin
from django.urls import path, include
#from main import models
#from api import views
from baltic import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('blog/', include('blog.urls')),
    path('api/', include('api.urls')),
#    path('/api/workers/$/', views.workers_list),
#    path('/api/workers/(?P<pk>[0-9]+)$/', views.workers_detail),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
