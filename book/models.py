from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField



availability_status=(
    ('available', 'available'),
    ('not available', 'not available'),
    ('coming soon', 'coming soon'),
)

class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='author',default='default.png')
    occupation = models.CharField(max_length=255)
    bio = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category',default='default.png')
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='book',default='default.png',null=True, blank=True)
    author = models.ForeignKey(Author, null=True, blank=True,on_delete=models.CASCADE,related_name='author')
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    availability_status = models.CharField(max_length=200,choices=availability_status, null=True, blank=True) 
    num_of_books_available = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,related_name='category', null=True, blank=True,on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title',null=True, blank=True)
    description =RichTextField(null=True, blank=True)


    def __str__(self):
        return self.title


class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    book = models.ForeignKey(Book, on_delete= models.CASCADE)
    def __str__(self):
        return f'{self.user.username} - {self.book.title}'
    
    class Meta:
        unique_together = ['user', 'book']


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    book = models.ForeignKey(Book, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f'{self.user.username} - {self.book.title}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    book = models.ForeignKey(Book, on_delete= models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'
    
