from django.contrib import admin
from .models import Book,Author,Category,Borrowing,Wishlist,Review
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Borrowing)
admin.site.register(Wishlist)
admin.site.register(Review)