Resolvendo o Problema XY
=========================
:author: Humberto Rocha
:date: 2015-10-21 8:35
:tags: comunidade, comunicação, lifehack
:image: /images/argument.jpg
:category: LifeHack

Olá pessoal, tudo bom?

Esta postagem teve como base o episódio de um podcast que acompanho, o `Developer Tea`_, e minha percepção de que este é um problema recorrente em nosso dia a dia como programador, em comunidades e no trabalho.

**TLDR:** Ao descrever um problema tente contextualizar ao máximo, explicitar sua intenção e evite o jargão técnico se possível.

O problema XY acontece quando queremos resolver um problema X e achamos que Y é a melhor maneira de resolver. Então, perguntamos sobre Y sem ao menos mencionar X.

Um dialogo simples mostra esta dinâmica:

**Brian:** Cara, você sabe como eu faço para recuperar os três últimos caracteres do nome de um arquivo?

**Reg:** Se você tiver ele em uma variável é só tirar uma fatia ``arquivo[:-3]``

**Reg:** Mas pra que você quer fazer isso?

**Reg:** Você está tentando recuperar a extensão do arquivo?

**Brian:** Sim

**Reg:** Porque não me disse antes?

**Reg:** Desta forma você terá problemas com extensões que não possuem 3 caracteres.

**Reg:** Somente capturar os 3 últimos caracteres não resolve seu problema.

Discussões como essa acontecem o tempo todo em comunidades, e é muito comum que ela se estenda por muito tempo, deixando as pessoas aborrecidas por não conseguirem efetivamente ajudar ou frustradas por não chegarem a uma solução para o real problema.

Legal, mas como eu evito este tipo de problema?
-----------------------------------------------

A primeira coisa que precisamos fazer é contextualizar o nosso problema e evitar o 'tecniquês' ao máximo na hora de descrevê-lo. Se estamos tentando capturar as inciais do nome de um usuário para fazer abreviação descreva seu problema desta forma, não saia dizendo que você quer capturar os primeiros caracteres de algumas strings e concatená-las com ponto.

Quando informamos o contexto, permitimos que as pessoas ajudem com o problema, não com detalhes específicos de uma forma de implementação que no final pode acabar não o resolvendo. O próprio caso de abreviação tem questões como as formas de tratamento (sr, sra, srta, etc) que podem passar batido quando fora de contexto.

Outro ponto importante é explicar sua intenção. Por exemplo, se você está tentando validar um email com expressões regulares, provavelmente muitas pessoas poderão te ajudar a chegar em uma expressão que valide o padrão de endereço de email, mas sua intenção era de saber se ele pertence a alguém. Sua solução resolve a questão de saber se o email é válido, entretanto não garante que alguém esteja o utilizando. 

É bem comum, devido ao medo de menosprezarem nosso problema, querer chegar com alguma solução na cabeça antes de perguntar. De fato isso é importante e encorajado nas listas de discussão —  procure antes de perguntar, tente resolver sozinho primeiro — porém, se realizando os passos anteriores não foi encontrada a solução, é necessário voltar a raiz do problema, abandonar os pedaços de solução que temos na cabeça e partir do início sempre buscando contextualizar nosso problema e explicitar nossa intenção. Claro que detalhar o que já foi tentado pode ajudar, mas não esqueça de 'começar do começo' ao descrevê-lo. 

Algumas referências em inglês sobre o assunto:

- `The XY Problem`_
- `Wiki XY Problem`_

    Deveria haver um — e de preferencialmente apenas um —  modo óbvio para fazer algo.

    Embora esse modo possa não ser óbvio a princípio, a menos que você seja holandês.

    -- `O Zen do Python`_

.. _Developer Tea: http://developertea.com/episodes/18468/
.. _The XY Problem: http://xyproblem.info/
.. _Wiki XY Problem: http://mywiki.wooledge.org/XyProblem/
.. _O Zen do Python: https://www.python.org/dev/peps/pep-0020/
