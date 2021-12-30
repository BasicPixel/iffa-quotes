from django.urls import path
from . import views

urlpatterns = [
    path("", views.available_routes),
    path("list", views.quote_list),
    path("pending", views.pending_quotes),
    path("<int:id>", views.get_quote),
    path("random", views.random_quote),
    path("add-quote", views.add_quote),
    path("delete/<int:id>", views.delete_quote),
]