from django.urls import path
from .views import HomePage,BookDetailPage,CategoryFilter,AllCategories,AuthorFilter,AllAuthor,AllBooks,add_wishlist,remove_wishlist,add_borrowing,remove_borrowing
urlpatterns = [
    path('',HomePage,name='home'),
    path('book_detail/<slug>',BookDetailPage,name='book_detail'),
    path('all_category/',AllCategories,name="all_category"),
    path('all_author/',AllAuthor,name="all_author"),
    path('all_book/',AllBooks,name="all_book"),
    path('category/<str:category_name>',CategoryFilter,name="category"),
    path('author/<str:author_name>',AuthorFilter,name="author"),
    path('add_wishlist/<pk>',add_wishlist,name="add_wishlist"),
    path('remove_wishlist/<pk>',remove_wishlist,name="remove_wishlist"),
    path('add_borrowing/<pk>',add_borrowing,name="add_borrowing"),
    path('remove_borrowing/<pk>',remove_borrowing,name="remove_borrowing"),
]
