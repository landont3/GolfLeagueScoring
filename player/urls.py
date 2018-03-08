from django.urls import path

from .views import welcome, score_entry, enter_scores, edit_scores, list_scores, score_edit


urlpatterns = [
    path('', welcome, name='player_home'),
    path('scores', score_entry, name='score_entry'),
    path('score_detail', enter_scores, name='enter_scores'),
    path('score_detail/<int:player_round_id>', score_edit, name='score_edit'),
    path('list_scores', list_scores, name='list_scores'),
    path('edit_scores/<int:week_id>', edit_scores, name='edit_scores')
]
