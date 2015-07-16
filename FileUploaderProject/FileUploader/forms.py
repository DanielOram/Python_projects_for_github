__author__ = 'danieloram'

from django import forms

#simple form for entering the file
class ImageUploadForm(forms.Form):
    imageFile = forms.FileField(
        label = 'Select a file to upload!',
        help_text= 'There is no size limit but please try to keep it to 2.5mb or less'
    )