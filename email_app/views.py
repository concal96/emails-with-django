from django.shortcuts import render
from email_app.forms import EmailForm
from email_app.models import Email
from django.core.mail import send_mail
# Create your views here.
def thanks(request):
    return render(request,'email_app/thanks.html')

def index(request, id=0):
    form = EmailForm()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            #save the form to the Email database
            form.save()
            #attempt to set email to latest email object
            recent = Email.objects.last()
            #send mail to entered email from above field
            send_mail(
                'Why look for The Great Question Of Life, The Universe and Everything?',
                "Eventually just habit, I think. \n\nThanks for visiting!\n\n- Connor",
                '',
                [recent],
                fail_silently=False,
            )
            return thanks(request)
    
    return render(request,'email_app/index.html',{'form':form})

    
