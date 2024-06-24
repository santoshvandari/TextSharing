from django.shortcuts import render,redirect
from main.SlugGenerator import slug_generator,fileid
from main.RemovingText import RemoveAllExpiredFiles
from main.models import SharedText

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
                SharedText.objects.create(title=notetitle,note=notecontent,slug=slug,fileid=textid)
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

def Download(request):
    if request.method=="POST":
        fileid = (request.POST.get("fileid")).strip()
        if not fileid:
            print("file id: "+fileid)
            return render(request,'download.html',{"error" : "Text ID Cannot Be Empty"})
        if fileid:
            try:
                text=SharedText.objects.filter(fileid=fileid).first()
            except Exception as ex:
                print(ex)
                return redirect("/404")
            if not text:
                return redirect("/404")
            elif text.is_expired():
                # remove from teh datbase and the file from the server
                if(RemoveAllExpiredFiles()):
                    return redirect("/404")
                return redirect("/404")
            else:
                return render(request,"download.html",{"text":text})
        else:
            return redirect("/404")
    return render(request,'download.html')




def DownloadText(request,slug):
    if not slug:
        return redirect("/404")
    if slug:
        try:
            text = SharedText.objects.filter(slug=slug).first()
        except Exception as ex:
            print(ex)
            return redirect("/404")
        if not text:
                return redirect("/404")
        elif text.is_expired():
            if(RemoveAllExpiredFiles()):
                return redirect('/404')
            return redirect('/404')
        else:
            return render(request,"SingleTextFileView.html",{"text":text})
    else:
        return redirect("/404")
    return redirect('/404')
            











def Custom404(request):
    return render(request,"404.html")


