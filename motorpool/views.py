from django.shortcuts import render, get_object_or_404
from motorpool.models import Brand


def brand_list(request):
    template_name = 'motorpool/brand_list.html'
    brand_objects = Brand.objects.all()
    brand_number = brand_objects.count()
    context = {
        'brand_objects': brand_objects,
        'brand_number': brand_number,
    }
    return render(request, template_name, context)


def brand_detail(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    context = {
        'brand': brand,
        'cars': brand.cars.all(),
        'brand_number': Brand.objects.count(),
    }
    return render(request, 'motorpool/brand_detail.html', context)
