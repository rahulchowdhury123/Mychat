from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
  
    path('<str:room>/',views.room,name='room'),
    path('check',views.check,name='check'),
    path('data',views.data,name='data'),
    path('checkrecipent', views.checkrecipent, name='checkrecipent'),
    path('forgot',views.forgot,name='forgot'),
    path('otpp',views.otpp,name='otpp'),
    path('otp1',views.otp1,name='otp1'),
    # path('checkrecipent',views.checkrecipent,name='checkrecipent'),
    path('send',views.send,name='send'),
    
    path('getMessages/<str:room>/<str:username>/',views.getMessages,name='getMessages'),
    path('payment',views.payment,name="payment"),

    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)