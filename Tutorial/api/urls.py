# encoding=utf-8

from django.urls import path

from api.views import QuestionDetail, QuestionList

urlpatterns = [
    path('polls/', QuestionList.as_view(), name='polls_list'),
    path('polls/<int:pk>', QuestionDetail.as_view(), name='polls_detail'),
]
