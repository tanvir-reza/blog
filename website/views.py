from django.shortcuts import render

# Create your views here.


def custom_404(request, exception):
    return render(request, '404.html', status=404)
