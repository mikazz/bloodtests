from rest_framework import serializers
from bloodtests.models import TestResult


class FieldsCannotBeNone(Exception):
    pass


class TestResultSerializer(serializers.ModelSerializer):
    ideal_range = serializers.SerializerMethodField()

    def get_ideal_range(self, data):
        if data.lower and not data.upper:
            return f"value >= {data.lower}"
        elif not data.lower and data.upper:
            return f"value <= {data.upper}"
        else:
            return f"{data.lower} <= value <= {data.upper}"

    class Meta:
        model = TestResult
        fields = [
            "code",
            "name",
            "unit",
            "ideal_range",
            'lower',
            'upper'
        ]
    def create(self, data) -> TestResult:
        """
            validation when creation
        """
        # if not data['code'].isalpha():
        #     raise serializers.ValidationError("Only alphanumeric")
        upper = data.get("upper", None)
        lower = data.get("lower", None)

        if upper and upper < 0 or lower and lower < 0:
            raise serializers.ValidationError("Only positive numbers for 'upper' and 'lower' allowed")
        if not upper and not lower:
            raise serializers.ValidationError("Lower and upper cannot both be null")
        if upper and lower:
            if not upper > lower:
                raise serializers.ValidationError("Lower value can't exceed upper value")
        return TestResult.objects.create(**data)
