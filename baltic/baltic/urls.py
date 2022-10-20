from django.contrib import admin
from django.urls import path
from main import models
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/api/workers/$', views.workers_list),
    path('/api/workers/(?P<pk>[0-9]+)$', views.workers_detail),
]
