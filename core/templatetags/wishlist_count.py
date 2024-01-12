from django import template
from book.models import Wishlist
register = template.Library()
@register.filter()
def wishlist_count(user):
  if user.is_authenticated:
    wishlist_count = Wishlist.objects.filter(user=user).count()
    return wishlist_count 
  else:
    return 0