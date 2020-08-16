from django.urls import path, include
from .views import searchSchemePage, searchResultsView, appliedSchemes

urlpatterns = [    
    path('schemes/', searchSchemePage, name='schemes'),
    path('schemes/search/', searchResultsView, name='schemes'),
    path('applied-schemes/', appliedSchemes, name='applied-schemes'),
]