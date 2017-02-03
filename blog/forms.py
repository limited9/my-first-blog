from django import forms
from .models import Post, Comment

class  PostForm(forms.ModelForm):

    class Meta: # 폼을 만들기 위해 어떤 모델이 쓰여야 하는지 장고에게 알려주는 구문
        model = Post
        fields = ('title', 'text', ) # title과 text 컬럼

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
