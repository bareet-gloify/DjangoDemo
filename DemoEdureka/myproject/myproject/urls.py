from django.conf.urls import url
from django.contrib import admin
from webapp import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url('employees/', views.employeeList.as_view()),
]
