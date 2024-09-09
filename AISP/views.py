from django.shortcuts import render
from .forms import SearchForm

def search(request):
    form = SearchForm()
    results = None
    if request.method == 'GET' and 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Here you can handle the query and search your data models.
            # results = YourModel.objects.filter(name__icontains=query)
            results = f'Search results for "{query}"'
    
    return render(request, 'AISP/home.html', {'form': form, 'results': results})