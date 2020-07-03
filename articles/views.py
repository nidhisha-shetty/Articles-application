#from django.http import HttpResponse                   ###This will be required if we execute code on line number 15 (	#return HttpResponse("<h1> Welcome to the world of articles </h1>")) 
from django.http import Http404          #to execute try catch block code for page not found (line 48-51)
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
from .forms import ArticleForm

from .models import Article




########################Home page view #################################
def home_view(request):
	
	#return HttpResponse("<h1> Welcome to the world of articles </h1>")
	return render(request, "home_page_links.html",{})


#####################Main home page view ##############################
def main_home_view(request):
	return render(request, "main-home-view.html",{}) 

#####################Guest home page view ##############################
def guest_home_view(request):
	return render(request, "guest_home_view.html", {})

def register(request):

	if request.method=='POST':
		f_n=request.POST['First name']
		l_n=request.POST['Last name']
		un=request.POST['Username']
		email=request.POST['Email address']
		pwd=request.POST['Password']
		cnf_pwd=request.POST['confirm password']

	
		if pwd==cnf_pwd:
			if User.objects.filter(username=un).exists():
				
				messages.info(request, "Username already exists")
				return redirect("register")
			elif User.objects.filter(email=email).exists():
				messages.info(request, "Email already exists")
				return redirect("register")
			else:
				user=User.objects.create_user(username=un,password=pwd,email=email,first_name=f_n,last_name=l_n)
				user.save();
				messages.info(request, "User added successfully!")
				return redirect("register")
		else:
			messages.info(request, " 'Password' and 'Confirm Password' do not match")
			return redirect("register")
	else:	
		return render(request, "register.html")


##################### Login view ##############################

def login(request):
	if request.method=='POST':
		un=request.POST['Username']
		pwd=request.POST['Password']

		user=auth.authenticate(username=un, password=pwd)
		if user is not None:
			auth.login(request, user)
			return redirect("admin_home_page")
		else:
			messages.info(request, "Invalid credentials")
			return redirect("login")

	else:
		return render(request, "login.html")
	
	messages.info(request, "Invalid credentials")

##################### guest article list ##############################
def guest_article_list(request, pass_id):

	try:    #same execution of code as in line 46, this time with try catch block
		obj=Article.objects.get(id=pass_id)
	except:     #here exception is "DoesNotExist" error
		raise Http404

	context={
		'Title': obj.article_title,
		'Desc': obj.article_description,
		"object": obj
	}	
	return render(request, "guest_view.html", context)


#################To store data to DB#############################
def article_detail_store_view(request):
	form=ArticleForm(request.POST or None)
	if form.is_valid():
		messages.info(request, "Article created!")
		form.save()
		form=ArticleForm()
	context={
		'Form':form
	}	
	return render(request, "article_create.html", context)

def guest_article_create(request):
	form=ArticleForm(request.POST or None)
	if form.is_valid():
		messages.info(request, "Article created!")
		form.save()
		form=ArticleForm()
	context={
		'Form':form
	}	
	return render(request, "guest_article_create.html", context)

#################To retrieve data #######################################
# def article_detail_display_view(request):
# 	obj=Article.objects.get(id=17)
# 	context={
# 		'Title': obj.article_title,
# 		'Desc': obj.article_description

# 	}	
# 	return render(request, "article_detail.html", context)



#################To retrieve data from db of specific id#######################################
def article_detail_display_view(request, pass_id):  #since we will even pass the id in the url
	#obj=Article.objects.get(id=pass_id) #pass_id is the id that the user passes in the url
	#obj=get_object_or_404(Article, id=pass_id)  #to get error message as "PageNotFound" inplace of "DoeNotExist" for invalid object id's

	try:    #same execution of code as in line 46, this time with try catch block
		obj=Article.objects.get(id=pass_id)
	except:     #here exception is "DoesNotExist" error
		raise Http404

	context={
		'Title': obj.article_title,
		'Desc': obj.article_description
	}	
	return render(request, "article_detail.html", context)


def guest_article_detail_display_view(request, pass_id):

	try:    #same execution of code as in line 46, this time with try catch block
		obj=Article.objects.get(id=pass_id)
	except:     #here exception is "DoesNotExist" error
		raise Http404

	context={
		'Title': obj.article_title,
		'Desc': obj.article_description
	}	
	return render(request, "guest_article_display.html", context)

##############################To delete a object from the database#######################
def article_delete_view(request, pass_id):

	obj=get_object_or_404(Article, id=pass_id)
	if request.method == "POST":
		obj.delete()
		messages.info(request, "Article deleted successfully")
		return redirect("/article_list/")

	context={
	'object':obj
	}

	return render(request, "article_delete.html",context)





#########################View the list of objects to view the details of each object#################################333
def article_list_view(request):
	obj=Article.objects.all()
	context={
		'object':obj
	}
	return render(request, "article_list.html", context)


def guest_article_view(request):
	obj=Article.objects.all()
	context={
		'object':obj
	}
	return render(request, "guest_view.html", context)




#########################View the list of objects to delete each object#################################
def article_list_delete_view(request):
	obj=Article.objects.all()
	context={
		'object':obj
	}
	return render(request, "article_list_delete.html", context)

###########################To edit data of database############################################
# def render_initial_data(request):
# 	initial_data={
# 		'article_title':"This is article title"

# 	}
# 	obj=Article.objects.get(id=25)
# 	form=ArticleForm(request.POST or None, initial=initial_data)
# 	context={
# 		"form": form
# 	}
# 	return render(request,"article_edit.html",context)







# def render_initial_data(request):

# 	initial_data={                                 #used to display default data
# 		'article_title':"This is perfect"
# 	}
	

# 	obj=Article.objects.get(id=35)
# 	form=ArticleForm(request.POST or None,  instance=obj)
# 	if form.is_valid():
# 		form.save()
# 		form=ArticleForm()
# 	context={
# 		"my_form": form,
# 	}
# 	return render(request, "article_edit.html", context)	



def render_initial_data(request, pass_id):
	obj=Article.objects.get(id=pass_id)

	form=ArticleForm(request.POST or None,  instance=obj)  #instance is used to dispaly data of each field from DB
	if form.is_valid():
		form.save()
		messages.info(request, "Article edited successfully!")
		return redirect("/article_list/")
	context={
		"my_form": form,
		"object": obj
	}
	return render(request, "article_edit.html", context)


def article_list_render_data(request):
	obj=Article.objects.all()
	context={
		'object':obj
	}
	return render(request, "article_list_edit.html", context)
	
def logout_view(request):
	auth.logout(request)
	return redirect("/")
