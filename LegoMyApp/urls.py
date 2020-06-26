from django.urls import include, path
from . import views

## URL Patterns - the first parameter is the pattern, the second is the method you're calling inside of your view
## Third is the name of the pattern/function.

urlpatterns = [
    path('', views.home, name='lego_home'),
    path('Collection/', views.index, name='list_lego_sets'),
    path('AddToCollection/', views.add_lego_set, name='add_set'),
    path('Characters/', views.index_mini, name='list_minifigs'),
    path('AddToCharacters/', views.add_minifig, name='add_minifig'),
    path('Collection/<int:pk>/Delete/', views.delete_lego_set, name='delete_lego_set'),
    path('Collection/<int:pk>/Details/', views.lego_details, name='lego_details'),
    path('Characters/<int:pk>/Delete/', views.delete_minifig, name='delete_minifig'),
    path('Characters/<int:pk>/Details/', views.minifig_details, name='minifig_details'),
    path('Collection/<int:id>/Edit/', views.lego_edit, name='lego_edit'),
    path('Delete/', views.deleted, name="deleted"),  # url for deleting data in a database#
    path('ApiService/', views.api_response, name='api_response'),
]
