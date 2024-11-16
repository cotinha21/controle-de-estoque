PROJETO - CONTROLE DE ESTOQUE


Participantes (Engenharia de Produção):
gabriel cota: 202410312
pedro pagano: 202410138



Qual a Proposta
A proposta do programa de controle de estoque é oferecer uma solução simples e eficiente para a gestão de produtos em um ambiente de pequena escala, como em pequenos negócios ou para uso pessoal. Aqui estão os principais objetivos do programa:
Facilidade de Uso: Através de uma interface gráfica intuitiva, qualquer usuário, independentemente de sua familiaridade com tecnologia, pode facilmente adicionar, remover e gerenciar produtos em estoque.

Gerenciamento Eficiente: Permitir que os usuários mantenham um registro organizado dos produtos disponíveis, controlando quantidades e atualizando informações conforme necessário, tudo gerido através de uma interface direta e amigável.

Flexibilidade e Escalabilidade: Projetado para ser facilmente adaptável, o código pode ser expandido com novas funcionalidades ou integrado a sistemas mais complexos conforme as necessidades do usuário crescem.

Resolução de Problemas Comuns: Através de funcionalidades como pesquisa e atualização de quantidades, o programa visa resolver problemas comuns enfrentados no gerenciamento de estoques, como encontrar rapidamente um item ou corrigir discrepâncias nas quantidades registradas.

Como foi feito
O programa é desenvolvido em Python e utiliza a biblioteca Tkinter para criar uma interface gráfica de usuário (GUI). Aqui estão os principais componentes e métodos utilizados:
Tkinter: 
Usado para criar a interface gráfica. A janela principal é criada e configurada com botões, entradas de texto e um listbox para interagir com o usuário.
Classes Produto e Estoque:
A classe Produto define o modelo de um produto com atributos de nome e quantidade.
A classe Estoque gerencia os produtos, permitindo carregar, adicionar, remover, atualizar, listar, e salvar produtos no arquivo estoque.txt.
Arquivo estoque.txt: Usado para carregar e salvar o estado do estoque, garantindo que os dados persistam entre as execuções do programa.

Widgets do Tkinter:
Frames, Entry, Button, Listbox: Organizam a interface de usuário para entrada de dados, execução de ações (como adicionar/remover produtos), e exibição da lista de produtos no estoque.
Messagebox:
 Exibe mensagens de erro ou sucesso ao usuário.

Como utilizar o programa
Iniciar o Programa: Execute o script em um ambiente Python. Uma janela será aberta, representando a interface do controle de estoque.
Adicionar Produto:
Insira o nome do produto no campo "Nome do Produto".
Informe a quantidade no campo "Quantidade".
Clique no botão "Adicionar" para incluir o produto no estoque. Se o produto já existir, a quantidade será incrementada.
Remover Produto:
Selecione o produto na lista.
Informe a quantidade a ser removida (opcional, padrão é 1).
Clique em "Remover" para decrementar a quantidade ou remover o produto se a quantidade atingir zero.
Atualizar Quantidade:
Selecione o produto na lista.
Informe a nova quantidade no campo "Quantidade".
Clique em "Atualizar" para modificar a quantidade existente para a nova quantidade informada.
Excluir Produto:
Selecione o produto que deseja excluir da lista.
Clique em "Excluir" para remover completamente o produto do estoque.
Pesquisar Produto:
Digite parte ou o nome completo do produto no campo "Pesquisar".
Clique em "Pesquisar" para filtrar e exibir apenas os produtos que correspondem à pesquisa.
Salvar Alterações: 
Todas as alterações são salvas automaticamente no arquivo estoque.txt após qualquer operação de adição, remoção, atualização ou exclusão de produtos.
O programa é projetado para ser intuitivo e fácil de usar, oferecendo uma solução simples para o gerenciamento de estoque com funcionalidades essenciais para manipular produtos.

link github: https://github.com/cotinha21/controle-de-estoque


