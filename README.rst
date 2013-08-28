python-eventick
===============

O python-eventick é um wrapper para acessar os dados da API do www.eventick.com.br.

Instalação
----------

.. code-block::

    pip install python-eventick


ou

.. code-block::

    git clone https://github.com/lyralemos/python-eventick.git
    cd python-eventick
    python setup.py install


Exemplo
---

.. code-block:: python

    from eventick import Eventick

    eventickAPI = Eventick('username@email.com','password')
    eventos = eventickAPI.events() #lista de eventos

Documentação
------------

API(autenticação)
~~~~~~~~~~~~~~~~
Ao instanciar um objeto Eventick será realizada a autenticação

.. code-block:: python

    eventickAPI = Eventick('username@email.com','password')

events()
~~~~~~~~~~
Lista de todos os eventos.

.. code-block:: python

    eventos = eventickAPI.events()

event(id)
~~~~~~~~~
Retorna informações específicas de um evento

``id`` - Código do evento

.. code-block:: python

    evento = eventickAPI.event(1234)

attendees(id_evento)
~~~~~~~~~~~~~~~~~~~~
Lista dos participantes do evento

``id_evento`` - Código do evento

.. code-block:: python

    participantes = eventickAPI.attendees(1234)

attendee(id_evento,id)
~~~~~~~~~~~~~~~~~~~~~
Informações de um participante específico.

``id_evento`` - Código do evento

``id`` - Código do participante

.. code-block:: python

    participante = eventickAPI.attendee(1234,65432)


checkin(id_evento,code,time)
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Realiza o check-in do participante.

``id_evento`` - Código do evento

``code`` - Código de identificação do participante

``time`` - Horário do checkin

Changelog
---------

``0.2`` - Corrigido problemas de instalação

``0.1`` - Versão inical