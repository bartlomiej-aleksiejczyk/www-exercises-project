from rest_framework import serializers

from ludzie.models import Stanowisko, Osoba


class StanowiskoSerializer(serializers.Serializer):
    nazwa = serializers.CharField(max_length=60, allow_null=False, allow_blank=False)
    opis = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return Stanowisko.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', "NIE PODANO")
        instance.save()
        return instance


class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = '__all__'
