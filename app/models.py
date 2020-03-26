from django.db import models

class Item(models.Model):
    # TODO: Define fields here
    no = models.IntegerField('no', blank=True, null=True)
    name = models.CharField('name', blank=True, max_length=100)
    CATEGORY = (
        ('0', 'シューター'),
        ('1', 'マニューバー'),
        ('2', 'ブラスター'),
        ('3', 'スピナー'),
        ('4', 'ローラー'),
        ('5', 'フデ'),
        ('6', 'チャージャー'),
        ('7', 'スロッシャー'),
        ('8', 'シェルター'),
        ('9', 'ガイザー'),
    )
    category = models.CharField(blank=True, max_length=2, choices=CATEGORY)
    gauge = models.IntegerField('gauge', blank=True, null=True)
    release_condition = models.CharField('release_condition', blank=True, max_length=100)
    range = models.IntegerField('range', blank=True, null=True)
    continuous_power = models.IntegerField('continuous_power', blank=True, null=True)
    fixed_num = models.IntegerField('fixed_num', blank=True, null=True)
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'ブキ'
        verbose_name_plural = 'ブキ一覧'

    def __str__(self):
        return self.name
