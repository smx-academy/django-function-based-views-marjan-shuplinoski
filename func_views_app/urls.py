from django.urls import path
from .views import ime_get_post, plostina_perimetar, paren_neparen

urlpatterns = [
    path("ime_get_post", ime_get_post),
    path("plostina_perimetar", plostina_perimetar),
    path("paren_neparen", paren_neparen)
]
