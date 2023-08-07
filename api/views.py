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
    if request.method == 'POST':
        try:
            file = request.FILES['purchases']

        except KeyError:
            return HttpResponse('File was not attached!', status=400)

        if not file.name.endswith('csv'):
            return HttpResponse('File is not csv format!', status=400)

        data = file.read().decode('UTF-8').split('\r\n')
        csv_reader = csv.reader(data, delimiter=',', quotechar='|')
        for column in csv_reader:
            try:
                expense_type = ExpenseType.objects.get(name__exact=column[4])
            except ObjectDoesNotExist:
                expense_type = ExpenseType(name=column[4])
                expense_type.save()
            Purchase(
                user=CustomUser.objects.get(pk=int(column[0])),
                amount=column[1],
                description=column[2],
                date=column[3],
                expense_type=expense_type
            ).save()

        return HttpResponse('Purchases added!', status=200)


@api_view(['POST'])
def upload_additions_from_csv(request):
    """
    /addition/upload

    <form method="post" enctype="multipart/form-data">
        <input type="file" name="additions">
        <button type="submit">Upload File</button>
    </form>
    """
    if request.method == 'POST':
        try:
            file = request.FILES['additions']

        except KeyError:
            return HttpResponse('File was not attached!', status=400)

        if not file.name.endswith('csv'):
            return HttpResponse('File is not csv format!', status=400)

        data = file.read().decode('UTF-8').split('\r\n')
        csv_reader = csv.reader(data, delimiter=',', quotechar='|')
        for column in csv_reader:
            Addition(
                user=CustomUser.objects.get(pk=int(column[0])),
                amount=column[1],
                description=column[2],
                date=column[3],
                addition_type=int(column[4])
            ).save()

        return HttpResponse('Additions added!', status=200)


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
