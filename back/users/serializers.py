from rest_framework import serializers

from .models import User, Workshop


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = [
            'workshop_name',
            'phone',
            'email',
            'city',
            'street',
            'house_number',
            'flat_number',
            'zip_code',
            'slug',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class UserSerializerDB(serializers.ModelSerializer):
    workshop = WorkshopSerializer()

    class Meta:
        model = User
        fields = [
            'workshop',
            'last_login',
            'username',
            'is_active',
            'date_joined',
            'first_name',
            'last_name',
            'phone',
            'email',
            'city',
            'street',
            'house_number',
            'flat_number',
            'zip_code',
        ]
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('street', instance.street)
        instance.house_number = validated_data.get('house_number', instance.house_number)
        instance.flat_number = validated_data.get('flat_number', instance.flat_number)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        if 'workshop' in validated_data:
            workshop_data = validated_data.pop('workshop')
            instance.workshop = Workshop.objects.create(**workshop_data)
        instance.save()
        return instance
