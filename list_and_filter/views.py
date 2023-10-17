from django.shortcuts import render

def hello_template(request):
    return render(request, 'list_and_filter/hello.html')