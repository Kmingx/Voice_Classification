from django.db import models

# Create your models here.
#제목처럼 글자수의 길이가 제한된 텍스트는 CharField를 사용
#내용(content)처럼 글자수를 제한할 수 없는 텍스트는 위처럼 TextField를 사용
#성일시처럼 날짜와 시간에 관계된 속성은 DateTimeField를 사용
class Question(models.Model):
    subject = models.CharField(max_length=200)# 200자까지 가능하도록 max_length=200을 설정
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


class Menu(models.Model):
    menuName = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    content = models.TextField()
