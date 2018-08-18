from django import forms


class SubmitCodeForm(forms.Form):
    file = forms.FileField()
