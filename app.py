from flask import Flask, render_template, request
import datetime, os

app = Flask(__name__)
LOG_PATH = os.path.join(os.path.dirname(__file__), 'logs', 'access.log')

def log_access(page):
    os.makedirs('logs', exist_ok=True)
    with open(LOG_PATH, 'a') as f:
        f.write(f"{datetime.datetime.now()} | IP:{request.remote_addr} | {request.method} | /{page}\n")

@app.context_processor
def inject_now():
    return {'now': datetime.datetime.now()}

@app.route('/')
def index():
    log_access('index')
    return render_template('index.html')

@app.route('/modulo1')
def modulo1():
    log_access('modulo1')
    return render_template('modulo1.html')

@app.route('/modulo2')
def modulo2():
    log_access('modulo2')
    return render_template('modulo2.html')

@app.route('/modulo3')
def modulo3():
    log_access('modulo3')
    return render_template('modulo3.html')

@app.route('/modulo4')
def modulo4():
    log_access('modulo4')
    return render_template('modulo4.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
