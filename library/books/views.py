from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import AuthorForm
from .forms import BookForm
from .models import Book


def home(request):
    return render(request, "books/home.html")


def book_list(request):
    search_query = request.GET.get("search", "").strip()

    if search_query:
        books = Book.objects.select_related("author").filter(
            title__icontains=search_query,
        )
    else:
        books = Book.objects.select_related("author").all()

    return render(
    request,
    "books/book_list.html",
    {
        "books": books,
        "search_query": search_query,
    },
)
def book_detail(request, pk):
    book = get_object_or_404(
        Book.objects.select_related("author"),
        pk=pk,
    )
    return render(
request,
"books/book_detail.html",
{"book": book},
)


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("books:book_list")

        return render(
        request,
        "books/add_book.html",
        {"form": form},
    )

    form = BookForm()

    return render(
        request,
        "books/add_book.html",
        {"form": form},
    )
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            return redirect("books:book_detail", pk=book.pk)

        return render(
        request,
        "books/edit_book.html",
        {"form": form, "book": book},
    )

    form = BookForm(instance=book)

    return render(
        request,
        "books/edit_book.html",
        {"form": form, "book": book},
    )
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("books:book_list")

    return render(
    request,
    "books/delete_book.html",
    {"book": book},
)
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("books:add_book")

        return render(
        request,
        "books/add_author.html",
        {"form": form},
    )

    form = AuthorForm()

    return render(
        request,
        "books/add_author.html",
        {"form": form},
    )

