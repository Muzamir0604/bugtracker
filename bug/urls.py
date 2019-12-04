from django.urls import path
from . import views


app_name = 'bug'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('form/',views.BugFormView,name="bug-form"),
    # path('snippet/', views.snippet_detail),

]
