from django.urls import path, include
from .views import searchSchemePage, searchResultsView

urlpatterns = [    
    path('schemes/', searchSchemePage, name='schemes'),
    path('schemes/search', searchResultsView, name='schemes'),
]