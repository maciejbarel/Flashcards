from django.conf.urls import url
from .views import MainView, FlashcardsListView, AddFlashcardView, PlayView, NewIntervalView


urlpatterns = [
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^flashcards/$', FlashcardsListView.as_view()),
    url(r'^flashcards/add/$', AddFlashcardView.as_view()),
    url(r'^play/$', PlayView.as_view(), name='play'),
    url(r'^flashcard/(?P<id>\d+)/(?P<grade>\d+)/$', NewIntervalView.as_view()),
]