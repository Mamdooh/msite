from django.shortcuts import render
from .utils import get_magic8ball_answer


def home(request):
    """
    Render the homepage with welcoming content.
    """
    context = {
        'title': 'Welcome to msite',
    }
    return render(request, 'home.html', context)


def magic8ball(request):
    """
    Handle magic 8-ball predictions.
    GET: Display form
    POST: Return prediction based on question hash
    """
    context = {
        'title': 'Magic 8-Ball',
        'answer': None,
        'question': None,
    }

    if request.method == 'POST':
        question = request.POST.get('question', '').strip()
        if question:
            answer = get_magic8ball_answer(question)
            context['answer'] = answer
            context['question'] = question

    return render(request, 'magic8ball.html', context)
