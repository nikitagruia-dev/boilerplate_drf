from django.urls import path, include

from apps.common.helpers import schema_view
from apps.books import urls as book_urls

urlpatterns = [
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("books/", include(book_urls), name='books'),
]
