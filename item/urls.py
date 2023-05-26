from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="item-index"),
    path('<int:id>', views.get_item_by_id, name='item-details'),
    path('create-item', views.create_item, name='create-item'),
    path('delete-item/<int:id>', views.delete_item, name='delete-item'),
    path('update-item/<int:id>', views.update_item, name='update-item'),
    path('see-offers/<int:id>', views.see_offers, name='see-offers')
]
