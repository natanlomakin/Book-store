from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('login', views.MyTokenObtainPairView.as_view()),
    path('register', views.register),
    path('allthebooks', views.get_all_books),
    path('loan', views.book_loan),
    path('mybooks', views.get_my_books),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
