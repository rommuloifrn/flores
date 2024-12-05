# bem-me-quer

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

"joguinho" que implementa TCP e UDP para a disciplina de greycomn

## diagrama de estado do client.py

```mermaid

stateDiagram

[*] --> e1
e1 --> e2
e2 --> e3
e3 --> e4
e4 --> e5
e5 --> e4
e5 --> e6

state "instancia socket TCP" as e1
state "socket tcp se conecta em localhost:5008" as e2
state "instancia socket UDP" as e3
state "envia quantidade de pétalas para o servidor" as e4
state "servidor espera por retirada de pétalas" as e5
state "servidor envia resultado final" as e6

```

## referências

- [Exemplo de cliente-servidor em python by pythonic](https://pythontic.com/modules/socket/udp-client-server-example)
- [Python socket docs](https://docs.python.org/3/library/socket.html#socket.socket.bind)

<br>
<br>
<br>

![](assets/kagome_with_python.jpg)