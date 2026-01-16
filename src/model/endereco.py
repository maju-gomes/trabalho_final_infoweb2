class Endereco:
    def __init__(self, i, cep, uf, ci, b, r, n, co):
        self.set_id(i)
        self.set_cep(cep)
        self.set_uf(uf)
        self.set_cidade(ci)
        self.set_bairro(b)
        self.set_rua(r)
        self.set_numero(n)
        self.set_complemento(co)

    def set_id(self, v):
        self.__id = v
    def set_cep(self, v):
        v = ''.join(c for c in v if c.isdigit()) if v else ''
        if not v or len(v) != 8:
            raise ValueError('CEP Inválido')
        self.__cep = v
    def set_uf(self, v):
        v = v.strip().upper() if v else ''
        if not v or len(v) != 2:
            raise ValueError('UF Inválido')
        self.__uf = v
    def set_cidade(self, v):
        v = v.strip().title() if v else ''
        if not v or len(v) > 100:
            raise ValueError('Cidade Inválida')
        self.__cidade = v
    def set_bairro(self, v):
        v = v.strip().title() if v else ''
        if not v or len(v) > 100:
            raise ValueError('Bairro Inválido')
        self.__bairro = v
    def set_rua(self, v):
        v = v.strip().title() if v else ''
        if not v or len(v) > 150:
            raise ValueError('Rua Inválida')
        self.__rua = v
    def set_numero(self, v):
        if not v or len(v) > 10:
            raise ValueError('Número Inválido')
        self.__numero = v
    def set_complemento(self, v):
        if v and len(v) > 50:
            raise ValueError('Complemento Inválido')
        self.__complemento = v

    def get_id(self):
        return self.__id
    def get_cep(self):
        return self.__cep
    def get_uf(self):
        return self.__uf
    def get_cidade(self):
        return self.__cidade
    def get_bairro(self):
        return self.__bairro
    def get_rua(self):
        return self.__rua
    def get_numero(self):
        return self.__numero
    def get_complemento(self):
        return self.__complemento
    
    def __str__(self):
        return f"{self.__id} - {self.__cep} - {self.__uf} - {self.__cidade} - {self.__bairro} - {self.__rua} - {self.__numero} - {self.__complemento}"
