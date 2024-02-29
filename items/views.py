from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import Products
from django.http import HttpResponseRedirect
from .forms import LoginForm
def home(request):
    return render (request, 'parts/home.html')


def tracks(request):
    context = {'data' : Products.objects.all()}
    return render (request, 'parts/tracks.html', context)


def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        content = request.POST['content']
        price = request.POST['price']
        image = request.FILES['image']
        Products.objects.create(name=name, content=content, price=price, image=image)
        return HttpResponseRedirect(reverse('tracks'))
    return render (request, 'parts/about.html')


def contact(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data['name'],
                content=form.cleaned_data['type'],
                price=form.cleaned_data['price'],
                image=form.cleaned_data['image']
            )
            return HttpResponseRedirect(reverse('tracks'))
    else:
        form = LoginForm()

    return render(request, 'parts/contact.html', {'form': form})


def tracks_show(request, id):
    product = Products.objects.get(id=id)
    context = {'product': product}
    return render(request, 'parts/tracks_show.html', context)


def tracks_delete(request, id):
    Products.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('tracks'))


def tracks_update(request, id):
    context={}
    if (request.method == 'POST'):
        product = Products.objects.get(id=id)
        product.name = request.POST['name']
        product.content = request.POST['content']
        product.price = request.POST['price']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return HttpResponseRedirect(reverse('tracks'))

    product = Products.objects.get(id=id)
    context['product'] = product
    return render(request, 'parts/tracks_update.html', context)


def category(request):
    context = {'data' : Products.objects.all()}
    return render (request, 'parts/category.html', context)


