Links da Semana #2
==================
:author: Gilson Filho
:date: 2015-09-10 11:44
:tags: links, utilidades, dicas
:image: /images/serie-links/cover_links_1.jpg
:category: Dicas

Olá pessoal,


Demorei, mas vamos para a segunda edição do **Links da Semana**. Hoje vamos falar de muitos tutoriais e ferramentas, então aproveitem!



1. Ebook *Python 3 Patterns, Recipes and Idioms*
----------------------------------------------------------

Esse ebook é para quem deseja aprimorar os seus conhecimentos com Python, principalmente a versão 3, com padrões, boas práticas receitas utéis, para melhorar a qualidade do seu desenvolvimento. Coloque na sua lista de livros técnicos para ler.

Link: `https://python-3-patterns-idioms-test.readthedocs.org/en/latest/ <https://python-3-patterns-idioms-test.readthedocs.org/en/latest/>`_

2. Python and Real-time Web
---------------------------

Esse é um artigo do blog `Eat at Joe's <http://mrjoes.github.io/>`_ que fala sobre a relação do Python com as aplicações web real-time, como funciona, e como integrar com as aplicações WSGI. Além disso, traz uma introdução dos frameworks assíncronos em Python, e de algumas ferramentas que dão suporte a isso.

Link: `http://mrjoes.github.io/2013/06/21/python-realtime.html <http://mrjoes.github.io/2013/06/21/python-realtime.html>`_

3. Pesquisando verbetes com dicio
---------------------------------

Esse utilitário não é desenvolvido em Python (foi feito em Node.js), mas vale o espaço no post. Ele basicamente é um comando para ser usado not terminal, para que possa pesquisa (com Internet claro), verbetes no dicionário Aurélio. Segue um exemplo:

.. code-block:: bash

    $ dicio computador
    1 O que faz cálculos (pessoa ou máquina). 2 Aparelho eletrônico usado para
    processar, guardar e tornar acessível informação de variados tipos. 3 O me
    smo que computador pessoal. 4 computador pessoal: computador para uso indi
    vidual, cuja construção se baseia num microprocessador.

É mais um item para sua caixa de ferramentas.

Link: `https://github.com/theuves/dicio <https://github.com/theuves/dicio>`_

4. Diretivas úteis para o seu projeto AngularJS
-----------------------------------------------

Hoje o AngularJS, é o framework front-end queridinho do momento, e tem suas razões, já que ele é simples de se usar, modular e traz a tão querida organização e definição de camadas para "casca" do seu sistema. Para quem não sabe, diretiva é uma das features do Angular que lhe oferece recursos para desenvolver um componente web, totalmente reutilizável. Nesse post, ele traz algumas delas que são muito interessantes, e que um dia poderá precisar. Você tem componentes de preview de arquivos PDF a editores de textos incorporados.

Link: `http://codecondo.com/angular-js-directives/ <http://codecondo.com/angular-js-directives/>`_

5. PyPi Client - Acessando informações de pacotes via linha de comando
----------------------------------------------------------------------

Ele é um outro utilitário, para que possa acessar informações do PyPi como informações de pacote, estatísticas de download ou acessar documentação do pacote que pesquisou, em uma interface de linha de comando. Abaixo é um exemplo de como pode verificar informações do matplotlib:

.. code-block:: bash

    $ pypi info matplotlib

    matplotlib
    ==========
    Python plotting package

    Latest release:   1.3.1

    Last day:           2,015
    Last week:         16,744
    Last month:        59,989

    Author:   John D. Hunter, Michael Droettboom
    Author email: mdroe@stsci.edu

    PyPI URL:  http://pypi.python.org/pypi/matplotlib
    Home Page: http://matplotlib.org

    License: BSD

Link: `https://github.com/sloria/pypi-cli <https://github.com/sloria/pypi-cli>`_

6. Mastering Django atualizado para versão 1.8
----------------------------------------------

O Mastering Django é um famoso ebook, por ensinar o uso do framework Django, e agora foi atualizado para a versão 1.8 da ferramenta. Para quem deseja aprender a usar Django, fica a dica.

Link: `http://www.masteringdjango.com <http://www.masteringdjango.com>`_

Fonte: `https://github.com/big-nige/djangobook-Updated-to-1.8 <https://github.com/big-nige/djangobook-Updated-to-1.8>`_

7. Awesome Django: As aplicações Django selecionadas a mão
-----------------------------------------------------------------------------

Esse repositório traz uma lista de várias apps para usar nos seus projetos com Django. É organizado por categorias, cada uma define o objetivo das aplicações selecionadas. É uma curadoria de ferramentas que um dia poderá precisar.

Link: `https://github.com/rosarior/awesome-django <https://github.com/rosarior/awesome-django>`_

8. Exemplo de chat usando Tornado + WebSockets + MongoDB
--------------------------------------------------------

Esse repositório é um projeto de exemplo, um chat, que é feito usando as tecnologias: Websockets, Tornado, MongoDB e Motor. 

Link: `https://github.com/arruda/Tornado-WS-Assincrono <https://github.com/arruda/Tornado-WS-Assincrono>`_

9. Interpolação de String no Python 3
-------------------------------------

Foi aprovado uma nova PEP, voltado para interpolação de String. Chamado de PEP 0498, ela traz o `f-string` que oferece mais uma opção no tratamento das strings do seu código Python.

Link: `https://www.python.org/dev/peps/pep-0498/ <https://www.python.org/dev/peps/pep-0498/>`_

10. Criando queries SQL com Jinja2
----------------------------------

Pode parecer estranho, mas a idéia `Roman Zaiev <https://github.com/semirook>`_ é interessante e vale testar. Ele criou uma ferramenta em que você usa o Jinja2 para contruir queries variadas, com o SQL, e depois utilizadas no seu projeto somente com Python. O próprio README do projeto vai explicar melhor, então acesse.

Link: `https://github.com/semirook/snaql <https://github.com/semirook/snaql>`_

11. Aprendendo padrões de projetos com Python
---------------------------------------------

E por último, esse projeto traz vários códigos em Python, implementando cada padrão de projeto usado hoje no desenvolvimento. Vários livros que encontramos, usam C++ ou Java para exemplificar, e agora com esse repositório, você entenderá melhor o que cada padrão sugere.

Link: `https://github.com/faif/python-patterns <https://github.com/faif/python-patterns>`_


Fico por aqui. Até o próximo post!
