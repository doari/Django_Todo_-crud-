from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)         # 할 일의 제목
    description = models.TextField(blank=True)       # 할 일의 설명 (빈칸 가능)
    completed = models.BooleanField(default=False)   # 완료 여부

    def __str__(self):
        return self.title   # 이 객체를 문자열로 표현할 때 title을 사용
