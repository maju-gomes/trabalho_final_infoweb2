from dao.usuariosDAO import AdminDAO, DoadorDAO, FavorecidoDAO
from dao.enderecoDAO import EnderecoDAO
from dao.doacao_produtoDAO import DoacaoDAO, ProdutoDAO
from model.usuarios import Admin, Doador, Favorecido
from model.endereco import Endereco
from model.doacao_produto import Doacao, Produto

# end = Endereco(
#     None,
#     '31090-855',
#     'PE',
#     'Recife',
#     'Ta Bom',
#     'Felicidade',
#     '100',
#     None
# )
# EnderecoDAO.inserir(end)


# admin = Admin(
#     None,
#     'Gilbert',
#     'gil@gmail.com',
#     '1234',
#     '12.345.678/0001-98'
# )
# AdminDAO.inserir(admin)


# doador = Doador(
#     None,
#     'Ricardo',
#     'ric@gmail.com',
#     '1234',
#     '555.555.555-88',
#     '(84) 998124951'
# )
# DoadorDAO.inserir(doador)


# fav = Favorecido(
#     None,
#     'Clara',
#     'cla@gmail.com',
#     '1234',
#     '777.777.777-88',
#     None,
#     1
# )
# FavorecidoDAO.inserir(fav)


# doacao = Doacao(
#     None,
#     'PC',
#     'Tecnologia',
#     2,
#     1
#     )

# DoacaoDAO.inserir(doacao)


produto = Produto(
    None,
    'Celular',
    'Tecnologia',
    4,
    1
)
ProdutoDAO.inserir(produto)