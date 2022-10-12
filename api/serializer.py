from rest_framework import serializers
from api.models import Reviews
from api.models import Books
from api.models import Cart


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    author = serializers.CharField()
    price = serializers.IntegerField()
    publisher = serializers.CharField()
    qty = serializers.IntegerField()

    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get("name")
        instance.author = validated_data.get("author")
        instance.price = validated_data.get("price")
        instance.publisher = validated_data.get("publisher")
        instance.qty = validated_data.get("qty")
        instance.save()
        return instance

    # def validate(self, data):
    #     errors = []
    #     price = data.get("price")
    #     qty = data.get("qty")
    #     if qty not in range(1, 500):
    #         # raise serializers.ValidationError("Invalid Quantity")
    #         errors.append({'password': "Invalid Price"})
    #     if price not in range(50, 1000):
    #
    #         # raise serializers.ValidationError("Invalid Price")
    #         errors.append({'password': "Invalid password"})
    #     if errors:
    #         raise serializers.ValidationError(errors)
    #
    #     return data


# Field level validation error

    def validate_price(self, value):
        if value not in range(1, 500):
            raise serializers.ValidationError('Invalid Price')
        return value
    def validate_qty(self, value):
        if value not in range(1, 500):
            raise serializers.ValidationError('Invalid Quantity')
        return value


class ReviewModelSerializer(serializers.ModelSerializer):
    created_date = serializers.CharField(read_only=True)

    class Meta:
        model = Reviews
        # exclude = ("created_date",)
        # fields = ["book", "user", "rating", "comment"]
        fields = "__all__"


# Import model for password and authentication

from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CartSerializer(serializers.ModelSerializer):
    books = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        models = Cart
        fields = ["books","user", "status"]


