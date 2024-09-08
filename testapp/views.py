from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        "veriable":"this is send by index"
    }
    return render(request,"index.html",context)
    # return HttpResponse("hello this is home page")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html")
def contact(request):
    return render(request,"contact.html")
def Organic_Farming(request):
    return render(request,"Organic_Farming.html")
def Organic_Fruits(request):
    return render(request,"Organic_Fruits.html")
def Organization_Information(request):
    return render(request,"Organization_Information.html")