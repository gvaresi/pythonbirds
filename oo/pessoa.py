class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 30

    @classmethod
    def metodo_e_atributo_de_classe(cls):
        return f'{cls} - olhos = {cls.olhos}'



if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    giulia = Pessoa(nome='Giulia')
    gian = Pessoa(felipe,giulia, nome='Gian')
    print(Pessoa.cumprimentar(gian)) # metodo com indicação do elemento
    print(id(gian))
    print(gian.cumprimentar()) # omitindo o elemento no parentes mas ele foi indicado no primeiro argumentp antes do '.'
    print(gian.nome)
    print(gian.idade)
    for filho in gian.filhos:
        print(filho.nome)
    gian.sobrenome = 'Varesi'
    del gian.filhos
    del felipe.idade
    del giulia.idade
    felipe.olhos = 1
    del felipe.olhos
    print(gian.__dict__)
    print(felipe.__dict__)
    print(giulia.__dict__)
    Pessoa.olhos = 3
    print(gian.olhos)
    print(felipe.olhos)
    print(giulia.olhos)
    print(id(gian.olhos), id(felipe.olhos), id(giulia.olhos))
    print(Pessoa.metodo_estatico(), gian.metodo_estatico())
    print(Pessoa.metodo_e_atributo_de_classe(), gian.metodo_e_atributo_de_classe())

