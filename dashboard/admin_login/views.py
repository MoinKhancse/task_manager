from django.shortcuts import render,redirect,HttpResponse
from admin_login.models import User,data_add
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def reg(request):
    if request.method == "POST":
        user_name = request.POST.get('name')
        email = request.POST.get('email')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if password_1 != password_2:
            return redirect('reg')
        else:
            user_reg =User.objects.create_user(user_name,email,password_1)
            return redirect('login')
    return render(request, 'reg.html')

def login_page(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('password')

        user = authenticate(username = a, password = b)
        if user != None:
            login(request, user)
            return redirect("index")
        else:
            return redirect('login')

    return render(request, 'login.html')

def admin_logout(request):
    logout(request)
    return redirect('login')

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('login')
def add_data(request):
    if request.user.is_authenticated:

        if request.method == "POST" and request.FILES:  
            p_name = request.POST.get('product_name') 
            p_title = request.POST.get('product_title') 
            p_catagory = request.POST.get('product_category')
            image = request.FILES['product_img']

            add_save = data_add(name=p_name,title=p_title,catagory=p_catagory,image=image)
            add_save.save()
            return redirect('index')
        
def show(request):
    show_data = data_add.objects.all()
    return render(request, 'show.html',{'context':show_data})

def edit(request):
    pass