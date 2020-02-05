from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('<int:pk>/profile/edit', views.EditProfile.as_view(), name='edit-profile'),
    path('<int:pk>/profile', views.DetailProfile.as_view(), name='profile'),

]
