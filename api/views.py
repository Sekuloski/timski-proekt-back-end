import csv

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import PurchaseSerializer, AdditionSerializer
from customers.models import CustomUser
from finance.models import Purchase, Addition, ExpenseType, ADDITION_TYPES


# Create your views here.

@api_view(['POST'])
def upload_purchases_from_csv(request):
    """
    /purchase/upload

    <form method="post" enctype="multipart/form-data">
        <input type="file" name="purchases">
        <button type="submit">Upload File</button>
    </form>
    """
    if request.user.is_authenticated:
        try:
            file = request.FILES['purchases']

        except KeyError:
            return HttpResponse('File was not attached!', status=400)

        if not file.name.endswith('csv'):
            return HttpResponse('File is not csv format!', status=400)

        user_id = request.user.id
        data = file.read().decode('UTF-8').split('\r\n')
        csv_reader = csv.reader(data, delimiter=',', quotechar='|')
        for column in csv_reader:
            try:
                expense_type = ExpenseType.objects.get(name__exact=column[3])
            except ObjectDoesNotExist:
                expense_type = ExpenseType(name=column[3])
                expense_type.save()
            Purchase(
                user=CustomUser.objects.get(pk=int(user_id)),
                amount=column[0],
                description=column[1],
                date=column[2],
                expense_type=expense_type
            ).save()

        return HttpResponse('Purchases added!', status=200)

    else:
        return HttpResponse('User not logged in!', status=401)


@api_view(['POST'])
def upload_additions_from_csv(request):
    """
    /addition/upload

    <form method="post" enctype="multipart/form-data">
        <input type="file" name="additions">
        <button type="submit">Upload File</button>
    </form>
    """
    if request.user.is_authenticated:
        try:
            file = request.FILES['additions']

        except KeyError:
            return HttpResponse('File was not attached!', status=400)

        if not file.name.endswith('csv'):
            return HttpResponse('File is not csv format!', status=400)

        user_id = request.user.id
        data = file.read().decode('UTF-8').split('\r\n')
        csv_reader = csv.reader(data, delimiter=',', quotechar='|')
        for column in csv_reader:
            Addition(
                user=CustomUser.objects.get(pk=int(user_id)),
                amount=column[0],
                description=column[1],
                date=column[2],
                addition_type=int(column[3])
            ).save()

        return HttpResponse('Additions added!', status=200)
    else:
        return HttpResponse('User not logged in!', status=401)


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
