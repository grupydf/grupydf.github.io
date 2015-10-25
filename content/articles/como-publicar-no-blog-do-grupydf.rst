Como Publicar No Blog Do Grupy-Df
=================================
:date: 2015-07-22 14:57
:category: Tutoriais
:author: Magnun Leno
:tags: tutorial, tecnico, pelican, site, git, github, pip, virtual env
:image: /images/monty-python-knights.jpg

Olá pessoal! Recentemente `inauguramos o site do Grupy-DF`_ e alguns membros do grupo estão começando a produzir conteúdos. Como eu fui o "maluco" a propor essa plataforma, achei que seria justo escrever um tutorial para aqueles que desconhecem um pouco o `Pelican`_. Então preparem seus cérebros pois vamos aprender desde *virtual env* até versionamento de código!

O Que é o Pelican
-----------------

Primeiramente o Pelican é um gerador de site estático multiplataforma (GNU/Linux, Mac OS e Windows), isto é, nosso site não possui nenhum servidor de aplicação (*backend*) em execução, ele é composto apenas de arquivos HTML, CSS e JavaScript. Mas por que isso é vantajoso? Eu já `escrevi sobre isso no meu site`_, mas em resumo ganhamos em performance, hospedagem, segurança e versionamento. Como este site receberá publicações de várias pessoas, resolvemos usar as *Issues* do GitHub para controlar os artigos que estão em processo de escrita (foi criada uma tag `Artigos`_ para concentrar todos os trabalhos). 

Outra vantagem de utilizarmos o site estático tendo o GitHub como "backend" é que as publicações podem ser controladas por meio de Pull Requests. Desta forma não limitamos as publicações apenas a quem tem permissão no repositório e/ou é membro do Grupy-DF. Já se estivéssemos utilizando um CMS... teríamos que criar uma conta pra esse usuário e confiar a ele acesso à nossa infraestrutura.

Obtendo Uma Cópia do Site
-------------------------

Para obter uma cópia do site você vai precisar do Git. Primeiramente acesse o `repositório do site`_ e crie um fork. Uma vez criado fork, clone o site em um diretório qualquer do seu desktop:

.. code-block:: bash

    $ cd ~
    $ git clone git@github.com:magnunleno/grupydf.github.io.git
    $ cd grupydf.github.io

O repositório é composto de alguns diretórios principais:

.. code-block:: bash

    grupydf.github.io
    │
    ├── content
    │   ├── articles
    │   ├── images
    │   └── pages
    ├── .plugins
    └── .themes

É tudo muito intuitivo, o diretório ``content`` possui todos os conteúdos, como artigos, imagens e páginas, o ``.plugins`` contém todos os *plugins* do Pelican, e o diretório ``themes`` possui o tema que utilizamos no site. Mas não se preocupem, vamos nos focar apenas no diretório ``contents``.

Agora temos que preparar o ambiente.

Preparando o Ambiente
---------------------

Criar o ambiente de uso do Pelican é muito simples, pra isso você vai precisar de:

- Python 2.7;
- VirtualEnv;
- Conexão de internet;
- Um terminal;
- Um editor de texto;
- Um navegador;

Primeiro abra um terminal e crie um *virtual environment* para o Python 2.7 (note que este passo não é obrigatório, mas é uma boa prática):

.. code-block:: bash

    $ virtualenv --prompt "(grupy-df)" ~/venv/grupy-df

Eu gosto de armazenar todos os meus *virtual envs* em um mesmo diretório (neste caso ``~/venv``), mas você pode colocar em qualquer outro lugar. Uma vez criado este *virtual env*, ative-o:

.. code-block:: bash

    $ . ~/venv/grupy-df/bin/activate

Uma vez ativado o *virtual env* basta instalar todas as dependências, para isso utilize o seguinte comando:

.. code-block:: bash

    $ pip install -r requirements.txt

Após instaladas todas as dependências faça uma compilação de teste do site com o comando ``make html``. Ao compilar o site é criado um diretório ``output``, com o conteúdo gerado, não se preocupe, este diretório já está no ``.gitignore`` e não deverá ser entrar no seu *commit*. Para visualizar o site **localmente** rode o comando ``make serve`` (sua linha de comando ficará "presa" pois ela está servindo as páginas neste momento) e acesse a URL http://localhost:8000. Note que todos estes comandos devem ser executados na raiz do repositório, onde se encontra o arquivo de "receitas" do make, isto é, o arquivo ``Makefile``. Para sair do "modo servidor" pressione ``Ctrl+C`` e a linha de comando retornará ao normal.

Após algum tempo de uso passe a pegar o costume de sempre executar uma cadeia de comandos para evitar que arquivos de compilações prévias interfiram com a minha visualização atual: ``make clean html serve``. Apenas esta linha de comando limpa o conteúdo do diretório ``output``, gera o site novamente, e entra no modo servidor. Novamente, para sair do *modo servidor* pressione ``Ctrl+C``.

Escrevendo Seus Próprios Artigos
--------------------------------

Para escrever seus próprios artigos sugiro olhar alguns de exemplo no diretório ``contents/articles``. Eu pessoalmente prefiro o uso da linguagem de marcação ReStructured Text, mas o Pelican também suporta a linguagem Markdown. Um artigo tem um cabeçalho fixo, conforme abaixo (em ReST):


.. code-blocK:: rst

    Como Publicar No Blog Do Grupy-Df
    =================================
    :date: 2015-07-22 14:57
    :author: Magnun Leno
    :category: Tutoriais
    :tags: tutorial, tecnico, pelican, site
    :image: /images/monty-python-knights.jpg

Ou em Markdown:

.. code-blocK:: markdown

    Title: Como Publicar No Blog Do Grupy-Df
    Date: 2015-07-22 14:57
    Author: Magnun Leno
    Category: Tutoriais
    Tags: tutorial, tecnico, pelican, site
    Image: /images/monty-python-knights.jpg

Novamente é tudo muito intuitivo, temos o título do artigo (a primeira linha em ReST, ou a precedida por ``Title:`` em Markdown) seguido da data de publicação (no formato ``YYYY-MM-DD HH:MM``). Logo abaixo temos o nome do autor, categoria e uma lista de tags. Somente a última tag é algo implementado por mim e não é nativo do Pelican.

A Tag ``:image::`` ou ``Image:`` (em Markdown) faz referência à imagem de capa do artigo, que também fica no "cabeçalho" do artigo, conforme print screens abaixo:

.. figure:: {filename}/images/article-image-header.png
    :target: {filename}/images/article-image-header.png
    :alt: Article Image Header
    :align: center

Após estas *meta-tags*, basta escrever o texto de acordo com a linguagem de marcação adotadas: `ReStructured Text`_ ou `Markdown`_. Para mais informações a `documentação do Pelican é excelente`_!
Uma vez concluído o artigo, emita novamente o comando ``make clean html serve`` e acesse a URL http://localhost:8000 para ver como ficou.

Lembre que o CSS deste site ainda não está completamente concluído e algumas coisas ainda precisam ser melhoradas, como por exemplo a exibição de códigos, tabelas e etc.

Enviando Sua Contribuição
-------------------------

Uma vez concluído o artigo, vamos realizar o *commit* da alteração:

.. code-block:: bash

    $ git add content/article/meu-artigo.rst
    $ git add content/images/minha-imagem-do-artigo.png
    $ git commit -m "Adicionado novo artivo 'meu-artigo'"

Com o *commit* realizado com sucesso, você pode realizar o push pro seu repositório remoto (GitHub):

.. code-block:: bash

    $ git push origin pelican

Agora basta enviar um *Pull Request* do seu repositório e os gestores do site irão aprovar sua contribuição.

.. _inauguramos o site do Grupy-DF: /blog/bem-vindos-ao-blog-do-grupy-df/
.. _Pelican: http://blog.getpelican.com/
.. _escrevi sobre isso no meu site: http://mindbending.org/pt/adeus-wordpress
.. _Artigos: https://github.com/grupydf/grupydf.github.io/labels/Artigo
.. _repositório do site: https://github.com/grupydf/grupydf.github.io/
.. _ReStructured Text: http://sphinx-doc.org/rest.html#rst-primer
.. _Markdown: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
.. _documentação do Pelican é excelente: http://docs.getpelican.com/en/3.6.0/content.html
