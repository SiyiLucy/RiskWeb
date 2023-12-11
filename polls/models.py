from django.db import models
from sklearn import svm
import numpy as np
import pandas as pd

class StudentInfo(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=20)
    stu_name = models.CharField(max_length=20)
    stu_psw = models.CharField(max_length=20)

class sale(models.Model):
    goodsID = models.CharField(primary_key=True, max_length=20)
    goodsA = models.CharField(max_length=20)
    goods1 = models.CharField(max_length=20)
    goodsB = models.CharField(max_length=20)
    goods2 = models.CharField(max_length=20)

class score(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')

class RankingManager(models.Manager):
    def get_last_row_id(self):
        last_row = self.order_by('-id').first()
        if last_row:
            return last_row.id
        else:
            return None

class Newrank(models.Model):
    droppable1Content = models.CharField(max_length=20)
    droppable2Content = models.CharField(max_length=20)
    droppable3Content = models.CharField(max_length=20)
    droppable4Content = models.CharField(max_length=20)
    droppable5Content = models.CharField(max_length=20)
    droppable6Content = models.CharField(max_length=20)
    droppable7Content = models.CharField(max_length=20)
    droppable8Content = models.CharField(max_length=20)
    droppable9Content = models.CharField(max_length=20)
    droppable10Content = models.CharField(max_length=20)
    objects = RankingManager()

    @classmethod
    def count_non_empty_values(self):
        non_empty_values = 0
        Newrank = self.objects.order_by('-id')[:1]

        if Newrank:
            rank = Newrank[0]
            if rank.droppable1Content:
                non_empty_values += 1
            if rank.droppable2Content:
                non_empty_values += 1
            if rank.droppable3Content:
                non_empty_values += 1
            if rank.droppable4Content:
                non_empty_values += 1
            if rank.droppable5Content:
                non_empty_values += 1
            if rank.droppable6Content:
                non_empty_values += 1
            if rank.droppable7Content:
                non_empty_values += 1
            if rank.droppable8Content:
                non_empty_values += 1
            if rank.droppable9Content:
                non_empty_values += 1
            if rank.droppable10Content:
                non_empty_values += 1
        return non_empty_values

    def calculate_weights(self,Newrank):
        weights = []
        total_weight = 0.0
        for i in range(1, Newrank + 1):
            weight = 1 / i
            weights.append(weight)
            total_weight += weight
        # 归一化权重
        weights = [weight / total_weight for weight in weights]
        return weights

class match(models.Model):
    match1Content = models.CharField(max_length=20)
    match2Content = models.CharField(max_length=20)
    match3Content = models.CharField(max_length=20)
    match4Content = models.CharField(max_length=20)
    match5Content = models.CharField(max_length=20)
    match6Content = models.CharField(max_length=20)
    match7Content = models.CharField(max_length=20)
    match8Content = models.CharField(max_length=20)
    match9Content = models.CharField(max_length=20)
    match10Content = models.CharField(max_length=20)
    level1Content = models.CharField(max_length=20)
    level2Content = models.CharField(max_length=20)
    level3Content = models.CharField(max_length=20)
    level4Content = models.CharField(max_length=20)
    level5Content = models.CharField(max_length=20)
    level6Content = models.CharField(max_length=20)
    level7Content = models.CharField(max_length=20)
    level8Content = models.CharField(max_length=20)
    level9Content = models.CharField(max_length=20)
    level10Content = models.CharField(max_length=20)

class mark(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')


class Newmatch(models.Model):
    match1Content = models.CharField(max_length=20)
    match2Content = models.CharField(max_length=20)
    match3Content = models.CharField(max_length=20)
    match4Content = models.CharField(max_length=20)
    match5Content = models.CharField(max_length=20)
    match6Content = models.CharField(max_length=20)
    match7Content = models.CharField(max_length=20)
    match8Content = models.CharField(max_length=20)
    match9Content = models.CharField(max_length=20)
    match10Content = models.CharField(max_length=20)
    level1Content = models.CharField(max_length=20)
    level2Content = models.CharField(max_length=20)
    level3Content = models.CharField(max_length=20)
    level4Content = models.CharField(max_length=20)
    level5Content = models.CharField(max_length=20)
    level6Content = models.CharField(max_length=20)
    level7Content = models.CharField(max_length=20)
    level8Content = models.CharField(max_length=20)
    level9Content = models.CharField(max_length=20)
    level10Content = models.CharField(max_length=20)

    @staticmethod
    def get_last_row_id():
        last_row = Newmatch.objects.last()
        if last_row:
            return last_row.id
        return None
class code(models.Model):
    code1Content = models.CharField(max_length=20)
    code2Content = models.CharField(max_length=20)
    code3Content = models.CharField(max_length=20)
    code4Content = models.CharField(max_length=20)
    code5Content = models.CharField(max_length=20)
    code6Content = models.CharField(max_length=20)
    code7Content = models.CharField(max_length=20)
    code8Content = models.CharField(max_length=20)
    code9Content = models.CharField(max_length=20)
    code10Content = models.CharField(max_length=20)
    @staticmethod
    def get_last_row_id():
        last_row = code.objects.last()
        if last_row:
            return last_row.id
        return None
class Newmark(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')
    x16 = models.CharField(max_length=100, default='default_value')
    x17 = models.CharField(max_length=100, default='default_value')
    x18 = models.CharField(max_length=100, default='default_value')
    x19 = models.CharField(max_length=100, default='default_value')


class Newmark1(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')
    x16 = models.CharField(max_length=100, default='default_value')
    x17 = models.CharField(max_length=100, default='default_value')
    x18 = models.CharField(max_length=100, default='default_value')
    x19 = models.CharField(max_length=100, default='default_value')


class Newmark2(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')
    x16 = models.CharField(max_length=100, default='default_value')
    x17 = models.CharField(max_length=100, default='default_value')
    x18 = models.CharField(max_length=100, default='default_value')
    x19 = models.CharField(max_length=100, default='default_value')


class Newmark3(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')
    x16 = models.CharField(max_length=100, default='default_value')
    x17 = models.CharField(max_length=100, default='default_value')
    x18 = models.CharField(max_length=100, default='default_value')
    x19 = models.CharField(max_length=100, default='default_value')


class Newmark4(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')
    x16 = models.CharField(max_length=100, default='default_value')
    x17 = models.CharField(max_length=100, default='default_value')
    x18 = models.CharField(max_length=100, default='default_value')
    x19 = models.CharField(max_length=100, default='default_value')
class Newmark5(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')
    x16 = models.CharField(max_length=100, default='default_value')
    x17 = models.CharField(max_length=100, default='default_value')
    x18 = models.CharField(max_length=100, default='default_value')
    x19 = models.CharField(max_length=100, default='default_value')
class Newmark6(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')
    x16 = models.CharField(max_length=100, default='default_value')
    x17 = models.CharField(max_length=100, default='default_value')
    x18 = models.CharField(max_length=100, default='default_value')
    x19 = models.CharField(max_length=100, default='default_value')

class Newmark7(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')
    x16 = models.CharField(max_length=100, default='default_value')
    x17 = models.CharField(max_length=100, default='default_value')
    x18 = models.CharField(max_length=100, default='default_value')
    x19 = models.CharField(max_length=100, default='default_value')

class Newmark8(models.Model):
    x1 = models.CharField(max_length=100, default='default_value')
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')
    x16 = models.CharField(max_length=100, default='default_value')
    x17 = models.CharField(max_length=100, default='default_value')
    x18 = models.CharField(max_length=100, default='default_value')
    x19 = models.CharField(max_length=100, default='default_value')

class score1(models.Model):
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')
class score2(models.Model):
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')

class score3(models.Model):
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')

class score4(models.Model):
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')

class score5(models.Model):
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')

class score6(models.Model):
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')

class score7(models.Model):
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')

class score8(models.Model):
    x2 = models.CharField(max_length=100, default='default_value')
    x3 = models.CharField(max_length=100, default='default_value')
    x4 = models.CharField(max_length=100, default='default_value')
    x5 = models.CharField(max_length=100, default='default_value')
    x6 = models.CharField(max_length=100, default='default_value')
    x7 = models.CharField(max_length=100, default='default_value')
    x8 = models.CharField(max_length=100, default='default_value')
    x9 = models.CharField(max_length=100, default='default_value')
    x10 = models.CharField(max_length=100, default='default_value')
    x11 = models.CharField(max_length=100, default='default_value')
    x12 = models.CharField(max_length=100, default='default_value')
    x13 = models.CharField(max_length=100, default='default_value')
    x14 = models.CharField(max_length=100, default='default_value')
    x15 = models.CharField(max_length=100, default='default_value')

class result(models.Model):
    result_score= models.CharField(max_length=100, default='default_value')

class newresult(models.Model):
    begin_score= models.CharField(max_length=100, default='default_value')
    end_score = models.CharField(max_length=100, default='default_value')
    @staticmethod
    def get_last_row_id():
        last_row = newresult.objects.last()
        if last_row:
            return last_row.id
        return None