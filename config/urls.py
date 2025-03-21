from http.cookiejar import debug

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polvon.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('baton/' , include('baton.urls')),
    path('user/', include('user.urls')),
] + debug_toolbar_urls()
