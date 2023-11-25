from django.shortcuts import render
from .forms import QuestionPaperForm
from .models import Question
import random


# Create your views here.

def generate_question_paper(request):
    if request.method == 'POST':
        form = QuestionPaperForm(request.POST)

        if form.is_valid():
            total_marks = form.cleaned_data['total_marks']
            easy_percentage = form.cleaned_data['easy_percentage']
            medium_percentage = form.cleaned_data['medium_percentage']
            hard_percentage = form.cleaned_data['hard_percentage']

            # Fetch questions from the database
            all_questions = Question.objects.all()

            # Calculate the number of questions based on difficulty percentages
            easy_weightage = int((easy_percentage / 100) * total_marks)
            medium_weightage = int((medium_percentage / 100) * total_marks)
            hard_weightage = total_marks - easy_weightage - medium_weightage

            # Fetch questions for each difficulty level
            easy_questions = list(all_questions.filter(difficulty='Easy'))
            medium_questions = list(all_questions.filter(difficulty='Medium'))
            hard_questions = list(all_questions.filter(difficulty='Hard'))

            # Distribute the weightage among the available questions for each difficulty level
            selected_easy_questions = distribute_weightage(easy_questions, easy_weightage)
            selected_medium_questions = distribute_weightage(medium_questions, medium_weightage)
            selected_hard_questions = distribute_weightage(hard_questions, hard_weightage)

            # Combine the selected questions
            question_paper = selected_easy_questions + selected_medium_questions + selected_hard_questions

            # Calculate total marks based on the weightage of each question
            total_marks = sum(question.marks for question in question_paper)

            # Render the question paper
            context = {'question_paper': question_paper, 'total_marks': total_marks}
            return render(request, 'generator/question_paper.html', context)

    else:
        form = QuestionPaperForm()

    return render(request, 'generator/generate_question_paper.html', {'form': form})

def distribute_weightage(questions, weightage):
    selected_questions = []
    total_weightage = 0

    while total_weightage < weightage and questions:
        question = random.choice(questions)
        if total_weightage + question.marks <= weightage:
            selected_questions.append(question)
            total_weightage += question.marks
        questions.remove(question)

    return selected_questions