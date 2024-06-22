from django.shortcuts import render

# Create your views here.
def Home(request):
    if request.method=="POST":
        pass
    return render(request,"index.html")




def Custom404(request):
    return render(request,"404.html")


