from django.shortcuts import render
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.


class CommentList(generics.ListCreateAPIView):
	queryset=Comment.objects.all()
	serializer_class=CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Comment
	serializer_class=CommentSerializer
	
def comment(request):
    if request.method == "POST":
        Comment.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            body=request.POST['body'],
        )
        return render(request, 'comment.html')
    else:
        return render(request, 'comment.html')