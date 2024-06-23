from django.shortcuts import render

# Create your views here.
def Home(request):
    if request.method=="POST":
        notetitle=request.POST.get('NoteTitle').strip()
        notecontent=request.POST.get("NoteContent").strip()
        if notetitle and notecontent:
            print(notetitle,notecontent)
            statusdata={
                'status':'success',
                'slug':'http://127.0.0.1:8000/d/'+slug,
                'fileid':fileno
            }


        else:
            successdata={
                'status':'error',
                'message':'All Fields are Required.'
            }
            return render(request,'index.html',successdata)
    return render(request,"index.html")




def Custom404(request):
    return render(request,"404.html")


