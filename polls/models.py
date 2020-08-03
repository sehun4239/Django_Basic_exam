from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)        # 컬럼을 설정해주는 것: CharField 는 문자열을 지칭함
    pub_date = models.DateTimeField("date published")       # date published는 코멘트같은 것

    # def __repr__(self):         # repr은 객체를 임의로 특정 문자열로 표현하고 싶을때 사용 (연산 x)
    def __str__(self):            # str은 일반적으로 연산을 위해서 문자열로 바꾸고 싶을때 사용
        return self.question_text

    # id = models.IntegerField         << 얘는 안 써도 됨 왜냐?
    # Table의 id column은 default로 지정된다 ! id가 primary key, Not Null, Unique (없는게 없고, 겹치는 경우가 없어 id로 모두 식별 가능)
    # id는 authoincrement 특성을 가지는 정수형으로 지정되어 있다. 자동으로 생성해주기 때문에 class 정의에서 나오지 않는다.

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey는 특정 테이블의 프라이머리키를 가리키는 키
    # question_id라고 안 쓰는 이유는 애초에 foreignKey를 붙여버리면 _id가 뒤에 붙어서 question_id가 만들어짐
    # Question relation에서 id가 사라진다면  CASCADE를 써서 연관된 것을 싹다 지우게 한다. (연결된 것들)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)              # 초기 값이 0으로 세팅됨

    def __str__(self):
        return self.choice_text