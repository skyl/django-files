from django import forms
from files.models import File

class FileForm(forms.ModelForm):
    ''' Simple File with SplitDateTime for jq-ui widgets '''

    class Meta:
        model = File
        exclude = ('object_id', 'content_type', 'owner')

class SearchForm(forms.Form):
    terms = forms.CharField(required=False)
    action = forms.CharField(initial="search",widget=forms.HiddenInput)
