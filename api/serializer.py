from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    author = serializers.CharField()
    price = serializers.IntegerField()
    publisher = serializers.CharField()
    qty = serializers.IntegerField()

