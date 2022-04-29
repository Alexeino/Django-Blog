from django.urls import path
from .views import *

urlpatterns = [
    path('',BlogPostListView.as_view(),name="all_blogs"),
    path('<slug>',BlogPostDetailView.as_view(),name="blog_detail"),
    path('featured/',BlogPostFeaturedView.as_view()),
    path('category/',BlogPostCategoryView.as_view(),name="category_blogs"),
]
