from django.urls import path

from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.OfferCreate.as_view(), name='create'),
    path('<int:id>/update/', views.OfferUpdate.as_view(), name='updateOffer'),
    path('<int:id>/delete', views.OfferDelete.as_view(), name='deleteOffer'),
    path('<int:id>/sendComment/', views.sendComment, name='sendComment'),
    path('<int:id>/sendEmail/', views.sendEmail, name='sendEmail'),
]