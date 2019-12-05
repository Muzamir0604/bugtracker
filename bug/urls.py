from django.urls import path
from . import views


app_name = 'bug'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('form/',views.BugFormView,name="bug-form"),
    path('detail/<int:id>/', views.bug_detail_view, name='bug-detail')
    # path('snippet/', views.snippet_detail),

]
