from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Book


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'library/home.html', context)


class BookListView(ListView):
    model = Book
    template_name = 'library/home.html'
    context_object_name = 'books'
    ordering = ['-date_posted']
    paginate_by = 5


class BookDetailView(DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'comment', 'book_author', 'posted_by', 'private']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'comment', 'book_author', 'private']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.author:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.author:
            return True
        return False


class UserBookListView(ListView):
    model = Book
    template_name = 'library/user_books.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Book.objects.filter(book_author=user).order_by('-date_posted')


def about(request):
    return render(request, 'library/about.html', {'title': 'О библиотеке Horwing Logistics'})