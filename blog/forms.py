from django import forms
from django.core.exceptions import ValidationError
from .models import Tag


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        exclude = []

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('slug may not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'slug must be unique. We have "{new_slug}" slug already.')
        return new_slug

    # def save(self):
    #     new_tag = Tag.objects.create(title=self.cleaned_data['title'],
    #                                  slug=self.cleaned_data['slug'])
    #     return new_tag
