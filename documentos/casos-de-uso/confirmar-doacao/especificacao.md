# Caso de Uso: Confirmar Doacao

## **Atores Envolvidos**
- **Administrador**

---

## **Pré-condições**
- O administrador deve estar logado no sistema
- Deve existir uma proposta de doação registrada

---

## **Pós-condições**
- A doação deve aparecer para o administrador como apta à reciclagem (se aceita) ou inapta (se não aceita).

---

## **Fluxo Principal - Aceitar doação**
1. O administrador visualiza a proposta de doação.
2. O administrador confirma a proposta.
3. O sistema cadastra a doação no banco de dados

---

## **Fluxo alternativo(1) - Não aceitar a doação**
1. O administrador rejeita a doação
2. O sistema marca a doação como rejeitada e exibe este status ao doador
