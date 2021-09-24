from django.urls import path
from blog.views import BlogPostListView,BlogPostFeaturedView,BlogPostCategoryView,BlogPostDetailView

urlpatterns = [
    path('',BlogPostListView.as_view()),
    path('<slug>',BlogPostDetailView.as_view()),
    path('category',BlogPostCategoryView.as_view()),
    path('featured',BlogPostFeaturedView.as_view()),
]
