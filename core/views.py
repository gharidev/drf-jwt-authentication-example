from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .permissions import AllowInternalUsers


class HelloView(APIView):
    permission_classes = (AllowInternalUsers,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
