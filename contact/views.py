from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def contact_api(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        data = serializer.validated_data

        send_mail(
            subject=f"New Portfolio Contact from {data['name']}",
            message=data['message'],
            from_email=None,
            recipient_list=['abiabinaya03m@gmail.com'],
            fail_silently=True,
        )

        return Response(
            {"success": True, "message": "Message sent successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
