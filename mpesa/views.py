from django.shortcuts import render

# Create your views here.
def homePage(request):
   return render(request,'blog.html')
def singlePage(request):
   return render(request,'blog-single.html')
def indexPage(request):
   return render(request,'index.html')