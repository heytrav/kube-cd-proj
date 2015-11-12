from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^ingredients/$', views.IngredientsView.as_view(), name='ingredients'),
    url(r'^ingredient/create$', views.IngredientCreate.as_view(),
        name='create_ingredient'),
    url(r'^ingredient/(?P<pk>[0-9]+)/edit$', views.IngredientUpdate.as_view(),
        name='edit_ingredient'),
    url(r'^ingredient/(?P<pk>[0-9]+)/delete$', views.IngredientDelete.as_view(),
        name='delete_ingredient'),
]
