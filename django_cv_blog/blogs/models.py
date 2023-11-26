from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to="blogs", null=True)  # null=True değerini sil
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=False, blank=True, db_index=True, editable=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
