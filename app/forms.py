"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))


class AnketaForm(forms.Form):
    username = forms.CharField(label = 'Ваше имя', min_length = 4, max_length = 254)
    gender = forms.ChoiceField(label = 'Ваш пол', choices = [('1', 'Мужской'), ('2', 'Женский')], widget=forms.RadioSelect, initial = 1)
    bisuness = forms.ChoiceField(label = 'Ваш род деятельности', choices = [('1', 'Школьник'), ('2', 'Студент'), ('3', 'Преподаватель'), ('4', 'Другая')], widget=forms.RadioSelect, initial = 1)
    email = forms.EmailField(label = 'Ваш e-mail', min_length = 7)
    promotion = forms.ChoiceField(label = 'Как часто вы хотите получать рассылку', choices = (('1', 'Никогда'), ('2', 'Раз в полгода'), ('3', 'Раз в месяц'), ('4', 'Раз в неделю')))
    notice = forms.BooleanField(label = 'Был ли вам полезен наш сайт?', required = False)
    message =forms.CharField(label = 'Как бы мы могли улучшить наш сайт', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': 'Комментарий'}



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','content','image',)
        labels = {'title': 'Заголовок','description': 'Описание','content': 'Содержание','image': 'Картинка'}
