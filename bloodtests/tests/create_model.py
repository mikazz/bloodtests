from bloodtests.models import TestResult
import pytest
import json
from rest_framework import status
from rest_framework.test import APIClient
from bloodtests.models import Test


@pytest.fixture()
def request_client():
    client = APIClient()
    return client
#
#
# @pytest.mark.django_db()
# class TestBloodTests():
#     apipath = '/api/bloodtests/test/'
#
#     def test_method_post(self, request_client):
#         #TestResult(**{'code': 'CHO1', 'name': 'Cholesterol', 'unit': 'g/M', 'upper': 99, 'lower': 45}).save()
#         TestResult(**{'code': 'CHO1', 'name': 'Cholesterol', 'unit': 'g/M', 'upper': 99, 'lower': 45}).save()
#
from bloodtests.serializers import TestResultSerializer


@pytest.mark.django_db()
class TestBloodTests():
    apipath = '/api/bloodtests/test/'

    def test_serializer(self, request_client):
        #data = {'code': 'CHO1', 'name': 'Cholesterol', 'unit': 'g/M', 'upper': 99}
        #data = {'code': 'CHO1', 'name': 'Cholesterol', 'unit': 'g/M', 'lower': 99, 'upper':203}
        #data = {'code': 'CHO1', 'name': 'Cholesterol', 'unit': 'g/M'}
        #data = {'code': 'CHO1', 'name': 'Cholesterol', 'unit': 'g/M', 'lower': 50, 'upper': 30}
        data = {'code': 'CHO', 'name': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'unit': 'g/M', 'lower': 99}
        serializer = TestResultSerializer(data=data)
        print(serializer.is_valid())
        serializer.save()

    def test_model(self, request_client):
        #TestResult(**{'code': 'CHO1', 'name': 'Cholesterol', 'unit': 'g/M', 'upper': 99, 'lower': 45}).save()
        TestResult(**{'code': 'CHO1', 'name': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'unit': 'g/M', 'upper': 99, 'lower': 45}).save()
