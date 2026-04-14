from django import forms


class ContactForm(forms.Form):
    PHONE_METHOD_CHOICES = [
        ("phone", "Phone"),
        ("whatsapp", "WhatsApp"),
    ]

    name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={"placeholder": "Your name"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "your@email.com"}),
    )
    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "+1 (555) 000-0000"}),
    )
    phone_method = forms.ChoiceField(
        choices=PHONE_METHOD_CHOICES,
        initial="phone",
        required=False,
    )
    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={"placeholder": "What's on your mind?", "rows": 5}),
    )
