from database import BancoDeDados
from dao.usuarioDAO import UsuarioDAO
from model.usuarios import Usuario

def lerSalvarObjUsuario():

    banco_dados = BancoDeDados("banco_usuario.db")
    usuario_dao = UsuarioDAO(banco_dados)

    usuario_dao.criar_tabela()

    usuario1 = Usuario(
        None,
        "Maria",
        "maria@gmail.com",
        "senha123"
    )

    usuario2 = Usuario(
        None,
        "Maria",
        "maria2@gmail.com",
        "senha123"
    )

    # usuario_dao.inserir_usuario(usuario1)
    # usuario_dao.inserir_usuario(usuario2)
    usuario_dao.excluir_usuario(2)

    usuarios = usuario_dao.listar_usuarios()
    
    for u in usuarios:
        print(u)

lerSalvarObjUsuario()


