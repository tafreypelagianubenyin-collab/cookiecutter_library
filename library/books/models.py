from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    publication_year = models.IntegerField()
    available = models.BooleanField(default=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )
    cover_image = models.ImageField(
        upload_to="book_covers/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
