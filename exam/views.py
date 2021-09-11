from django.shortcuts import render
from .models import *
import time
from django.db.models import Min

def get_prev_id(curr_id):
    try:
        ret_id = Question.objects.filter(id__lt=curr_id).order_by("-id")[0:1].get().id
    except Question.DoesNotExist:
        ret_id = Question.objects.aggregate(Min("id"))['id__min']
    return ret_id

def get_next_id(curr_id):
    try:
        ret_id = Question.objects.filter(id__gt=curr_id).order_by("id")[0:1].get().id
    except Question.DoesNotExist:
        ret_id = Question.objects.aggregate(Min("id"))['id__min']
    return ret_id

def welcome(request):
    questions = Question.objects.all()
    context = {
        'session_id': int(time.time()),
        'questions': questions,
        'next_question_id': get_next_id(questions.first().id)
    }
    return render(request, 'welcome.html', context)

def next(request):
    if request.is_ajax():
        question = Question.objects.get(pk=request.GET.get('current'))

        previous_id = get_prev_id(question.id)
        if request.GET.get('answer')=='yes':
            previous_id = request.GET.get('current')

        print(previous_id, request.GET.get('session'), request.GET.get("answer"))
        if request.GET.get("answer") != "yes":
            if request.GET.get("finish") == 'on':
                que = Question.objects.get(id=5)
                answer, created =Answer.objects.get_or_create(question=que, user_session=request.GET.get('session'))
                answer.answer = request.GET.get("answer")
                answer.save()
            else:
            # print(request.GET.get("answer"), question.id, question.question)
            # print("answer ", request.GET.get("answer"))
                que = Question.objects.get(id=previous_id)
                answer, created =Answer.objects.get_or_create(question=que, user_session=request.GET.get('session'))
                answer.answer = request.GET.get("answer")
                answer.save()
        
        context = {
            'total': Question.objects.all().count(),
            'previous': previous_id,
            'current': get_next_id(question.id),
            'question': question,
            'range': range(question.rating) if question.types==1 else None
        }
        return render(request, 'finish.html') if bool(request.GET.get('finish')) else render(request, 'container.html', context)
