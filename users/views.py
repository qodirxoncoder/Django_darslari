from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

#about.html fayli uchun view
def about(request):
    return render(request, 'about.html')