from django.urls import path

from base import views


urlpatterns = [
  path('jobform/',views.BasicDetailView.as_view(),name="createform"),
  path('jobform/<int:pk>',views.BasicDetailView.as_view(),name="editform"),
  path('viewForm/<int:pk>',views.DataView.as_view(),name="dataview"),
  path('getState/',views.getState.as_view(),name="getState"),
  path('getCity/<str:pk>',views.getCity.as_view(),name="getCity"),
  path('getData/<str:pk>',views.GETDATA.as_view(),name="getData"),




]