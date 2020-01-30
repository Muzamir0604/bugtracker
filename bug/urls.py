from django.urls import path
from . import views


app_name = 'bug'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    # path('form/',views.BugFormView,name="bug-form"),
    path('form/', views.BugCreate.as_view(), name = "bug-form"),
    path('<int:pk>/detail', views.DetailBug.as_view(), name='bug-detail'),
    path('<int:pk>/delete', views.DeleteBug.as_view(), name='bug-delete'),
    path('<int:pk>/update', views.UpdateBug.as_view(), name='bug-update')
    # path('snippet/', views.snippet_detail),

]
