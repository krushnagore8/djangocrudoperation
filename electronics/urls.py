from django.urls import path
from electronics import views
urlpatterns=[
    path("",views.home,name="home "),
    path("update_data/<int:id>",views.update_data,name="update_data")
]