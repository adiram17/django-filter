import django_filters
from django import forms


class BookFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains', widget = forms.TextInput(attrs={'class': 'form-control '}))
    author = django_filters.CharFilter(lookup_expr='icontains', widget = forms.TextInput(attrs={'class': 'form-control '}))
    