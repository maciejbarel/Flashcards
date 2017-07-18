import datetime

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.utils.timezone import now

from .forms import FlashcardForm
from .models import Flashcard


class MainView(View):

    def get(self, request):
        if request.user.is_authenticated:
            username = " ".join([request.user.first_name, request.user.last_name])
            return render(request, "main/index.html", {'username': username})
        else:
            return render(request, "main/index.html")


class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        return redirect('main')


class FlashcardsView(LoginRequiredMixin, View):

    def get(self, request):
        form = FlashcardForm()
        user = User.objects.get(username=request.user.get_username())
        flashcards = Flashcard.objects.filter(user=user)
        username = " ".join([request.user.first_name, request.user.last_name])
        ctx = {'flashcards': flashcards, 'form': form, 'username': username}
        return render(request, 'main/flashcards.html', ctx)

    def post(self, request):
        form = FlashcardForm(request.POST)

        if form.is_valid():
            flashcard = form.save(commit=False)
            user = User.objects.get(username=request.user.get_username())
            flashcard.user = user
            flashcard.save()

        return redirect('flashcards')


class PlayView(LoginRequiredMixin, View):

    def get(self, request):
        query = Flashcard.objects.filter(user=request.user, repeat__lte=datetime.datetime.now()).order_by('repeated')
        username = " ".join([request.user.first_name, request.user.last_name])
        if query:
            return render(request, 'main/play.html', {'flashcard': query[0], 'username': username})
        else:
            return render(request, 'main/play.html', {'username': username})


class NewIntervalView(LoginRequiredMixin, View):

    """
    Implement Supermemo 2 algorithm (based on https://www.supermemo.com/english/ol/sm2.htm).
    """

    def get(self, request, id, grade):
        flashcard = Flashcard.objects.get(id=id)
        grade = int(grade)
        if grade < 3:
            flashcard.interval = 1
        else:
            if not flashcard.repeated:
                if flashcard.interval == 1:
                    flashcard.interval = 6
                else:
                    flashcard.interval = flashcard.interval * flashcard.ef
                flashcard.ef = flashcard.ef + (0.1 - (5-grade)*(0.08 + (5-grade)*0.02))
        flashcard.repeated = True

        if grade == 5:
            flashcard.repeat = now().date() + datetime.timedelta(days=flashcard.interval)
            flashcard.repeated = False

        flashcard.save()

        return redirect('play')


