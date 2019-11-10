from django import forms
from .models import Article





#########################################To retrieve database fields with same height and width also known as Raw HTML form##########
class ArticleForm(forms.ModelForm):
	class Meta:
		model=Article
		fields =[
		'article_title',
		'article_description'
		] 





##########################################To create our own form also known as Pure Django forms#########
# class ArticleForm(forms.Form):
# 	article_title = forms.CharField(widget=forms.TextInput(
# 													attrs={"placeholder":"Enter article title here"}))
# 	article_description = forms.CharField(required=False, widget=forms.Textarea(
# 													attrs={"placeholder":"Enter description here"}))		

				

		