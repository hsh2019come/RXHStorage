from django.conf.urls import url
from storage import views

urlpatterns = [
    url(r'^form/', views.form, name='form'),
    url(r'^return_detail/', views.return_detail, name='return_detail'),
]
