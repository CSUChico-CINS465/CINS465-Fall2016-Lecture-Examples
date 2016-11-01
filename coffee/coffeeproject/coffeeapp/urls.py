from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'register$',views.register,name='register'),
    url(r'blogcreate$',views.create_blog_post,name='create_blog_post'),
]
