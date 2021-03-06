from django.urls import path
from . import views

app_name = 'botArena'
urlpatterns = [
    # ex: /botArena/
    path('', views.home, name='home'),
    # ex: /botArena/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /botArena/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /botArena/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login/', views.logging_test, name="login"),
    # path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'), # TODO delete
    path('registration/', views.registration, name='registration'),
    path('game/<str:name>', views.game, name='game'),
    path('new_game/', views.creating_game_view, name='new_game'),
    path('game/<str:name>/new_bot', views.creating_bot_view, name='new_bot')
]
