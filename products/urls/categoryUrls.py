from django.urls import path, include
from ..views import categoryViews


urlpatterns = [
    path('', view= categoryViews.index, name= "products.index"),
    path('<int:id>/', view= categoryViews.getById),
    path('create/', view= categoryViews.create),
    path('<int:id>/update/', view= categoryViews.update),
    path('<int:id>/delete/', view= categoryViews.delete),
    path('search/', view= categoryViews.search)
]