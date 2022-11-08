from django import forms
from django.db.models import Max
from api_rest.models import User,UserSession
userSessionMax = UserSession.objects.aggregate(Max('id_user_session'))['id_user_session__max']
userSessionQ = UserSession.objects.get(id_user_session=userSessionMax)
user = User.objects.get(id_user=userSessionQ.id_user.id_user)

class formLoggin_user(forms.Form):
    usuario = forms.CharField(label='',max_length=50,required=True,
                              widget=forms.TextInput(attrs={'class' : 'form-control',
                                                            'id':'floatingInput',
                                                            'Placeholder':'name@example.com',
                                                            'type':'email'}))

class formLoggin_pass(forms.Form):
    password = forms.CharField(label='',max_length=50,required=True,
                              widget=forms.TextInput(attrs={'class' : 'form-control',
                                                            'id':'floatingPassword',
                                                            'Placeholder':'Password',
                                                            'type':'password'}))

class formLogout(forms.Form):
    password = forms.CharField(label='',max_length=1,required=True,
                              widget=forms.TextInput(attrs={'value' : 's',
                                                            'style':'display:none;'}))
    
class formRegistro(forms.Form):
    class formRegistro_nombre(forms.Form):
        nombre = forms.CharField(label='',max_length=50,required=True,
                                 widget=forms.TextInput(attrs={'class' : 'form-control',
                                                               'id':'firstName'}))
    class formRegistro_apellido(forms.Form):
        apellido = forms.CharField(label='',max_length=100,required=True,
                                 widget=forms.TextInput(attrs={'class' : 'form-control',
                                                               'id':'lastName'}))
    class formRegistro_telefono(forms.Form):
        telefono = forms.IntegerField(label='',max_value=9999999999,required=True,
                                 widget=forms.TextInput(attrs={'class' : 'form-control',
                                                               'id':'Phone'}))
    class formRegistro_email(forms.Form):
        email = forms.EmailField(label='',max_length=50,required=True,
                                 widget=forms.TextInput(attrs={'class' : 'form-control',
                                                               'id':'email',
                                                               'placeholder':'you@example.com'}))
    class formRegistro_pass(forms.Form):
        password = forms.CharField(label='',max_length=50,required=True,
                                 widget=forms.TextInput(attrs={'class' : 'form-control',
                                                               'id':'password',
                                                               'placeholder':'*********'}))

class formPerfil(forms.Form):
    class formPerfil_nombre(forms.Form):
        nombre = forms.CharField(label='',max_length=50,required=True,
                                 widget=forms.TextInput(attrs={'class' : 'form-control',
                                                               'id':'inputFirstName',
                                                               'placeholder':'Ingresa tu nombre',
                                                               'value':user.nombre}))
    class formPerfil_apellido(forms.Form):
        apellido = forms.CharField(label='',max_length=100,required=True,
                                 widget=forms.TextInput(attrs={'class' : 'form-control',
                                                               'id':'inputLastName',
                                                               'value':user.apellidos}))
    class formPerfil_telefono(forms.Form):
        telefono = forms.IntegerField(label='',max_value=9999999999,required=True,
                                 widget=forms.TextInput(attrs={'class' : 'form-control',
                                                               'id':'inputPhone',
                                                               'value':user.telefono}))
    class formPerfil_email(forms.Form):
        email = forms.EmailField(label='',max_length=50,required=True,
                                 widget=forms.TextInput(attrs={'class' : 'form-control',
                                                               'id':'inputUsername',
                                                               'placeholder':'you@example.com',
                                                               'value':user.username}))
    class formPerfil_pass(forms.Form):
        password = forms.CharField(label='',max_length=50,required=True,
                                 widget=forms.TextInput(attrs={'class' : 'form-control',
                                                               'id':'password',
                                                               'placeholder':'*********',
                                                               'value':user.password,
                                                               'hidden':''}))