from django import forms



class ContactForm(forms.Form):
    Name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class":"input100",
            "placeholder":"Name",
            "name":"name",
        }
    ))

    Email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"input100",
                "placeholder":"Email",
                "name":"email",
            }
    ))

    Message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"input100",
                "placeholder":"Message",
                "name":"message",
            }
    ))
