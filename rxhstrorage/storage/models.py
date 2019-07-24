import datetime

from django.db import models


# pos_choices = (('0', '上'), ('1', '中'), ('2', '下'))


# Create your models here.

class StorageRack(models.Model):
    '''货架表'''
    num = models.IntegerField(verbose_name='货架号')

    # pos = models.CharField(verbose_name='位置', choices=pos_choices, default='0',max_length=10)

    # pos=mode
    def __str__(self):
        return f'货架{self.num}'


class Position(models.Model):
    '''位置表'''
    name = models.CharField(verbose_name='位置', max_length=10)

    def __str__(self):
        return self.name


#
# class Sto2Pos(models.Model):
#     '''货架和位置多对多关系表'''
#     sto = models.ForeignKey(to='StorageRack', )
#     pos = models.ForeignKey(to='Position', )
#
#     def __str__(self):
#         return f'{self.sto}{self.pos}'
#
#     class Meta:
#         '''联合唯一'''
#         unique_together = ('sto', 'pos')


class MaterialCls(models.Model):
    '''分类表'''
    name = models.CharField(verbose_name='原料类别', max_length=108)

    def __str__(self):
        return self.name


class Material(models.Model):
    '''原材料表'''
    name = models.CharField(verbose_name='原材料名称', max_length=256, )
    amount = models.DecimalField(verbose_name='数量', max_digits=6, decimal_places=2)
    storage = models.ForeignKey(verbose_name='货架', to='StorageRack')
    pos = models.ForeignKey(verbose_name='位置', to='Position')
    cls = models.ForeignKey(verbose_name='原料类别', to='MaterialCls', default=1)
    update_data = models.DateTimeField(verbose_name='数据变更时间', auto_now=True, null=True)

    def __str__(self):
        return self.name
