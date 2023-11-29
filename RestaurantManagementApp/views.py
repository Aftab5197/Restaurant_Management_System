from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from RestaurantManagementApp.models import Food, Cuisine


# Create your views here.
@login_required
def home(request):
    food = Food.objects.all()
    data = {'foods':food}
    return render(request,'home.html',data)

@login_required
def addfun(request):
    if request.method == "POST":
        f = Food()
        f.item_name = request.POST['tbitem']
        f.menu_type = request.POST['tbmenu']
        f.timings = request.POST['tbtimings']
        f.food_type = request.POST['tbtype']
        f.price = request.POST['tbprice']
        f.cuisine = Cuisine.objects.get(cname=request.POST['ddlcuisine'])
        f.save()
        return redirect(home)
    else:
        c = Cuisine.objects.all()
        data = {'cuisine':c}
    return render(request,'add.html',data)

@login_required
def editfun(request,id):
    f = Food.objects.get(id=id)
    if request.method == 'POST':
        f.item_name = request.POST['tbitem']
        f.menu_type = request.POST['tbmenu']
        f.timings = request.POST['tbtimings']
        f.food_type = request.POST['tbtype']
        f.price = request.POST['tbprice']
        f.cuisine = Cuisine.objects.get(cname=request.POST['ddlcuisine'])
        f.save()
        return redirect(home)
    else:
        cuisines = Cuisine.objects.all()
        data = {'cuisine': cuisines,'food':f}
    return render(request, 'edit.html', data)

@login_required
def deletefun(request,id):
    f = Food.objects.get(id=id)
    f.delete()
    return redirect(home)

@login_required
def dummy(request):
    return render(request,'index.html')
@login_required
def searchBar(request):
    if request.method == "GET":
        query = request.GET['query']
        if query:
            foods = Food.objects.filter(item_name__icontains = query)
            return render(request,'search.html',{'foods':foods})
        else:
            print("no information to show")
            return render(request,'search.html',{})

@never_cache
def loginfun(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid user')
            return redirect(loginfun)
        user = authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'Invalid password')
        else:
            login(request,user)
            return redirect(dummy)
    return render(request,'login.html')



@never_cache
def registerfun(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['pass']
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect(registerfun)

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,

        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")
        return redirect(registerfun)
    return render(request, 'register.html')


@never_cache
def logoutfun(request):
    logout(request)
    return redirect(loginfun)
