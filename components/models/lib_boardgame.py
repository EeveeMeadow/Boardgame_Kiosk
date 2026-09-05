from enum import IntEnum

from tortoise import fields, models
from tortoise.fields import Now
from tortoise.migrations.constraints import UniqueConstraint


class BoardGameQuality(IntEnum):
    Unknown = 0
    MissingParts = 1
    Damaged = 2
    Worn = 3
    WellLoved = 4
    GoodAsNew = 5
    Unopened = 6

class BoardGame(models.Model):
    id = fields.IntField(pk=True, null=False, generated=True)
    owner = fields.DecimalField(max_digits=20, decimal_places=0, null=False)
    name = fields.CharField(max_length=50, null=False)
    description = fields.CharField(max_length=2500, null=True)
    quality = fields.IntEnumField(enum_type=BoardGameQuality, default=BoardGameQuality.Unknown, null=False)
    user_rating = fields.DecimalField(max_digits=3, decimal_places=1, null=True)
    thumbnail = fields.BinaryField(null=True)
    bgg_id = fields.IntField(null=True)
    private = fields.BooleanField(db_default=False, default=False, null=False)
    created = fields.DatetimeField(db_default=Now(), auto_now_add=True, null=True)
    copies = fields.SmallIntField(default=1, db_default=1, null=False)

    class Meta:
        table = 'usergame'
        schema = 'lib'
        constraints = [
            UniqueConstraint(fields=('owner', 'name'), name='uq_usergame_name')
        ]