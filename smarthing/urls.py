from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^smarthing/$', views.HomeView.as_view(), name="home"),
    url(r'^smarthing/productos/$', views.PrinView.as_view(), name="pro"),
    url(r'^smarthing/productos/(?P<slug>[-\w]+)/$', views.ProView.as_view(), name="detalle"),
]
