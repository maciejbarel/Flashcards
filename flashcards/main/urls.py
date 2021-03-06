from django.conf.urls import url, include
from . import views


urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^flashcards/(?P<pk>\d+)/', views.FlashcardsView.as_view(), name='flashcards'),
    url(r'^play/(?P<pk>\d+)/$', views.PlayView.as_view(), name='play'),
    url(r'^flashcard/(?P<pk>\d+)/(?P<grade>\d+)/$', views.NewIntervalView.as_view()),
    url(r'^flashcard/delete/(?P<pk>\d+)/$', views.FlashcardDeleteView.as_view(), name='delete_flashcard'),
    url(r'^flashcard/edit/(?P<pk>\d+)/$', views.FlashcardEditView.as_view(), name='edit_flashcard'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^(flashcards|play)/$', views.DeckChoiceView.as_view(), name='deck_choice'),
]