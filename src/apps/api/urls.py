from django.urls import include

from .docs import urls as docs_url

urlpatterns = [include(docs_url)]
