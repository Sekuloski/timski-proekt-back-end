from rest_framework import serializers
from finance.models import Purchase, ExpenseType, Addition


class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseType
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    expense_type = ExpenseTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Purchase
        fields = '__all__'


class AdditionSerializer(serializers.ModelSerializer):
    expense_type = ExpenseTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Addition
        fields = '__all__'
