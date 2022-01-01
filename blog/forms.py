from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["comment2post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "your Email",
            "text": "Your Comment",
        }
