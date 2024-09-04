from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306165862',
        'name': 'William Matthew Saputra',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
