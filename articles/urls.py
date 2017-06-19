from django.conf.urls import url
from articles import views

urlpatterns = [
    url(r'^articles/titles/$', views.get_titles),
    url(r'^articles/bodys/$', views.get_bodys),
    url(r'^articles/search/(?P<title>\D+)/$', views.search),
]
