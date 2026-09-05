from tortoise import fields, models
from tortoise.migrations.constraints import UniqueConstraint


class BoardGameRank(models.Model):
    id = fields.IntField(pk=True, null=False, generated=True)
    bggid = fields.IntField(null=False)
    name = fields.CharField(max_length=50, null=False)
    yearpublished = fields.IntField(null=False)
    rank = fields.IntField(null=False)
    bayesaverage = fields.DecimalField(max_digits=6, decimal_places=5, null=False)
    average = fields.DecimalField(max_digits=6, decimal_places=5, null=False)
    usersrated = fields.IntField(null=False)
    isexpansion = fields.BooleanField(null=False)


    class Meta:
        table = 'bgrank'
        schema = 'bgg'
        constraints = [
            UniqueConstraint(fields=('bggid', ), name='uq_bgrank')
        ]