from django.shortcuts import render,redirect 

def Error__404(request, exception):
    return render(request, '404.html', status=404)