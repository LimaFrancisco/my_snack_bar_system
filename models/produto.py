from typing import Type 

# Uma das principais classes do projeto, representa a criação de objetos do tipo Produto
class Produto:

    contador_id = 0                               # Incrementa a cada objeto do tipo Produto criado

    def __init__(self, nome_produto: Type[str], preco: Type[float], descricao: Type[str]) -> Type[None]:
        Produto.contador_id += 1                  # Responsável por manter um valor único ao id de cada objeto do tipo Produto criado
        self.__id_produto = Produto.contador_id   # Identificador do objeto
        self.__nome_produto = nome_produto        # Nome do produto
        self.__preco = preco                      # Preço do produto
        self.__descricao = descricao              # Descrição em texto do produto


    # Métodos responsáveis por da visualização ao conteúdo dos atributos
    def get_id_produto(self) -> Type[int]:
        return self.__id_produto

    def get_nome_produto(self) -> Type[str]:
        return self.__nome_produto

    def get_preco(self) -> Type[float]:
        return self.__preco

    def get_descricao(self) -> Type[str]:
        return self.__descricao

    # Método para modificar o valor do atributo preço
    def atualizar_preco(self, novo_preco: Type[float]) -> Type[None]:
        self.__preco = novo_preco

