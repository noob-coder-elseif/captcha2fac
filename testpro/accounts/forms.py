import imp
from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import Group, User

class CaptchaTestForm(forms.Form):
    # myfield = AnyOtherField()
    x = Group.objects.all()
    groups = []
    for y in x:
        groups.append[(f'{y.id}',f'{y.name}')]
    group = forms.ChoiceField(choices=groups)
    captcha = CaptchaField()

# class CaptchaTestModelForm(forms.ModelForm):
#     captcha = CaptchaField()
#     class Meta:
#         model = MyModel