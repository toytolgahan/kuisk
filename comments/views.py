from django.shortcuts import render
from .forms import CommentForm

# Create your views here.

def send_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return render(request, 'comment_success.html')
    else:
        form = CommentForm()

    return render(request, 'send_comment.html',{'form':form})