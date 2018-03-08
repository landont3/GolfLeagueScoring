from django.urls import path


from .views import welcome, week_list, match_list, match_edit


urlpatterns = [
    path('', welcome, name='match_home'),
    path('week', week_list, name='week_list'),
    path('week/<int:week_id>', match_list, name='match_list'),
    path('edit/<int:match_id>', match_edit, name='match_edit')
]
