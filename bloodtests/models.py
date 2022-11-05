from django.db import models
from django.db.models import CheckConstraint, Q


class TestResult(models.Model):
    """
    code - varchar up to 4 characters in length
    name - varchar up to 100 characters in length
    unit - varchar up to 10 characters in length
    lower - positive float
    upper - positive float

    lower or upper can be null but not both.
    If both are non null then require upper > lower.
    """
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    lower = models.FloatField(null=True, blank=True, default=None)
    upper = models.FloatField(null=True, blank=True, default=None)

    class Meta:
        db_table = "bloodtests_testresult"
        constraints = (
            CheckConstraint(
                check=Q(lower__gte=0.0),
                name='lower_range_constraint'),
            CheckConstraint(
                check=Q(upper__gte=0.0),
                name='upper_range_constraint'),
            # CheckConstraint(
            #     check=Q(upper__isnull=False) | Q(lower__isnull=False),
            #     name='not_both_null_allowed_constraint'
            # )
        )


class Test(TestResult):
    pass
