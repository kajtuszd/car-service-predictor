from rest_framework import serializers

from .models import User, Workshop


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = [
            'workshop_name',
            'slug',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class UserSerializer(serializers.ModelSerializer):
    workshop = WorkshopSerializer()

    class Meta:
        model = User
        fields = '__all__'
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def update(self, instance, validated_data):
        if 'workshop' in validated_data:
            workshop_data = validated_data.pop('workshop')
            workshop = Workshop.objects.create(**workshop_data)
            instance.workshop = workshop
        instance.save()
        return instance
