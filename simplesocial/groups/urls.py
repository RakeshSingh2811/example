from django.urls import path
from . import views

app_name='groups'

urlpatterns = [
    path('',views.GroupListView.as_view(),name="all"),
    path('new/',views.CreateGroup.as_view(),name="create"),
    path('posts/in/<slug>',views.GroupDetailView.as_view(),name="single")
]