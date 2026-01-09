from django.shortcuts import get_object_or_404, render
from .models import Reference

def home(request):
    refs = Reference.objects.all()
    return render(request, 'catalog/home.html', {'refs': refs})

def reference_detail(request, slug):
    ref = get_object_or_404(Reference, slug=slug)
    photos = ref.photos.all()
    return render(request, 'catalog/reference_detail.html', {'ref': ref, 'photos': photos})
