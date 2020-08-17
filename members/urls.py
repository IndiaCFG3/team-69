from django.urls import path
from .views import verify_documents

urlpatterns = [    
    path('document/verification/<int:id>/', verify_documents, name='doc-verify'),
]