from django.conf.urls import url
from application import views


urlpatterns = [
	url(r'^prescription/', views.show_prescription, name='show_prescription'),
]
