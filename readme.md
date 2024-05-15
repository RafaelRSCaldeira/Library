# Sistema Simples de Gerenciamento de Biblioteca com Uso de Tipos Abstratos de Dados

**Objetivo:**
Desenvolver um sistema de gerenciamento de biblioteca utilizando tipos abstratos de dados (ADTs) como pilhas, filas, listas e mapas para realizar operações de empréstimo, devolução, reserva de livros e gerenciamento de usuários.

**Descrição:**
O sistema deve permitir o cadastro de livros e usuários, controle de empréstimos, devoluções, reservas de livros e manutenção de um histórico de operações que possa ser revertido. Os dados devem ser gerenciados de forma eficiente utilizando os ADTs apropriados para cada tipo de operação.

**Requisitos Funcionais:**
1. Cadastro de Usuários:
- Armazenar as informações dos usuários, como ID, nome e histórico de empréstimos.
- Cada usuário deve ter um histórico de suas operações.
2. Cadastro de Livros:
- Registrar cada livro com atributos como ISBN, título, autor e disponibilidade.
- Permitir adicionar, remover e consultar livros no sistema.
3. Empréstimos de Livros:
- Permitir que usuários cadastrados emprestem livros disponíveis.
- A disponibilidade do livro deve ser atualizada imediatamente após o empréstimo.
- Registrar a operação no histórico do usuário.
4. Devolução de Livros:
- Permitir que os livros emprestados sejam devolvidos.
- Atualizar a disponibilidade do livro.
- Registrar a operação no histórico do usuário.
5. Reserva de Livros:
- Se um livro desejado não estiver disponível, permitir que o usuário entre em uma fila de espera.
- Gerenciar as reservas por livro.
- Registrar a operação no histórico do usuário.
6. Histórico e Reversão de Operações:
- Permitir que usuários desfaçam a última operação realizada (seja empréstimo, devolução ou reserva).

**Análise Complexidade Assintótica**
Todos os métodos implementados possuem O(1), exceto os listados abaixo:
- UserManager.showHistory -> O(n), em que n é o número de entradas no histórico do usuário
