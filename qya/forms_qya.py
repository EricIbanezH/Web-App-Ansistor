from secrets import choice
from django import forms
from .views import listaproductos

class formQuestion(forms.Form):
    tipoPost = forms.CharField(label='',widget=forms.TextInput(attrs={'value':'pregunta',
                                                                       'hidden':''}))
    
    title = forms.CharField(label='titulo de la pregunta ',
                            max_length=350,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'
                                                            }))
    cuerpo = forms.CharField(label='cuerpo de la pregunta ',
                            max_length=200,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'
                                                            }))
    producto = forms.ChoiceField(choices=listaproductos(),label='Producto ')
    tipo = forms.ChoiceField(choices=[('error','Error'),('duda','Duda'),('sugerencia','Sugerencia')],
                             label='Tipo de pregunta ')

class formAnswer(forms.Form):
    tipoPost = forms.CharField(label='',widget=forms.TextInput(attrs={'value':'respuesta',
                                                                       'hidden':''}))
    
    title = forms.CharField(label='Titulo de la respuesta ',
                            max_length=350,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'
                                                            }))
    cuerpo = forms.CharField(label='cuerpo ',
                            max_length=200,
                            required=True,
                            widget=forms.TextInput(attrs={'class':'form-control'
                                                            }))