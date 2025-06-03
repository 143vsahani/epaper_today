from django.shortcuts import render, redirect
from .models import Epaper
from .forms import EpaperForm

def upload_epaper(request):
    if request.method == 'POST':
        form = EpaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('epaper_list')
    else:
        form = EpaperForm()
    return render(request, 'epaper/upload.html', {'form': form})

def epaper_list(request):
    epapers = Epaper.objects.filter(is_published=True).order_by('-date')
    return render(request, 'epaper/list.html', {'epapers': epapers})
