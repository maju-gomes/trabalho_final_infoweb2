class Usuario:
    def __init__(self, i, n, e, s):
        self.set_id(i)
        self.set_nome(n)
        self.set_email(e)
        self.set_senha(s)

    def set_id(self, v):
        self.__id = v
    def set_nome(self, v):
        if not v:
            raise ValueError('Nome Inválido')
        self.__nome = v
    def set_email(self, v):
        if not v or '@' not in v:
            raise ValueError('E-mail Inválido')
        self.__email = v
    def set_senha(self, v):
        if not v:
            raise ValueError('Senha Inválida')
        self.__senha = v

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_senha(self):
        return self.__senha
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__senha}"


class Admin(Usuario):
    def __init__(self, i, n, e, s, cnpj):
        super().__init__(i, n, e, s)
        self.set_cnpj(cnpj)

    def set_cnpj(self, v):
        v = ''.join(c for c in v if c.isdigit())
        if not v or len(v) != 14:
            raise ValueError('CNPJ Inválido')
        self.__cnpj = v

    def get_cnpj(self):
        return self.__cnpj
    def __str__(self):
        return f"{super().__str__()} - {self.__cnpj}"


class Doador(Usuario):
    def __init__(self, i, n, e, s, cpf):
        super().__init__(i, n, e, s)
        self.set_cpf(cpf)

    def set_cpf(self, v):
        v = ''.join(c for c in v if c.isdigit())
        if not v or len(v) != 11:
            raise ValueError('CPF Inválido')
        self.__cpf = v
    def get_cpf(self):
        return self.__cpf
    def  __str__(self):
        return f"{super().__str__()} - {self.__cpf}"


class Favorecido(Usuario):
    def __init__(self, i, n, e, s, cpf):
        super().__init__(i, n, e, s)
        self.set_cpf(cpf)

    def set_cpf(self, v):
        v = ''.join(c for c in v if c.isdigit())
        if not v or len(v) != 11:
            raise ValueError('CPF Inválido')
        self.__cpf = v
    def get_cpf(self):
        return self.__cpf
    def  __str__(self):
        return f"{super().__str__()} - {self.__cpf}"