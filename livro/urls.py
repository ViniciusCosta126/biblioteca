from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('ver-livro/<int:id>', views.ver_livros, name="ver_livros")
]
