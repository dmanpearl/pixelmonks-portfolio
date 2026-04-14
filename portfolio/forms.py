from django import forms


class ContactForm(forms.Form):
    CONTACT_METHOD_CHOICES = [
        ("", "— preferred contact method —"),
        ("email", "Email"),
        ("phone", "Phone"),
        ("whatsapp", "WhatsApp"),
        ("signal", "Signal"),
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
    contact_method = forms.ChoiceField(
        choices=CONTACT_METHOD_CHOICES,
        required=False,
    )
    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={"placeholder": "What's on your mind?", "rows": 5}),
    )

    def clean(self):
        cleaned = super().clean()
        phone = cleaned.get("phone")
        method = cleaned.get("contact_method")
        if method in ("phone", "whatsapp", "signal") and not phone:
            self.add_error("phone", "Phone number is required for this contact method.")
        return cleaned
