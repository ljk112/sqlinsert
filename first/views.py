from django.shortcuts import render
from .models import Clothes

def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('img')
        clothes = Clothes(name=name, img=img)
        clothes.save()

    return render(request, 'template.html')

def index(request):
    numbers = list(range(1, 21))

    try:
        selected_number = int(request.GET.get('number'))
    except:
        selected_number = 1


    if selected_number == 1:
        clothes = Clothes.objects.all()
    else:
        min_range = (selected_number - 1) * 10000 + 100000
        max_range = selected_number * 10000 + 100000
        clothes = Clothes.objects.filter(name__gte=min_range, name__lt=max_range)

    return render(request, 'template.html', {'clothes': clothes, 'numbers': numbers, 'selected_number': selected_number})


def index2(request):
    clothes = Clothes.objects.filter(name__gt=100000, name__lt=123456)
    return render(request, 'template.html', {'clothes': clothes})
