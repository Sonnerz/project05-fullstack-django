from django import forms
from .models import Post, PostComment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add post title'}),
            'tag': forms.TextInput(attrs={'placeholder': 'Add keywords for example; camera, photography, ISO...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Add post content...'})
        }


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('comment',)


class AdminPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')
