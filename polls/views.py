from django.shortcuts import render, get_object_or_404
from polls.models import Question

# 클라이언트가 서버에 요청을 보내는 작업 => request
# 클라이언트가 서버에 요청을 보낼때 여러가지 정보가 같이 서버에 제공
# 이 내용을 request라는 객체로 만들어서 사용한다.
# 서버가 클라이언트에게 결과를 보내는 작업 => response
# 넣은 리스트 객체를 생성
def index(request):
    #로직처리 코드가 나와요!
    tmp = Question.objects.all().order_by('-pub_date')[:3]
    context = {"latest_question_list": tmp}
    return render(request, 'index.html', context)

def detail(request, question_id):
    # 로직처리 코드가 나와요!
    # 아까는 모든 Question객체를 다 구해서 리스트로 만들었는데, 이번에는 특정 Question 객체 하나만 구해야 한다
    tmp = get_object_or_404(Question, pk=question_id)        # pk 는 primary key를 의미
    context = {"question": tmp}
    return render(request, 'detail.html', context)

def vote(request, bbb):
    # 넘어온 데이터(bbb)는 Question 객체의 id가 넘어 왔다.
    question = get_object_or_404(Question, pk=bbb)
    # request header 안에 form에서 선택한 데이터가 포함되서 전달되고 이것을 추출하기 위해서 request.POST["choice"] 를 사용
    selected_choice = question.choice_set.get(pk=request.POST["choice"])

    selected_choice.votes += 1
    selected_choice.save()

    context = {"vote_list": question}

    # result.html에서 현재 투표항목에 대한 각 항목들의 투표현황을 출력
    return render(request, 'result.html', context)