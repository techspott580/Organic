from django.shortcuts import render,HttpResponse
from datetime import datetime
from testapp.models import Contact
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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Check if the name is empty or missing
        if not name:
            return render(request, 'contact.html', {'error': 'Name is required'})

        # Create and save the new contact
        new_contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        new_contact.save()
        
        
        
    return render(request,"contact.html")
def Organic_Farming(request):
    return render(request,"Organic_Farming.html")
def Organic_Fruits(request):
    return render(request,"Organic_Fruits.html")
def Organization_Information(request):
    return render(request,"Organization_Information.html")