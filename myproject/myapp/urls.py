from django.conf.urls import url, include
#from django.urls import path, include
from myapp import views 
urlpatterns = [ 
     url(r'^$', views.HomePageView.as_view()),
     url('login/', views.login.as_view(),name='log_in'), 
     url('registration/', views.reg.as_view(),name='reg'), 
 ] 
