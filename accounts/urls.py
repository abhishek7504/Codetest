from django.urls import path,include
from . import views

urlpatterns = [
    path('user/',views.UserList.as_view()),
    path('spam/',views.MarkAsSpam.as_view()),
    path('search/',views.Search.as_view()),
    path('login/',views.Login.as_view()),
]