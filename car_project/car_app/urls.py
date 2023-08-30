from django.urls import path
from .views import OwnerListCreateView, OwnerRetrieveUpdateDestroyView, AutoListCreateView, AutoRetrieveUpdateDestroyView, AutosPassportListCreateView, AutosPassportRetrieveUpdateDestroyView

urlpatterns = [
    path('owners/', OwnerListCreateView.as_view(), name='owner-list-create'),
    path('owners/<int:pk>/', OwnerRetrieveUpdateDestroyView.as_view(), name='owner-retrieve-update-destroy'),
    path('autos/', AutoListCreateView.as_view(), name='auto-list-create'),
    path('autos/<int:pk>/', AutoRetrieveUpdateDestroyView.as_view(), name='auto-retrieve-update-destroy'),
    path('autos-passports/', AutosPassportListCreateView.as_view(), name='autos-passport-list-create'),
    path('autos-passports/<int:pk>/', AutosPassportRetrieveUpdateDestroyView.as_view(), name='autos-passport-retrieve-update-destroy'),
]