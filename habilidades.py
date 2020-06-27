from flask_restful import Resource
from flask import request
import json

lista_habilidades = [{'id': '0', 'nome': 'Python'},
                     {'id': '1', 'nome': 'Java'},
                     {'id': '2', 'nome': 'SQL'},
                     {'id': '3', 'nome': 'Django'},
                     {'id': '4', 'nome': 'PHM'},
                     {'id': '5', 'nome': 'APS.Net Core'},
                     {'id': '6', 'nome': 'Angular'},
                     {'id': '7', 'nome': 'React.Js'}]

class Habilidades(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            mensagem = 'Habilidade de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status': 'sucesso',
                        'mensagem': 'Registro excluido'}

class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]
