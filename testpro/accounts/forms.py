from django import forms
from captcha.fields import CaptchaField

class CaptchaTestForm(forms.Form):
    # myfield = AnyOtherField()
    captcha = CaptchaField()

# class CaptchaTestModelForm(forms.ModelForm):
#     captcha = CaptchaField()
#     class Meta:
#         model = MyModel