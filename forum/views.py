from django.shortcuts import render

# Create your views here.
def forum(request):
    return render(request,'forum/forum.html')