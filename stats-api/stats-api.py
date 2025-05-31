from flask import Flask, jsonify
from flask_cors import CORS
import psutil
import socket
import platform
import datetime

app = Flask(__name__)
CORS(app)

def get_system_uptime():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    now = datetime.datetime.now()
    uptime = now - boot_time
    return str(uptime).split('.')[0]  # Remove microseconds

@app.route('/api/stats')
def stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    uptime = get_system_uptime()
    hostname = socket.gethostname()
    os_info = platform.platform()

    return jsonify({
        "cpu": cpu_percent,
        "memory_used": round(mem.used / (1024 ** 3), 2),
        "memory_total": round(mem.total / (1024 ** 3), 2),
        "memory_percent": mem.percent,
        "uptime": uptime,
        "hostname": hostname,
        "os": os_info
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
