from rest_framework import viewsets
from portfolio.serializers import ProjetoSerializer
from portfolio.models import Projeto
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.http import JsonResponse

from django.core.mail import send_mail


import smtplib



class ProjetosViewsSets(viewsets.ModelViewSet):
    '''Mostrando todos os projetos'''
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    http_method_names = ['get']


class EmailSenderView(APIView): 
    def post(self, request, *args, **kwargs):
        
            # Lógica para enviar o e-mail aqui
        # ...
            assunto = f'Formulário preenchido por {request.data["name"]}'
            mensagem = f' Formulário preenchido por {request.data["name"]} \n Motivo do contato: {request.data["contactSubject"]} \n Email: {request.data["email"]} \n Telefone: {request.data["phone"]} '
            remetente = 'taynandossantosaparecido@outlook.com'
            destinatario = ['taynandossantosaparecido@gmail.com']

            send_mail(assunto, mensagem, remetente, destinatario)

            return Response({'message': 'E-mail enviado com sucesso!'}, status=status.HTTP_200_OK)