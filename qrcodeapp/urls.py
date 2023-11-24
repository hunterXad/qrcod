from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('all_events/', views.all_events, name='all_events'),
    path("regist/", views.regist, name="regist"),
    path("success/", views.success, name="success"),
    path('scan/', views.scan, name='scan'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
