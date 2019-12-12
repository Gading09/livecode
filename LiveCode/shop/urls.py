from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('input', views.form, name = 'form'),
    path('submit',views.submit,name ='submit'),
    path('<int:produk_id>',views.detail, name = 'detail')
]