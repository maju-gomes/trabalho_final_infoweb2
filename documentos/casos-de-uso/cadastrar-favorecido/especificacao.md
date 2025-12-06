# Caso de Uso: Cadastrar Favorecido

## **Atores Envolvidos**
- **Administrador**

---

## **Pré-condições**
- O administrador deve estar logado no sistema.  

---

## **Pós-condições**
- Uma novo usuário (favorecido) deve estar cadastrado no banco de dados do sistema e poderá acessá-lo com suas credenciais.

---

## **Fluxo Principal**
1. O administrador informa os dados do favorecido (nome, e-mail e senha e CPF).
2. O sistema verifica se todos os dados foram preenchidos corretamente.
3. O sistema cadastra o novo usuário no banco de dados.

---

## **Fluxo de Exceção (2)**
- **2a.** Se alguma informação não for preenchida, estiver incorreta ou o e-mail ou o CPF fornecido já estiver cadastrado no sistema, o sistema solicita a correção dos dados.

