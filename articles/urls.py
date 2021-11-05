#from django.urls import path, re_path
from django.conf.urls import url

from .import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),
    # path('', views.article_list),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name="detail"),
]

