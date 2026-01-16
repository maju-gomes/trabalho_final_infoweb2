class Doacao:
    def __init__(self, i, d, t, q_do, q_di, s, i_d):
        self.set_id(i)
        self.set_descricao(d)
        self.set_tipo(t)
        self.set_quantidade_doada(q_do)
        self.set_quantidade_disponivel(q_di)
        self.set_situacao(s)
        self.set_id_doador(i_d)

    def set_id(self, v):
        self.__id = v
    def set_descricao(self, v):
        v = v.strip().title() if v else ''
        if not v or len(v) > 50:
            raise ValueError('Descrição Inválida')
        self.__descricao = v
    def set_tipo(self, v):
        v = v.strip().title() if v else ''
        if not v or len(v) > 50:
            raise ValueError('Tipo Inválido')
        self.__tipo = v
    def set_quantidade_doada(self, v):
        if not v or v <= 0:
            raise ValueError('Quantidade Inválida')
        self.__quantidade_doada = v
    def set_quantidade_disponivel(self, v):
        self.__quantidade_disponivel = v
    def set_situacao(self, v):
        self.__situacao = v
    def set_id_doador(self, v):
        self.__id_doador = v

    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_tipo(self):
        return self.__tipo
    def get_quantidade_doada(self):
        return self.__quantidade_doada
    def get_quantidade_disponivel(self):
        return self.__quantidade_disponivel
    def get_situacao(self):
        return self.__situacao
    def get_id_doador(self):
        return self.__id_doador
    
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__tipo} - {self.__quantidade_doada} - {self.__quantidade_disponivel} - {self.__situacao} - {self.__id_doador}"
    
# -------------------------------

class Produto:
    def __init__(self, i, d, t, q, s, i_f):
        self.set_id(i)
        self.set_descricao(d)
        self.set_tipo(t)
        self.set_quantidade(q)
        self.set_situacao(s)
        self.set_id_favorecido(i_f)

    def set_id(self, v):
        self.__id = v
    def set_descricao(self, v):
        v = v.strip().title() if v else ''
        if not v or len(v) > 50:
            raise ValueError('Descrição Inválida')
        self.__descricao = v
    def set_tipo(self, v):
        v = v.strip().title() if v else ''
        if not v or len(v) > 50:        
            raise ValueError('Tipo Inválido')
        self.__tipo = v
    def set_quantidade(self, v):
        if not v or v <= 0:
            raise ValueError('Quantidade Inválida')
        self.__quantidade = v
    def set_situacao(self, v):
        if not v:
            raise ValueError('Situação Inválida')
        self.__situacao = v
    def set_id_favorecido(self, v):
        self.__id_favorecido = v

    def get_id(self):
        return self.__id
    def get_descricao(self): 
        return self.__descricao
    def get_tipo(self):
        return self.__tipo
    def get_quantidade(self):
        return self.__quantidade
    def get_situacao(self):
        return self.__situacao
    def get_id_favorecido(self):
        return self.__id_favorecido
    
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__tipo} - {self.__quantidade} - {self.__situacao} - {self.__id_favorecido}"