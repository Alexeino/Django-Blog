from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)


class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostCategoryView(APIView): #To retrieve posts related to a category, ENDPOINT
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None): #When somebody will click category this api view will be called and the data will come with
        data = self.request.data    # the request, which we will use to extract posts by category, similar to POST request in a 
        category = data['category'] # form.
        queryset = BlogPost.objects.order_by('-date_created').filter(category__iexact = category)
        serializer = BlogPostSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data)
