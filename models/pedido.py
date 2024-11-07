from typing import Type, List
from datetime import datetime
from .produto import Produto
from enums.status_pedido import StatusPedido

class Pedido: # Classe responsável por armazenar produtos pedidos pelo cliente

    contador_id = 0                               # Contador que incrementa toda vez que um objetos do tipo Pedido é criado

    def __init__(self, status: Type[StatusPedido], id_cliente: Type[int], produtos: Type[List[Produto]]) -> Type[None]:
        Pedido.contador_id += 1                   # O contador incrementa sempre quando um objeto é criado
        self.__id_pedido = Pedido.contador_id     # Identificador único do objeto
        self.__data_hora = datetime.now()         # Data e hora em que foi realizado o pedido
        self.__status = status                    # Status atual do pedido, valores do tipo StatusPedido
        self.__id_cliente = id_cliente            # Id do cliente que solicitou o pedido
        self.__produtos = produtos                # Todos produtos solicitados pelo cliente

    # Método para adicionar novo produto ao pedido
    def adicionar_novo_produto(self, novo_produto: Type[Produto]) -> Type[None]:
        self.__produtos.appende(novo_produto)
    
    # Retorna o valor total do pedido
    def calcular_total(self) -> Type[float]:
        total = 0
        for produto in self.__produtos:
            total += produto.get_preco()

        return total
    
    # Metodo para mudar o status do pedido
    def atualizar_status(self, status: Type[StatusPedido]) -> Type[None]:
        self.__status = status
    
    # Exibe dados do pedido
    def exibir_dados_pedido(self) -> Type[None]:
        dados = self.__retornar_cabecalho()
        dados += self.__exibir_dados_produtos()
        dados += self.__retornar_total()
        return dados
    
    # Método criardo para adicionar cabeçalho ao método exibir dados
    def __retornar_cabecalho(self) -> Type[str]:
        cabecalho = '---------------- DADOS DO PEDIDO -----------------\n' 
        cabecalho += f'{'-' * 50}\n'
        cabecalho += f'ID DO PEDIDO: {self.__id_pedido}\n\n'
        cabecalho += '-------------------- ITENS -----------------------\n'
        return cabecalho

    # Método criado para retornar os dados de todos os produtos do pedido
    def __exibir_dados_produtos(self) -> Type[str]:
        lista_produtos = ''
        quantidade = 0
        for produto in self.__produtos:
            if produto.get_nome_produto() not in lista_produtos:
                quantidade = self.__produtos.count(produto)
                lista_produtos += f'{produto.get_nome_produto() + ' ':-<38} {quantidade}x R$ {quantidade * produto.get_preco():.2f}\n'
        
        lista_produtos += f'{'-' * 50}'

        return lista_produtos

    # Método para retornar uma string com o valor total formatado 
    def __retornar_total(self) -> Type[str]:
        total = f'\n\n{'TOTAL ':-<41} R$ {self.calcular_total():.2f}'
        return total

