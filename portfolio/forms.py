from django import forms


class ContactForm(forms.Form):
    """Form liên hệ."""
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'NAME',
            'data-translate-placeholder': 'name_placeholder'
        })
    )
    
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'EMAIL',
            'data-translate-placeholder': 'email_placeholder'
        })
    )
    
    subject = forms.CharField(
        label='',
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'SUBJECT',
            'data-translate-placeholder': 'subject_placeholder'
        })
    )
    
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'YOUR MESSAGE',
            'data-translate-placeholder': 'message_placeholder'
        })
    )
    
    def clean_name(self):
        """Validate name field."""
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError('Tên phải có ít nhất 2 ký tự.')
        return name
    
    def clean_message(self):
        """Validate message field."""
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError('Nội dung tin nhắn phải có ít nhất 10 ký tự.')
        return message