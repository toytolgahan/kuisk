print("views.py is getting imported")
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from .models import Discipline, Person
# Create your views here.


def get_parent_discipline():
    return get_object_or_404(Discipline, title="Artificial Intelligence")

def get_main_discipline():
    parent_discipline = get_parent_discipline()
    return get_object_or_404(Discipline, parents=parent_discipline)

def home(request):
    print("home1")
    main_disciplines = get_main_discipline()
    print("home2")
    parent_discipline = get_parent_discipline()
    print("home4")
    context =  {'main_disciplines':main_disciplines, 'parent_discipline':parent_discipline}
    print("home5")
    return render(request, 'home.html', context)

def why(request):
    main_disciplines = get_main_discipline()
    context = {'main_disciplines':main_disciplines}
    return render(request,'why.html', context)

def discipline_detail(request, discipline_slug):
    main_disciplines = get_main_discipline()
    discipline = get_object_or_404(Discipline, slug=discipline_slug)
    subdisciplines = Discipline.objects.filter(parents=discipline)
    context = {'discipline': discipline, 'subdisciplines':subdisciplines,'main_disciplines':main_disciplines}
    return render(request, 'discipline_detail.html',context)

def person_detail(request, pk):
    main_disciplines = get_main_discipline()
    person = get_object_or_404(Person, pk=pk)
    context = {'person':person,'main_disciplines':main_disciplines}
    return render(request, 'person_detail.html',context)


def search(request):
    query = request.GET.get('query', '')
    discipline_results = Discipline.objects.filter(title__icontains=query)
    person_results = Person.objects.filter(last_name__icontains=query)
    context = {'discipline_results':discipline_results,'person_results':person_results, 'query':query}
    return render(request, 'search_results.html', context)

