from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import PurchaseSerializer, AdditionSerializer
from customers.models import CustomUser
from finance.models import Purchase, Addition


# Create your views here.
class PurchaseViewSet(ReadOnlyModelViewSet):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if isinstance(user, CustomUser):
            return Purchase.objects.filter(user=user)
        return Purchase.objects.none()


class AdditionViewSet(ReadOnlyModelViewSet):
    serializer_class = AdditionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if isinstance(user, CustomUser):
            return Addition.objects.filter(user=user)
        return Addition.objects.none()
