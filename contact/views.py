from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    #print("Peticion: {}".format(request.method))

    contactForm= ContactForm() #instancia de la clase
    if request.method=="POST":
        contactForm=ContactForm(data=request.POST)#capturar la informacion del formulario- sobreescribe la accion de la linea 9
        #capturar la informacion que se recibe desde la peticion POST
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')
        content= request.POST.get('content', '')
        #enviar email
        email=EmailMessage(
            "La Caffetiera: Nuevo mensaje de contacto",
            "De{} <{}>\n\nEscribir:\n\n{}".format(name,email,content),
            "no-contestar@inbox.mailtrap.io",
            ["mpaula_12@live.com"],
            reply_to=[email]
        )
        #enviar mail
        try:
            email.send()
            print("Hola")
            return redirect(reverse('contact')+"?ok")
        except:
            return redirect(reverse('contact')+"?fail")
        

    return render(request,"contact/contact.html", {'contactForm':contactForm})
