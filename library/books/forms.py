from django import forms

from .models import Author
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
    widgets = {
        "title": forms.TextInput(
            attrs={
                "class": (
                    "w-full px-4 py-3 border border-gray-300 "
                    "rounded-lg focus:outline-none focus:ring-2 "
                    "focus:ring-blue-500"
                ),
                "placeholder": "Enter book title",
            },
        ),
        "summary": forms.Textarea(
            attrs={
                "class": (
                    "w-full px-4 py-3 border border-gray-300 "
                    "rounded-lg focus:outline-none focus:ring-2 "
                    "focus:ring-blue-500"
                ),
                "placeholder": "Enter book summary",
                "rows": 5,
            },
        ),
        "publication_year": forms.NumberInput(
            attrs={
                "class": (
                    "w-full px-4 py-3 border border-gray-300 "
                    "rounded-lg focus:outline-none focus:ring-2 "
                    "focus:ring-blue-500"
                ),
                "placeholder": "Enter publication year",
            },
        ),
        "available": forms.CheckboxInput(
            attrs={
                "class": "h-4 w-4 text-blue-600 rounded focus:ring-blue-500",
            },
        ),
        "author": forms.Select(
            attrs={
                "class": (
                    "w-full px-4 py-3 border border-gray-300 "
                    "rounded-lg bg-white focus:outline-none "
                    "focus:ring-2 focus:ring-blue-500"
                ),
            },
        ),
        "cover_image": forms.ClearableFileInput(
            attrs={
                "class": (
                    "w-full px-4 py-3 border border-gray-300 "
                    "rounded-lg bg-white focus:outline-none "
                    "focus:ring-2 focus:ring-blue-500"
                ),
            },
        ),
    }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "first_name",
            "name",
            "nationality",
            "birth_date",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": (
                        "w-full px-4 py-3 border border-gray-300 "
                        "rounded-lg focus:outline-none focus:ring-2 "
                        "focus:ring-blue-500"
                    ),
                    "placeholder": "Enter author's first name",
                },
            ),
            "name": forms.TextInput(
                attrs={
                    "class": (
                        "w-full px-4 py-3 border border-gray-300 "
                        "rounded-lg focus:outline-none focus:ring-2 "
                        "focus:ring-blue-500"
                    ),
                    "placeholder": "Enter author's name",
                },
            ),
            "nationality": forms.TextInput(
                attrs={
                    "class": (
                        "w-full px-4 py-3 border border-gray-300 "
                        "rounded-lg focus:outline-none focus:ring-2 "
                        "focus:ring-blue-500"
                    ),
                    "placeholder": "Enter author's nationality",
                },
            ),
            "birth_date": forms.DateInput(
                attrs={
                    "class": (
                        "w-full px-4 py-3 border border-gray-300 "
                        "rounded-lg focus:outline-none focus:ring-2 "
                        "focus:ring-blue-500"
                    ),
                    "type": "date",
                },
            ),
        }
