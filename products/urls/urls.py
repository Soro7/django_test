from django.urls import path, include
from ..views import categoryViews, views

urlpatterns = [
    path('', view= views.index),
    path('search/', view= views.search),
    path('create/', view= views.create),
    path('temp/', view= views.temp)
]
