from django.forms import ModelForm
from .models import Author

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['gender','first_name','last_name','email']