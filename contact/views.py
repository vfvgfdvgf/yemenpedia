from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"رسالة جديدة من {name}",
                message=message,
                from_email=email,
                recipient_list=['halax.7y7@gmail.com'],  # بريدك
            )

            messages.success(request, "✅ تم إرسال رسالتك بنجاح!")
            return redirect('contact:contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
