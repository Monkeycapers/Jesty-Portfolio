from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/<int:page>', views.ajax, name='ajax'),
    path('ajax-toggle-night', views.togglenight, name='togglenight'),
    path('ajax-comment/<int:pid>', views.comment, name='comment'),
    path('<int:pid>', views.getPost, name='getPost'),
    path('<int:pid>/<slug:slug>', views.getPost, name='getPost'),
    path('tags/<str:tag>', views.postsByTag, name='postsByTag'),
    path('search', views.search, name='search'),
    path('search/<str:type>', views.search, name='search'),
    path('search/<str:type>/<str:searchtext>', views.search, name='search'),
    path('resume', views.showResume, name='showResume'),
    path('drawit', views.drawit, name='drawit'),
    path('projects', views.projects, name='projects')
]