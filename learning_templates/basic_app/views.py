from django.shortcuts import render

def index(request):
    context_dic ={"text":"Hello world!","number":100}
    return render(request,'basic_app/index.html',context_dic)

def others(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/reletive_url_templates.html')

