from django.shortcuts import render
from . models import PasswordGenerator 
import random
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect 

def home(request):
    return render(request, "generator/home.html")

def password(request):
    try:
        characters = list()
        if request.POST.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if request.POST.get('lowercase'):
            characters.extend(list('abcdefghijklmnopqrstuvwxyz'))
        if request.POST.get('special'):
            characters.extend(list('~!@#$%^&*()_+="/\?<>.:;'))
        if request.POST.get('numbers'):
            characters.extend(list('0123456789'))
        length = int(request.POST.get('length',14))
        site = request.POST.get('site')
        print(length,'aaaaaaaaaaaaa')
        print(site,'gggggggggg')

        thepassword = ''
        for x in range(length):
            thepassword += random.choice(characters)
        p = PasswordGenerator.objects.create(site=site, passwords=thepassword)
        p.save()
        print('111111111111111111',thepassword)
    except:
        thepassword = 'ERROR: Select an option to generate password'
    print(thepassword,'----------------------')
    return render(request,'generator/home.html',{'password' : thepassword})

def show_passwords(request):
    passwords = PasswordGenerator.objects.all()
    print(passwords,'ooooooooooooooooooooo')
    context = {'passwords':passwords}
    return render(request,'generator/show_passwords.html', context)

def delete_password(request, id):
    password = get_object_or_404(PasswordGenerator, id=id)
    print(password,'gggggggggggg')
    password.delete()
    return redirect('show_passwords')

def search_password(request):
    query =  request.GET.get('q')
    print(query,'kkkkkkkkkkkk')
    if query:
        passwords = PasswordGenerator.objects.filter(site__icontains = query)
        print(passwords,'jjjjjjjjjjjj')
    else:
        passwords = PasswordGenerator.objects.all()
    context = {'passwords':passwords}
    return render(request, 'generator/show_passwords.html',context)

# Create your views here.
