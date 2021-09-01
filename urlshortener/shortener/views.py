from django.shortcuts import render
from .forms import NewUrlForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        url = NewUrlForm(request.POST)
        if url.is_valid():
            new_url = url.save()
            form = NewUrlForm()
            data = {
                'form': form,
                'shortened_url': f'http://127.0.0.1:8000/{new_url.id}'
            }
            return render(request, 'shortener/index.html', data)
    else:
        form = NewUrlForm()
        data = {
            'form': form,
            'shortened_url': ''
            }
        return render(request, 'shortener/index.html', data)

    