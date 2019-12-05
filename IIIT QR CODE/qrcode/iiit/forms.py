from django import forms
class rform(forms.Form):
    firstname=forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'First Name'
    }))

    lastname=forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Last Name',
        'id':'lastName'
    }))

    email=forms.CharField(max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'you@example.com',
        'id':'email'
    }))

    scholar=forms.CharField(max_length=8,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Roll No.',
        'id':'address'
    }))

    year=forms.CharField(max_length=1,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'ex:- 1/2/3/4',
        'id':'yes'
    }))

    branch=forms.CharField(max_length=3,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'ex:- CSE/IT/ECE',
        'id':'br'
    }))


