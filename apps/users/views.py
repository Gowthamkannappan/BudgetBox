from rest_framework import generics
# The generics module provides generic class-based views.
from rest_framework.response import Response
#Response class is used to create the HTTP response for the view.
from rest_framework.permissions import IsAuthenticated

from rest_framework.parsers import MultiPartParser, FormParser   
# MultiPartParser and FormParser classes are imported to parse the request data that may include multipart form data (such as a file upload).


from .models import User
from .serializers import UserSerializer, UserSignInSerializer, UserSignUpSerializer

class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

class UserSignIn(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer

class UserProfile(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class UserProfileUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)