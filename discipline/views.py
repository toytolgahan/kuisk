from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from .models import Discipline, Person
# Create your views here.


parent_discipline = Discipline.objects.filter(title="Artificial Intelligence")
main_disciplines = Discipline.objects.filter(parents=parent_discipline)


def home(request):
    print("parent disciplines ",parent_discipline)
    print("in list form ",list(main_disciplines))
    print("main disciplines: ",main_disciplines)
    context =  {'main_disciplines':main_disciplines, 'parent_discipline':parent_discipline}
    return render(request, 'home.html', context)

def why(request):
    context = {'main_disciplines':main_disciplines}
    return render(request,'why.html', context)

def discipline_detail(request, discipline_slug):
    discipline = get_object_or_404(Discipline, slug=discipline_slug)
    subdisciplines = Discipline.objects.filter(parents=discipline)
    context = {'discipline': discipline, 'subdisciplines':subdisciplines,'main_disciplines':main_disciplines}
    return render(request, 'discipline_detail.html',context)

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    context = {'person':person,'main_disciplines':main_disciplines}
    return render(request, 'person_detail.html',context)


def search(request):
    query = request.GET.get('query', '')
    discipline_results = Discipline.objects.filter(title__icontains=query)
    person_results = Person.objects.filter(last_name__icontains=query)
    context = {'discipline_results':discipline_results,'person_results':person_results, 'query':query}
    return render(request, 'search_results.html', context)

