from rest_framework import serializers
from .models import Organisatie, Onderzoek, Vraag


class OrganisatieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisatie
        fields = ['id', 'bedrijfsnaam', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        if Organisatie.objects.filter(email=email).exists():
            raise serializers.ValidationError("E-mailadres is al in gebruik")

        wachtwoord = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if wachtwoord is not None:
            instance.set_password(wachtwoord)
        instance.save()
        return instance


class OnderzoekSerializer(serializers.ModelSerializer):
    token = serializers.CharField(write_only=True)

    class Meta:
        model = Onderzoek
        fields = ['onderzoek_id', 'titel', 'beschikbaar', 'beschrijving', 'startdatum', 'einddatum', 'type_onderzoek',
                  'locatie', 'met_beloning', 'beloning', 'doelgroep_leeftijd_van', 'doelgroep_leeftijd_tot',
                  'doelgroep_beperking', 'token']
        extra_kwargs = {
            'titel': {'validators': []},
        }

    def validate(self, data):
        token = data.get('token')
        if token is None:
            raise serializers.ValidationError("Geen API-token verstrekt.")

        try:
            organisatie = Organisatie.objects.get(token=token)
        except Organisatie.DoesNotExist:
            raise serializers.ValidationError("Ongeldige API-token.")

        titel = data.get('titel')
        if Onderzoek.objects.filter(organisatie=organisatie, titel=titel).exists():
            raise serializers.ValidationError(
                "Deze titel wordt al gebruikt voor een ander onderzoek van uw organisatie.")

        return data

    def create(self, validated_data):
        token = validated_data.pop('token', None)

        try:
            organisatie = Organisatie.objects.get(token=token)
        except Organisatie.DoesNotExist:
            raise serializers.ValidationError("Ongeldige API-token.")

        validated_data['organisatie'] = organisatie

        instance = Onderzoek.objects.create(**validated_data)

        print("Organisatie ID:", organisatie.id)
        return instance


class VraagSerializer(serializers.ModelSerializer):
    token = serializers.CharField(write_only=True)
    onderzoek_titel = serializers.CharField(write_only=True)

    class Meta:
        model = Vraag
        fields = ['vraag_id', 'vraagtitel', 'beschrijving', 'categorie', 'onderzoek_titel', 'token']

    def validate(self, data):
        token = data.get('token')
        if token is None:
            raise serializers.ValidationError("Geen API-token verstrekt.")

        try:
            organisatie = Organisatie.objects.get(token=token)
        except Organisatie.DoesNotExist:
            raise serializers.ValidationError("Ongeldige API-token.")

        data['organisatie'] = organisatie

        return data

    def create(self, validated_data):
        onderzoek_titel = validated_data.pop('onderzoek_titel', None)
        vraagtitel = validated_data.get('vraagtitel')

        try:
            onderzoek = Onderzoek.objects.get(titel=onderzoek_titel)
        except Onderzoek.DoesNotExist:
            raise serializers.ValidationError("Er bestaat geen onderzoek met deze titel.")

        if Vraag.objects.filter(vraagtitel=vraagtitel, onderzoek=onderzoek).exists():
            raise serializers.ValidationError("Deze vraagtitel bestaat al binnen dit onderzoek.")

        token = validated_data.pop('token', None)
        organisatie = validated_data.pop('organisatie', None)

        instance = Vraag.objects.create(onderzoek=onderzoek, **validated_data)

        return instance
