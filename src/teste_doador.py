from database import BancoDeDados
from dao.doadorDAO import DoadorDAO
from dao.usuariosDAO import UsuarioDAO
from dao.telefoneDAO import TelefoneDAO
from model.usuarios import Doador

def lerSalvarObjDoador():
    banco_dados = BancoDeDados("banco_doador.db")
    doador_dao = DoadorDAO(banco_dados) #vincula a variavel doador a este banco
    usuario_dao = UsuarioDAO(banco_dados)
    telefone_dao = TelefoneDAO(banco_dados)

    usuario_dao.criar_tabela()
    telefone_dao.criar_tabela()
    doador_dao.criar_tabela()

    doador1 = Doador(
        None,
        "Ludmylla",
        "lud@gmail.com",
        "senha123",
        "11122233344",
        1
    )

    doador_dao.inserir_doador(doador1)
    doadores = doador_dao.listar_doadores()

    for doador in doadores:
        print(doador)

lerSalvarObjDoador()