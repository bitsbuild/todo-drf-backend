from django.urls import path
from todorestapi.views import add_an_item,get_all_to_do_items,get_specific_to_do_item,remove_an_item,update_an_item
urlpatterns = [
    path('api/tasks/', get_all_to_do_items),
    path('api/tasks/find/<uuid:id>', get_specific_to_do_item),
    path('api/tasks/add/', add_an_item),
    path('api/tasks/update/', update_an_item),
    path('api/tasks/delete/', remove_an_item),
]

