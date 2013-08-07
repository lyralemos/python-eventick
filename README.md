python-eventick
===============

O python-eventick é um wrapper para acessar os dados da API do www.eventick.com.br.

Instalação
----------

```
git clone https://github.com/lyralemos/python-eventick.git
cd python-eventick
python sety.py install
```

Exemplo
---

```python
from eventick import Eventick

eventickAPI = EVentick('username@email.com','password')
eventos = eventickAPI.events() #lista de eventos
```
Documentação
------------

###API(autenticação)
Ao instanciar um objeto Eventick será realizada a autenticação
```python
eventickAPI = EVentick('username@email.com','password')
```
###events()
Lista de todos os eventos.
```python
eventos = eventickAPI.events()
```
###event(id)
Retorna informações específicas de um evento

<table>
  <tr>
    <th>Campo</th>
    <th>Descrição</th>
    <th>Tipo</th>
    <th>Obrigatorio?</th>
  <tr>
  <tr>
    <td>id</td>
    <td>Código do evento</td>
    <td>inteiro</td>
    <td>Sim</td>
  </tr>
<table>


```python
evento = eventickAPI.event(1234)
```
###attendees(id_evento)
Lista dos participantes do evento
<table>
  <tr>
    <th>Campo</th>
    <th>Descrição</th>
    <th>Tipo</th>
    <th>Obrigatorio?</th>
  <tr>
  <tr>
    <td>id</td>
    <td>Código do evento</td>
    <td>inteiro</td>
    <td>Sim</td>
  </tr>
<table>
```python
participantes = eventickAPI.attendees(1234)
```
###attendee(id_evento,id)
Informações de um participante específico.
<table>
  <tr>
    <th>Campo</th>
    <th>Descrição</th>
    <th>Tipo</th>
    <th>Obrigatorio?</th>
  <tr>
  <tr>
    <td>id_evento</td>
    <td>Código do evento</td>
    <td>inteiro</td>
    <td>Sim</td>
  </tr>
  <tr>
    <td>id</td>
    <td>Código do participante</td>
    <td>inteiro</td>
    <td>Sim</td>
  </tr>
<table>
```python
participante = eventickAPI.attendee(1234,65432)
```

###checkin(id_evento,code,time)
Realiza o check-in do participante.
<table>
  <tr>
    <th>Campo</th>
    <th>Descrição</th>
    <th>Tipo</th>
    <th>Obrigatorio?</th>
  <tr>
  <tr>
    <td>id_evento</td>
    <td>Código do evento</td>
    <td>inteiro</td>
    <td>Sim</td>
  </tr>
  <tr>
    <td>code</td>
    <td>Código de identificação do participante</td>
    <td>string</td>
    <td>Sim</td>
  </tr>
  <tr>
    <td>time</td>
    <td>Horário do checkin</td>
    <td>datetime</td>
    <td>Não</td>
  </tr>
<table>
