from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
# from django.http import Http404
from content.models import *
from executive.models import *

def home(request):
    return render(request, 'index.html')

def mission_and_vision(request):
    return render(request, 'about/mission-and-vision.html')

def partners(request):
    return render(request, 'about/partners.html')

def leadership(request):
    board_members = BoardMember.objects.filter(active=True)
    managers = Manager.objects.filter(active=True)
    return render(request, 'about/leadership.html', { 'board_members': board_members, 'managers': managers })

def stories(request):
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

from decouple import config

def contact(request):
    if request.method == "POST":
        body = {key: request.POST.get(key) for key in [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'message']}

        message = "\n".join(f"{ key }: { value }" for key, value in body.items())
        recipient_email = config('EMAIL_HOST_USER')

        try:
            if (send_mail(
                subject="From Contact Page",
                message=message,
                from_email="Contact Form",
                recipient_list=[recipient_email],
                fail_silently=False)):

                send_mail(
                subject="Your Email is Well Received",
                message=f"Dear {body["first_name"]},\n\nWe have received your email and will be in touch shortly. Thank you!\n\nThe YES Alumni Morocco Team",
                from_email=f"YES Alumni Morocco <{recipient_email}>",
                recipient_list=[body["email"]],
                fail_silently=False)

                request.session['message_sent_flag'] = True

            return render(request, 'contact/message-sent.html')

        except Exception:
            return render(request, 'contact/contact.html', { "error": "Failed to send email. Please try again later." })

    return render(request, 'contact/contact.html')

def faq(request):
    faqs = FAQ.objects.all().order_by('-priority', '-created_at')
    return render(request, 'contact/faq.html', { 'faqs': faqs })

def message_sent(request):
    if request.session.get('message_sent_flag'):
        del request.session['message_sent_flag']
        return render(request, 'contact/message-sent.html')
    else:
        # raise Http404("Page not found")
        return redirect('/')
