from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.mainV,name='main'),
    path('', views.indexV,name='index'),
    path('login/', views.logingV,name='login'),
    path('logout/', views.loguotV,name='logout'),
    path('Dashboard/', views.DashboardV,name='Dashboard'),
    path('create/user/', views.createuserV,name='createuser'),

























]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
