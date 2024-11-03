from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = [
            {'nome': 'Ana Carolina Silva', 'cpf': 12345678901 , 'protestos' : 'provedora Mynet'},
            {'nome': 'Bruno Henrique Oliveira', 'cpf': 98765432109 , 'protestos' : "" },
            {'nome': 'Camila Fernanda Santos', 'cpf': 11223344556 , 'protestos' : 'Jussara comercio' },
            {'nome': 'Daniel Augusto Pereira', 'cpf': 66554433221 , 'protestos' : ""},
            {'nome': 'Eduardo Luiz Costa', 'cpf': 10293847561 , 'protestos' : 'Provedora Cartnet'},
            {'nome': 'Fernanda Maria Almeida', 'cpf': 56473829100 , 'protestos' : 'Lojas João'},
            {'nome': 'Gabriel Antônio Souza', 'cpf': 90817263547 , 'protestos' : 'provedora silva' },
            {'nome': 'Helena Beatriz Rocha', 'cpf': 37482910563 , 'protestos' : ""},
            {'nome': 'Igor Rafael Mendes', 'cpf': 74628193057 , 'protestos' : 'Lojão do Povo' },
            {'nome': 'Juliana Cristina Ribeiro', 'cpf': 19283746509 , 'protestos' : 'Provedora carlos' },
            {'nome': 'Mariana Vitória Gomes', 'cpf': 28374659102 , 'protestos' : ""},
            {'nome': 'Nicolas Felipe Araújo', 'cpf': 47583920164 , 'protestos' : 'Varejo de roupas'},
            {'nome': 'Olivia Sofia Lima', 'cpf': 65748392018 , 'protestos' : 'Provedora JA net'},
            {'nome': 'Pedro Henrique Ferreira', 'cpf': 83920174658 , 'protestos' : 'Comercio MeM'}
            ]



@app.route("/")
def index():
    lista = usuarios
    return render_template("index.html", lista = lista)

@app.route("/consulta", methods=['POST', 'GET'])
def consulta():
    resposta = None
    cpf_digitado = request.args.get('cpf')
    if cpf_digitado:
        try:
            cpf_digitado = int(cpf_digitado)
            for i in usuarios:
                if i['cpf'] == cpf_digitado:
                    resposta = i
                    break 
                else:
                    resposta = ("usuario não encontrado")
        except ValueError:
            resposta = ("Cpf invalido, por favor insira apenas numeros")
    return render_template("consulta.html", resposta = resposta)

@app.errorhandler(404)
def page_not_fouder(e):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
