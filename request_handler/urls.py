from django.urls import path

from .views import *

urlpatterns = [
    path('method_a/', Method_A),
    path('method_b/<str:code>/<str:date_1>/<str:date_2>/', Method_B),
]
