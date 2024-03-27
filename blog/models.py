from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email_address = models.EmailField(max_length=254, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Tag(models.Model):
    caption = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f"#{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    excerpt = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True) #I must find how to insert the date.
    slug = models.SlugField(unique=True, default="", blank=True, null=False, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"{self.title}"
    
    
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

class Comment(models.Model):
    user_name = models.CharField(max_length=120, null=True)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")



    