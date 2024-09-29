from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import OrganisatieSerializer, OnderzoekSerializer, VraagSerializer
from .models import Organisatie, Onderzoek, Vraag
import jwt
import datetime


class Register(APIView):
    def post(self, request):
        serializer = OrganisatieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            organisatie = Organisatie.objects.get(email=serializer.data['email'])

            payload = {
                'id': organisatie.id,
                'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.now(datetime.UTC)
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')

            organisatie.token = token
            organisatie.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        organisatie = Organisatie.objects.filter(email=email).first()

        if organisatie is None:
            raise AuthenticationFailed('Gebruiker niet gevonden')

        if not organisatie.check_password(password):
            raise AuthenticationFailed('Onjuist wachtwoord')

        payload = {
            'id': organisatie.id,
            'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now(datetime.UTC)
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response


class Research(APIView):
    def post(self, request):
        serializer = OnderzoekSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            onderzoek = Onderzoek.objects.get(titel=serializer.data['titel'])

            onderzoek.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class Question(APIView):
    def post(self, request):
        serializer = VraagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            vraag = Vraag.objects.get(vraagtitel=serializer.data['vraagtitel'])

            vraag.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)
