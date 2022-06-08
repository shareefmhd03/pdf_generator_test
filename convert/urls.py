from django.urls import path
from . views import pdf_builder

urlpatterns = [

    path('download',pdf_builder),
]