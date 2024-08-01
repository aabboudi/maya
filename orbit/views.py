from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from content.models import *

def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def about(request):
    return render(request, 'about.html')

def stories(request):
    # stories = Post.objects.all()
    posts_with_images = []
    for post in Post.objects.all():
        first_image = post.images.first()
        posts_with_images.append({
            'post': post,
            'first_image': first_image,
            'authors': post.author.all(),
        })
    return render(request, 'stories/stories.html', { 'stories': posts_with_images })

def story_details(request, story: str):
    story = get_object_or_404(Post, slug=story)
    images = story.images.all()
    return render(request, 'stories/story.html', { 'story': story, 'images': images })

def programs(request):
    programs = Program.objects.all()
    return render(request, 'programs/programs.html', { 'programs': programs })

def program_details(request, program: str):
    program = get_object_or_404(Program, slug=program)
    return render(request, 'programs/program-details.html', { 'program': program })

def partners(request):
    return render(request, 'partners.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')
