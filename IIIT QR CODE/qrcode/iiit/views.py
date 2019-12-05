from django.shortcuts import render,redirect
from .models import userinput
from .forms import rform
from django.core.mail import send_mail
# Create your views here.
def confirm(request):
    return render(request,'cover/index.html')
def index(request):
    if request.method == 'POST':
        form=rform(request.POST)

        if form.is_valid():
            new_req= userinput(fname=request.POST['firstname'],lname=request.POST['lastname'],
            email=request.POST['email'],scholar_no=request.POST['scholar'],year=request.POST['year'],
            branch=request.POST['branch'])
            new_req.save()
            send_mail(
            'Registration Successful',
            new_req.fname+' '+new_req.lname+' ,\n'+'Thank You for Registering. \n\nFind link to your qr code below\n\n https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + new_req.fname+'_'+new_req.lname,
            'opensources.mr@gmail.com',
            [new_req.email],
            fail_silently=False,
            )
            return render(request,'cover/index.html',{'image':new_req.fname+'_'+new_req.lname+'-'+new_req.scholar_no})

    else:
        form=rform()

    context={'form':form}

    return render(request,'qr/index.html',context)
