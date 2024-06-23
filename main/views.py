from django.shortcuts import render

# Create your views here.
def Home(request):
    if request.method=="POST":
        notetitle=request.POST.get('NoteTitle')
        notecontent=request.POST.get("NoteContent")
    return render(request,"index.html")




def Custom404(request):
    return render(request,"404.html")


