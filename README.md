# Caixa Eletrônico API

## Descrição

Esta API simula o funcionamento de um caixa eletrônico. Recebe um valor de saque desejado e retorna a quantidade de cédulas necessárias, utilizando a menor quantidade de cédulas possível. As cédulas consideradas são: 100, 50, 20, 10, 5 e 2.

## Endpoints

### POST /api/saque

-  **Descrição**: Realiza o saque com a menor quantidade de cédulas.
-  **Entrada**:

   ```json
   {
      "valor": 380
   }
   ```

-  **Saída**
   {
   "100": 3,
   "50": 1,
   "20": 1,
   "10": 1,
   "5": 0,
   "2": 0
   }

**Instruções para execução**

1. Clone o repositório:
   (git bash)

git clone <URL do Repositório>
cd caixa_eletronico

2. Crie um ambiente virtual e ative-o:

python -m venv venv
venv\Scripts\activate

3. Instale as dependências:

pip install -r requirements.txt

4. Execute a aplicação:

python app.py

5. Acesse a API em http://localhost:5000/api/saque
# caixa_eletronico
