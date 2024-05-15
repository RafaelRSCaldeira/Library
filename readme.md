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

Para gerenciar uma biblioteca, foram utilizadas duas estruturas de dados: dicionários e filas. Os dicionários armazenaram informações sobre os livros disponíveis e os usuários da biblioteca. Por outro lado, a fila foi usada para acompanhar a ordem dos clientes que reservaram um livro específico.

O **dicionário** foi escolhido por várias razões:

1. **Acesso Rápido aos Elementos**: Os dicionários permitem acesso rápido aos seus elementos através de chaves, o que é muito eficiente, especialmente para grandes conjuntos de dados.

2. **Flexibilidade**: Você pode armazenar uma variedade de tipos de dados como valores em um dicionário, incluindo números, strings, listas e até mesmo outros dicionários.

3. **Mutabilidade**: Os dicionários são mutáveis, o que significa que você pode adicionar, remover e modificar elementos conforme necessário.

4. **Organização de Dados**: Os dicionários permitem organizar os dados de forma lógica e estruturada, associando valores a chaves específicas.

5. **Eficiência na Busca**: A busca por elementos em um dicionário é muito eficiente, independentemente do tamanho do dicionário, pois o tempo de busca não aumenta significativamente com o aumento do número de elementos.

6. **Implementação de Mapeamento**: Os dicionários são uma implementação eficiente do conceito de mapeamento, que é fundamental em muitos algoritmos e estruturas de dados.

7. **Fácil Manipulação de Dados**: Os dicionários facilitam a manipulação de dados em situações onde você precisa associar informações entre chaves e valores, como em análises de dados, processamento de texto e muito mais.

A **fila** foi escolhida pelos motivos a seguir:

1. **Gerenciamento de Tarefas Assíncronas**: As filas são úteis para implementar sistemas assíncronos, onde várias tarefas precisam ser executadas em segundo plano e em ordem específica.

2. **Comunicação entre Processos**: As filas podem ser compartilhadas entre processos em um programa multithread ou multiprocessado, permitindo uma comunicação segura e eficiente entre eles.

3. **Coordenação de Threads**: Em programas multithread, as filas são uma maneira segura de coordenar o acesso a recursos compartilhados entre várias threads, evitando condições de corrida.

4. **Buffer para Processamento Assíncrono**: As filas fornecem um mecanismo para bufferizar e enfileirar itens para processamento posterior em um ritmo que pode ser manipulado pelos processadores.

5. **Tolerância a Atrasos e Sobrecargas**: Ao usar filas, você pode lidar melhor com situações em que o produtor de dados está gerando itens mais rapidamente do que o consumidor pode processá-los, evitando assim a perda de dados.

6. **Padrão de Design para Fluxo de Dados**: Filas são um padrão de design comum para lidar com o fluxo de dados em sistemas distribuídos, permitindo que os diferentes componentes do sistema operem de forma independente, mas ainda coordenada.

7. **Implementação Eficiente**: As implementações de filas em Python são otimizadas para desempenho e eficiência, o que significa que podem lidar com grandes volumes de dados de forma rápida e escalável.
