from django.urls import path

from blog.views import home, andijon, namangan, buxoro, poytug

urlpatterns = [
    path("", home),
    path("andijon/", andijon),
    path("namangan/", namangan),
    path("buxoro/", buxoro),
    path("poytug/", poytug)
]
