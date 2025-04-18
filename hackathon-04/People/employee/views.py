from django.shortcuts import render
import random

# Create your views here.

#Taking salary input
def salary_form(request):
    return render(request, 'employee/salary_form.html')

#Calculate the salary
def salary_calc(request):
    if request.method == 'POST':
        name = request.POST['name']
        gross = float(request.POST['gross_salary'])
        tax = float(request.POST['tax'])
        bonus = float(request.POST['bonus'])

        net_salary =  gross - ((gross)*tax/100) + bonus        
        return render(request, 'employee/salary_calc.html', {'name': name, 'net_salary': net_salary})
    return render(request, 'employee/salary_form.html')

#WordJumble
def jumble_word(request):
    jumbled = ''
    original = ''
    if request.method == 'POST':
        original = request.POST['word']
        temp = list(original)
        random.shuffle(temp)
        jumbled = ''.join(temp)
    return render(request, 'employee/jumble.html', {'original': original, 'jumbled': jumbled})