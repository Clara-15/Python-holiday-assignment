# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        # Process user_input as needed
        return render(request, 'result.html', {'result': result})
