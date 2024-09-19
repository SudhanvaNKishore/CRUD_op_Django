from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('generate_pdf/', views.generate_pdf_view, name='generate_pdf'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
]