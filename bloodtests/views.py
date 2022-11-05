from django.http import Http404, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from bloodtests.models import TestResult
from bloodtests.serializers import TestResultSerializer


class TestDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, code):
        try:
            return TestResult.objects.get(code=code)
        except TestResult.DoesNotExist:
            raise Http404

    def get(self, request, code):
        entity = self.get_object(code)
        serialized = TestResultSerializer(entity)
        return JsonResponse(serialized.data, safe=False)

    def post(self, request, code):
        serializer = TestResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(len(TestResult.objects.all()))
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
