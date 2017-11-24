from threading import Thread

from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse

from app.maze import gen_output
from app.models import Submission


def home_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        if request.POST['tab-select'] == 'register':
            user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['pass'])
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            raise PermissionDenied
        return redirect(reverse('home'))
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def about_view(request):
    return render(request, 'about.html')


def maze_demo(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            raise PermissionDenied
        submission = Submission.objects.create(user=request.user, lang=request.POST['lang'], code=request.POST['code'])
        Thread(target=gen_output, args=(submission.pk, submission.code, submission.lang)).start()
        return redirect(reverse('submission', kwargs={'pk': submission.pk}))
    return render(request, 'maze.html')


def submission_display(request, pk):
    return render(request, 'submission.html', context={
        'submission': Submission.objects.get(pk=pk)
    })