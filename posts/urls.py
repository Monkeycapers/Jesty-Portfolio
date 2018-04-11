from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/<int:page>', views.ajax, name='ajax'),
    path('<int:pid>', views.getPost, name='getPost'),
    path('<int:pid>/<slug:slug>', views.getPost, name='getPost'),
    path('tags/<str:tag>', views.postsByTag, name='postsByTag'),
    path('search', views.search, name='search'),
    path('search/<str:type>', views.search, name='search'),
    path('search/<str:type>/<str:searchtext>', views.search, name='search'),
    
]