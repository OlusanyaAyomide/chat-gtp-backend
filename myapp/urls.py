from django.urls import path
from . import views

urlpatterns=[
    path("",views.searchInfo.as_view(),name="first"),
    path("search",views.ImageSearch.as_view(),name="img-search"),
    path("nav",views.NavBarList.as_view(),name="navbar")
    
]