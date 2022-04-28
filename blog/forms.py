from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, Post


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


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'slug': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
        'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
    }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('slug may not be "create"')
        return new_slug
