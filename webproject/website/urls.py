from django.urls import path,include
from . import views

urlpatterns = [
    path('hello/',views.say_hello),
    path('',views.home, name="base"),
    path('contact/',views.contact, name='contact'),
    path('pricing/',views.pricing, name='pricing'),
    path('smsapi/',views.smsapi, name='smsapi'),
    path('twoway/',views.twoway, name='twoway'),
    path("signup/",views.authView, name='authView'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signed-out/", views.SignedOutView.as_view(), name="sign-out"),
]