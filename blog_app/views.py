from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

from .models import Headline, Text
from .forms import HeadlineForm, DescriptionForm

def home(request):
    ''' The home page of the blog_app'''
    return render(request, 'blog_app/home.html')

def headlines(request):
    ''' The headlines for the blog_app'''
    headlines = Headline.objects.order_by('headline_text')
    context = {'headlines': headlines}
    return render(request, 'blog_app/headlines.html', context)

@login_required
def description(request, headline_id):
    ''' The description for the blog_app'''
    head = get_object_or_404(Headline, id=headline_id)
    description = head.text_set.order_by('-date_added')
    context = {'head':head, 'description':description}
    return render(request, 'blog_app/description.html', context)

@login_required
def new_headline(request):
    ''' Add a new headline '''
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = HeadlineForm()
    else:
        form = HeadlineForm(data=request.POST)
        if form.is_valid():
            new_headline = form.save(commit=False)
            new_headline.owner = request.user
            new_headline.save()
            return redirect('blog_app:headlines')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blog_app/new_headline.html', context)

@login_required
def new_description(request, headline_id):
    ''' Add a new description for a headline '''
    head = Headline.objects.get(id=headline_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = DescriptionForm()
    else:
        # POST data submitted; process data
        form = DescriptionForm(data=request.POST)
        if form.is_valid():
            new_description = form.save(commit=False)
            new_description.headline = head
            new_description.save()
            return redirect('blog_app:description', headline_id = headline_id)

    # Display a blank or invalid form
    context = {'head':head, 'form':form}
    return render(request, 'blog_app/new_description.html', context)

@login_required
def edit_description(request, description_id):
    '''Edit an exitsting description'''
    desc = Text.objects.get(id=description_id)
    head = desc.headline

    if head.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current description
        form = DescriptionForm(instance=desc)
    else:
        # POST data submitted; process data
        form = DescriptionForm(instance=desc, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:description', headline_id=head.id)

    context = {'desc':desc, 'head':head, 'form':form}
    return render(request, 'blog_app/edit_description.html', context)

