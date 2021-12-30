from django.urls import path
from . import views

urlpatterns = [
    path("list", views.quote_list),
    path("<int:id>", views.get_quote),
    path("random", views.random_quote),
    path("add-quote", views.add_quote),
    path("delete/<int:id>", views.delete_quote),
]