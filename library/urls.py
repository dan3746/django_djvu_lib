from django.urls import path

from library import views
from library.views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, UserBookListView

urlpatterns = [
    path('library', BookListView.as_view(), name='library-home'),
    path('library/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('library/new/', BookCreateView.as_view(), name='book-create'),
    path('library/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('library/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('user/<str:username>/books', UserBookListView.as_view(), name='user-books'),
    path('about/', views.about, name='library-about'),
]
