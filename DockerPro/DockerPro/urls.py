from django.contrib import admin
from django.urls import path
from studentapp.views import studentFormView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myform/', studentFormView,name='myform'),
]
