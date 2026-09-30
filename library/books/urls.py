from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path(
    "books/<int:pk>/delete/",
    views.delete_book,
    name="delete_book",
),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("add/", views.add_book, name="add_book"),
    path("add-author/", views.add_author, name="add_author"),
]
