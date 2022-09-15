from django.urls import path
from wishlist.views import show_wishlist, show_xml, show_json, return_data_json, return_data_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', return_data_xml, name="return_data_xml"),
    path('json/<int:id>', return_data_json, name="return_data_json"),
]