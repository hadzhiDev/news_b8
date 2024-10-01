from news.models import News
from django import forms


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = (
            'title',
            'description',
            'content',
            'category',
        )

        widgets = {
            'title': forms.TextInput(),
            'description': forms.TextInput(),
            'content': forms.Textarea(),
            'category': forms.Select(),
        }