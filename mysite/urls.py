"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from polls import views


# 2번째 인자는 입력 URL을 처리할 함수를 명시 (View에 있음)
# urlpattern을 명시할 때는 순서도 중요 ( 위에서 순서대로 찾기 때문에 )
urlpatterns = [                                     # 이게 등록되어 있어서 admin page를 열 수 있었던 것
    path('admin/', admin.site.urls),
    path('polls/', include("polls.urls"))                            # 모든 투표질문을 화면에 출력
]
# 모든 url을 한 곳에서 관리하기 보다는 app별로 관리하는 것이 나음 (include 사용)