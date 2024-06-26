from flask import Flask, request, jsonify

app = Flask(__name__)


def calcular_cedulas(valor):
    cedulas_disponiveis = [100, 50, 20, 10, 5, 2]
    resultado = {str(cedula): 0 for cedula in cedulas_disponiveis}

    for cedula in cedulas_disponiveis:
        if valor >= cedula:
            quantidade = valor // cedula
            resultado[str(cedula)] = quantidade
            valor -= quantidade * cedula

    return resultado


@app.route("/api/saque", methods=["POST"])
def saque():
    data = request.get_json()

    if "valor" not in data or not isinstance(data["valor"], int) or data["valor"] <= 0:
        return jsonify({"error": "Valor inválido. Insira um inteiro positivo."}), 400

    valor = data["valor"]
    resultado = calcular_cedulas(valor)

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)
