from django.shortcuts import render

def jinja(request):
    return render(request,'jinja.html',context={'name':'Adi'})

def jinja1(request):
    return render(request,'jinja1.html',context={'interview': 99})

def jinja2(request):
    return render(request,'jinja2.html',context={'identity':'Indian','identity1':'Odia'})

def jinja3(request):
    return render(request,'jinja3.html',context={'language':'python','language1':'html','language2':'css'})
