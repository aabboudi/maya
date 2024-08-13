from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from content.models import *
from executive.models import *

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about/about.html')

def partners(request):
    return render(request, 'about/partners.html')

def leadership(request):
    board_members = BoardMember.objects.filter(active=True)
    managers = Manager.objects.filter(active=True)
    return render(request, 'about/leadership.html', { 'board_members': board_members, 'managers': managers })

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
    programs_with_image = []
    programs = Program.objects.prefetch_related('goals').filter(active=True)

    for program in programs:
        goal = program.goals.first()
        bgimage_url = goal.image.url if goal and goal.image else None
        programs_with_image.append({
            'program': program,
            'bgimage_url': bgimage_url,
        })

    return render(request, 'programs/programs.html', { 'programs': programs_with_image })


def program_details(request, program: str):
    program = get_object_or_404(Program, slug=program)
    goals = program.goals.all()

    sample_events = [
        {
            'icon': 'atlassian.svg',
            'bgcolor': 'bg-blue-600',
            'color': 'blue',
            'category': 'Atlassian API',
            'title': 'Atlassian',
            'description': 'A software that develops products for software developers and developments.',
            'cta1': 'View Sample',
            'cta2': 'View API'
        },
        {
            'icon': 'asana.svg',
            'bgcolor': 'bg-rose-500',
            'color': 'rose',
            'category': 'Asana API',
            'title': 'Asana',
            'description': 'Track tasks and projects, use agile boards, measure progress.',
            'cta1': 'View Sample',
            'cta2': 'View API'
        },
        {
            'icon': 'slack.svg',
            'bgcolor': 'bg-amber-500',
            'color': 'amber',
            'category': 'Slack API',
            'title': 'Slack',
            'description': 'Email collaboration and email service desk made easy.',
            'cta1': 'View Sample',
            'cta2': 'View API'
        },
    ]
    return render(request, 'programs/program-details.html', { 'program': program, 'goals': goals, 'sample_events': sample_events })

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    faqs = FAQ.objects.all().order_by('-priority', '-created_at')
    return render(request, 'faq.html', { 'faqs': faqs })
