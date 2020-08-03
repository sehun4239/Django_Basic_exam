from django.urls import path
from . import views


app_name = "polls"


urlpatterns = [                                     # 이게 등록되어 있어서 admin page를 열 수 있었던 것
    path('', views.index, name="index" ),            # localhost:8000/polls # 모든 투표질문을 화면에 출력
    path('<int:question_id>/', views.detail, name="detail"),             # localhost:8000/polls/<숫자>
    path('<int:bbb>/vote/', views.vote, name="vote"),
]
