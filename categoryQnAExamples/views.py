from django.shortcuts import render

# Create your views here.

from .models import CategoryQnAExamples

def show_examples(request):
    question_ids = request.GET.getlist('question_ids')
    examples = CategoryQnAExamples.objects.filter(categoryQnA_id__id__in=question_ids)
    return render(request, 'admin/show_examples.html', {'examples': examples})
    # return render(request, 'admin/example.html')
