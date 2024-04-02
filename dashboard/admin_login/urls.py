from django.urls import path
from admin_login import views

urlpatterns = [
    path('',views.reg,name='reg'),
    path('login/',views.login_page, name='login'),
    path('index/',views.index,name='index'),
    path('show/',views.show,name='show'),
    path('logout/',views.admin_logout,name='logout')
]