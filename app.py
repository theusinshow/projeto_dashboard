from flask import Flask, render_template
import pandas as pd
import os

# Criação da aplicação Flask
app = Flask(__name__)

# Carregar o arquivo CSV
try:
    data = pd.read_csv('data/hardware_data.csv')
except FileNotFoundError:
    print("Erro: Arquivo 'hardware_data.csv' não encontrado na pasta 'data'.")
    data = pd.DataFrame()  # Cria um DataFrame vazio para evitar erros.

@app.route('/')
def index():
    # Página inicial com links para cada categoria
    return render_template('index.html')

@app.route('/gpu')
def gpu_dashboard():
    gpu_data = data[data['category'] == 'GPU']
    return render_template('gpu_dashboard.html', data=gpu_data.to_dict(orient='records'))

@app.route('/cpu')
def cpu_dashboard():
    cpu_data = data[data['category'] == 'CPU']
    return render_template('cpu_dashboard.html', data=cpu_data.to_dict(orient='records'))

@app.route('/motherboard')
def motherboard_dashboard():
    motherboard_data = data[data['category'] == 'Motherboard']
    return render_template('motherboard_dashboard.html', data=motherboard_data.to_dict(orient='records'))

# Executar a aplicação Flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
