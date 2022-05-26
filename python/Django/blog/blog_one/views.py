from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    all_blogs = Blog.objects.all()
    return render(request,'index.html', {'blogs' : all_blogs})

def fullblog(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog.html', {'blog' : blog})