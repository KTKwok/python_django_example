from django.urls import path
from . import views, vw_destination, vw_category

app_name = 'tour_app'

urlpatterns = [
    path("", views.landing, name="landing"),
    path("destination/list/", vw_destination.DestinationListView.as_view(), name="destinations"),
    path('destination/create/', vw_destination.DestinationCreateView.as_view(), name='destination_create'),
    path("destination/<int:pk>", vw_destination.DestinationDetailView.as_view(), name="destination"),
    path('destination/<int:pk>/update', vw_destination.DestinationUpdateView.as_view(), name='destination_update'),
    path('destination/<int:pk>/delete/', vw_destination.DestinationDeleteView.as_view(), name='destination_delete'),
    path("category/list/", vw_category.TourCategoryListView.as_view(), name="tour_categories"),
    path('category/create/', vw_category.TourCategoryCreateView.as_view(), name='tour_category_create'),
    path("category/<int:pk>", vw_category.TourCategoryDetailView.as_view(), name="tour_category"),
    path('category/<int:pk>/update', vw_category.TourCategoryUpdateView.as_view(), name='tour_category_update'),
    path('category/<int:pk>/delete/', vw_category.TourCategoryDeleteView.as_view(), name='tour_category_delete'),

]