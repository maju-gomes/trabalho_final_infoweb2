class Doacao:
    def __init__(self, i, d, t, q):
        self.set_id(i)
        self.set_descricao(d)
        self.set_tipo(t)
        self.set_qntd(q)
    def set_id(self, v): self.__id = v
    def set_descricao(self, v):
        if not v: raise ValueError('Descrição Inválida')
        self.__descricao = v
    def set_tipo(self, v):
        if not v: raise ValueError('Tipo Inválido')
        self.__tipo = v
    def set_qntd(self, v):
        if not v: raise ValueError('Quantidade Inválida')
        self.__qntd = v
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_tipo(self): return self.__tipo
    def get_qntd(self): return self.__qntd
    def __str__(self): return f"{self.__id} - {self.__descricao} - {self.__tipo} - {self.__qntd}"

class Produto:
    def __init__(self, i, d, t, q):
        self.set_id(i)
        self.set_descricao(d)
        self.set_tipo(t)
        self.set_qntd(q)
    def set_id(self, v): self.__id = v
    def set_descricao(self, v):
        if not v: raise ValueError('Descrição Inválida')
        self.__descricao = v
    def set_tipo(self, v):
        if not v: raise ValueError('Tipo Inválido')
        self.__tipo = v
    def set_qntd(self, v):
        if not v: raise ValueError('Quantidade Inválida')
        self.__qntd = v
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_tipo(self): return self.__tipo
    def get_qntd(self): return self.__qntd
    def __str__(self): return f"{self.__id} - {self.__descricao} - {self.__tipo} - {self.__qntd}"