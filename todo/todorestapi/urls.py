from django.urls import path
from todorestapi.views import sample,add_an_item,get_all_to_do_items,get_specific_to_do_item,remove_an_item,update_an_item
urlpatterns = [
    path('sample',sample),
    path('add',add_an_item),
    path('update',update_an_item),
    path('show',get_all_to_do_items),
    path('find',get_specific_to_do_item),
    path('delete',remove_an_item),
]

