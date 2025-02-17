from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(label='Your Comment', widget=forms.Textarea)