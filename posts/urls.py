from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/<int:page>', views.ajax, name='ajax'),
]