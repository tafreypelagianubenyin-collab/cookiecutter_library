from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "summary",
            "publication_year",
            "available",
            "author",
            "cover_image",
        ]
