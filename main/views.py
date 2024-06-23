from django.shortcuts import render
from main.SlugGenerator import slug_generator,fileid

# Create your views here.
def Home(request):
    if request.method=="POST":
        notetitle=request.POST.get('NoteTitle').strip()
        notecontent=request.POST.get("NoteContent").strip()
        if notetitle and notecontent:
            print(notetitle,notecontent)
            slug=slug_generator(notetitle)
            textid=fileid()
            try:
                successdata={
                    'status':'success',
                    'slug':'http://127.0.0.1:8000/d/'+slug,
                    'fileid':textid
                }
                return render(request,"index.html",successdata)
            except Exception as ex:
                print(ex)
                successdata={
                    'status':'error',
                    'message':'Something went wrong.'
                }
                return render(request,'index.html',successdata)
        else:
            successdata={
                'status':'error',
                'message':'All Fields are Required.'
            }
            return render(request,'index.html',successdata)
    return render(request,"index.html")




def Custom404(request):
    return render(request,"404.html")


