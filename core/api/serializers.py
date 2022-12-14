from rest_framework import serializers

from core.pos.models import Category, Product, Client
from core.postcosecha.models import Exportadora



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def to_representation(self, instance):
        return instance.toJSON()


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        return instance.toJSON()

class ExportadoraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exportadora
        fields = '__all__'

    def to_representation(self, instance):
        return instance.toJSON()