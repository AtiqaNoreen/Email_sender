# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.conf import settings

# # Create your views here.

# def send_mail_page(request):
#     context={}

#     if request.method=='POST':
#         address=request.POST.get("address")
#         subject=request.POST.get("Subject")
#         message=request.POST.get("message")

#         if address and subject and message:
#             try:
#                 send_mail(subject,message,settings.EMAIL_HOST_USER,[message])
#                 context['result']='Email sent Successfully'
#             except Exception as e:
#                 context['result']=f'Error sending Email {e}'              
#         else:
#             context['result']='All field require'
#     else:
#         return render(request,"index.html",context)        

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get("address")
        subject = request.POST.get("Subject")
        message = request.POST.get("Message")

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'

        # ✅ POST ke baad bhi render return karo
        return render(request, "index.html", context)

    # ✅ GET request
    return render(request, "index.html", context)
