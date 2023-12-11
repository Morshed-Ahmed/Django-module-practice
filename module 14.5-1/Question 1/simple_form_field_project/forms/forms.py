from django import forms

class Register(forms.Form):
    name = forms.CharField(label='Your Name',max_length=5,help_text= '', widget= forms.TextInput(attrs = {'placeholder' : 'Enter your name'}))
    email = forms.EmailField(label='Your Email')
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    password = forms.CharField(help_text='Password must be 6 digit',min_length=6,widget = forms.PasswordInput(),label='Your Password') 
    conPassword = forms.CharField(widget = forms.PasswordInput(),label='Conform Password') 
    agree = forms.BooleanField()


class Contact(forms.Form):
    first_name = forms.CharField(initial='Your name')
    description = forms.CharField(widget= forms.Textarea(attrs={'placeholder' : 'Comment Please'}))
    phoneNumber = forms.CharField( label='Phone Number',max_length= 12,widget= forms.NumberInput() )

