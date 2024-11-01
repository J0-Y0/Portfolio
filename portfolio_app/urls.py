from django.urls import path
from . import views

urlpatterns = [
    path("<str:page_name>", views.dynamic_page, name="dynamic_page"),
]
