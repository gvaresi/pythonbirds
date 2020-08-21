class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola, Meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 30

    @classmethod
    def metodo_e_atributo_de_classe(cls):
        return f'{cls} - olhos = {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe_pai = super().cumprimentar()  # retiramos o self do parentes para nao confundir com o
        return f'{cumprimentar_classe_pai}. Aperto de mão'  # metodo da propria função


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    giulia = Mutante(nome='Giulia')
    gian = Homem(felipe, giulia, nome='Gian')
    print(Homem.cumprimentar(gian))  # metodo com indicação do elemento
    print(id(gian))
    print(gian.cumprimentar())  # omitindo o elemento no parentes mas ele foi indicado no inicio, antes do '.'
    print(felipe.cumprimentar())  # omitindo o elemento no parentes mas ele foi indicado no inicio, antes do '.'
    print(giulia.cumprimentar())  # omitindo o elemento no parentes mas ele foi indicado no inicio, antes do '.'
    print(gian.nome)
    print(gian.idade)
    for filho in gian.filhos:
        print(filho.nome)
    gian.sobrenome = 'Varesi'
    del gian.filhos
    del felipe.idade
    del giulia.idade
    print(gian.__dict__)
    print(felipe.__dict__)
    print(giulia.__dict__)
    print(gian.olhos)
    print(felipe.olhos)
    print(giulia.olhos)
    print(id(gian.olhos), id(felipe.olhos), id(giulia.olhos))
    print(Pessoa.metodo_estatico(), gian.metodo_estatico())
    print(Pessoa.metodo_e_atributo_de_classe(), gian.metodo_e_atributo_de_classe())
    print(isinstance(gian, Pessoa))
    print(isinstance(gian, Homem))
    print(isinstance(felipe, Pessoa))
    print(isinstance(felipe, Homem))  # Pessoa nao herda nada de Homem
    print(giulia.olhos)
