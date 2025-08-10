# contact/forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'اكتب رسالتك هنا...'}),
        }
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="الاسم")
    email = forms.EmailField(label="البريد الإلكتروني")
    message = forms.CharField(widget=forms.Textarea, label="الرسالة")
