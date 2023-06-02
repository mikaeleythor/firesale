from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/person
    path('', views.index, name="person-index"),
    path('update', views.update_person, name='update-person'),
    path('create-person', views.create_person, name='create-person'),
    path('<int:id>', views.get_profile_by_id, name='profile-details'),
]
