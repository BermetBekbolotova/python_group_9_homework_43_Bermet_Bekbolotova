from django.urls import path

from webapp.views import index_view, make_calculation_view

urlpatterns = [
    path('', index_view),
    path('calculation/make/', make_calculation_view)
    ]