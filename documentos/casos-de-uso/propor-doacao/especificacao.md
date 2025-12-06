# Caso de Uso: Propor Doação

## **Atores Envolvidos**
- **Doador**
- **Administrador**

---

## **Pré-condições**
- O doador deve estar logado no sistema.  
- O doador deve ter pelo menos 18 anos.

---

## **Pós-condições**
- O produto doado deve aparecer para o administrador como uma opção a ser aceita e posteriormente reciclada.  
- Caso o administrador aceite a doação, o produto passa a constar como **apto à reciclagem**.

---

## **Fluxo Principal**
1. O doador informa o seu CPF, a descrição, o tipo e a quantidade da doação.
2. O sistema verifica os dados fornecidos.
3. O administrador confirma a proposta de doação.

---

## **Fluxo de Exceção (2)**
- **2a.** Se alguma informação não for preenchida ou o CPF do doador estiver incorreto, o sistema solicita a correção dos dados.

