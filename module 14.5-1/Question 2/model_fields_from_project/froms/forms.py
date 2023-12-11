from django import forms
from froms.models import JobsPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobsPost
        fields = '__all__'
        widgets = {
            'jobTitle': forms.TextInput(),
            'postExpireDate' : forms.TextInput(attrs = {'type':'date'})
        }