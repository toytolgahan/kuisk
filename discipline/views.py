from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from .models import Discipline, Person, Work
# Create your views here.


parent_discipline = Discipline.objects.get(title="Artificial Intelligence")
main_disciplines = Discipline.objects.filter(parents__title="Artificial Intelligence")
neural_models = Discipline.objects.filter(parents__title="Neural Networks")
machine_learning = Discipline.objects.filter(parents__title="Machine Learning")
reinforcement_learning = Discipline.objects.filter(parents__title="Reinforcement Learning")
human_readable = Discipline.objects.filter(parents__title="Human-Readable Models")

context = {}
context['main_disciplines'] = main_disciplines
context['neural_models'] = neural_models
context['machine_learning'] = machine_learning
context['reinforcement_learning'] = reinforcement_learning
context['human_readable'] = human_readable


def home(request):
    context['parent_discipline'] = parent_discipline
    return render(request, 'home.html', context)

def why(request):
    return render(request,'why.html', context)

def discipline_detail(request, discipline_slug):
    discipline = get_object_or_404(Discipline, slug=discipline_slug)
    subdisciplines = Discipline.objects.filter(parents=discipline)
    context['discipline'] = discipline
    context['subdisciplines'] = subdisciplines
    return render(request, 'discipline_detail.html',context)

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    works = Work.objects.filter(authors__id=person.id)
    context['person']= person
    context['works'] = works
    context['neural_models'] = neural_models
    return render(request, 'person_detail.html',context)


def search(request):
    query = request.GET.get('query', '')
    discipline_results = Discipline.objects.filter(title__icontains=query)
    person_results = Person.objects.filter(last_name__icontains=query)
    context['discipline_results'] = discipline_results
    context['person_results'] = person_results
    context['query'] = query
    return render(request, 'search_results.html', context)

