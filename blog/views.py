from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import ListAPIView,RetrieveAPIView
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer

#grabs all blogposts from Api
class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created') #queryset is the collection of items in this case all the items in the blogpost ordered by date created
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]

#ALLOWS to go into the blog post and view details
class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]

#filters blog posts by featured
class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]

class BlogPostCategoryView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def post(self,request, format=None):
        data = self.request.data
        category = data['category']
        queryset = BlogPost.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = BlogPostSerializer(queryset, many=True)

        return Response(serializer.data)