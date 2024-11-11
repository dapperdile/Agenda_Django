from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init'
            }
        ),
        label='Primeiro Nome',
        help_text='Nome sem espaço'

    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )

        # widgets = {
        #     'first_name': forms.TextInput(),
        # }
    
    def clean(self):

        self.add_error(
            None,
            ValidationError(
                'Mensagem de Erro',
                code='invalid'
            )
        )
        return super().clean()