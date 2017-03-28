from django.views import generic
from .models import product
from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    all_garments = product.objects.all()
    garments_men = []
    garments_women = []
    for garment in all_garments:
        if(garment.gender == "Men"):
            garments_men.append(garment)
        else:
            garments_women.append(garment)
    return render(request, 'garments/index.html', {'garments_men': garments_men,'garments_women': garments_women})

# class IndexView(generic.TemplateView):
#     template_name = 'garments/index.html'


class Contact_us_View(TemplateView):
    template_name = 'garments/contact_us.html'



class About_us_View(TemplateView):
    template_name = 'garments/about_us.html'

def gallery_men(request):
    all_garments = product.objects.all()
    garments_men = []

    for garment in all_garments:
        if(garment.gender == "Men"):
            garments_men.append(garment)

    return render(request, 'garments/gallery.html', {'all_garments': garments_men})

def gallery_women(request):
    all_garments = product.objects.all()
    garments_women = []

    for garment in all_garments:
        if (garment.gender == "Women"):
            garments_women.append(garment)

    return render(request, 'garments/gallery.html', {'all_garments': garments_women})

def detail(request,product_id):
    garment_details = product.objects.get(pk=product_id)

    return render(request, 'garments/detail.html', {'all_garments': garment_details})








