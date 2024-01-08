from django.urls import path
from blogapp.views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('detail/<str:pk>/', detail, name = 'detail'),
    path('delete/<str:pk>/', delete_post, name = 'delete'),
    # path('<str:pk>/likes/', like, name = 'likes'),

    path('register/', reg, name = 'register'),
    path('login/', sign_in, name = 'login'),
    path('logout/', sign_out, name = 'logout'),
]
