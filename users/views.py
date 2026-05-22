from django.shortcuts import render
from .models import User
from django.shortcuts import redirect


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

#about.html fayli uchun view
def about(request):
    return render(request, 'about.html')

#add_user.html fayli uchun view
def add_user(request):
    return render(request, 'add_user.html')


#add_user.html faylidan malumotlarni qabul qilib, bazaga saqlash uchun view
def add_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        User.objects.create(name=name, last_name=last_name, phone_number=phone_number)
        return redirect('index')
    return render(request, 'add_user.html')