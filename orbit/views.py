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
        print(first_image)
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
    program_with_image = []
    programs = Program.objects.prefetch_related('goals')

    for program in programs:
        goal = program.goals.first()
        bgimage_url = goal.image.url if goal and goal.image else None
        program_with_image.append({
            'program': program,
            'bgimage_url': bgimage_url,
        })

    return render(request, 'programs/programs.html', { 'programs': program_with_image })


def program_details(request, program: str):
    program = get_object_or_404(Program, slug=program)
    goals = program.goals.all()
    return render(request, 'programs/program-details.html', { 'program': program, 'goals': goals })

def partners(request):
    return render(request, 'partners.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')
