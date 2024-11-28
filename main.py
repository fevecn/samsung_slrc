from flask import Flask, render_template, request
import samsungctl
import yaml

app = Flask(__name__)


def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Carrega a configuração do config.yaml
config = load_config('config.yaml')

class SingletonRemote:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonRemote, cls).__new__(cls)
            cls._instance.remote = samsungctl.Remote(config)
        return cls._instance

# Função para enviar comandos para a TV
def send_command(command):
    try:
        singleton = SingletonRemote()
        singleton.remote.control(command)
        return "Success"  # Retorna sucesso quando o comando é enviado com sucesso
    except Exception as e:
        return str(e)  # Retorna a mensagem de erro em caso de exceção

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_command', methods=['POST'])
def send_command_route():
    command = request.form['command']
    result = send_command(command)
    return result  # Retorna o resultado de send_command

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

