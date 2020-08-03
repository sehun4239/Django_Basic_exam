from django.contrib import admin
from polls.models import Question, Choice

# 괄호안에는 내가 등록할 클래스가 나와야 한다.
admin.site.register(Question)
admin.site.register(Choice)

# 먼저 DB를 만들어야함 Terminal에 python manage.py makemigrations를 침