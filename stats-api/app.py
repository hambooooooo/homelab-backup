from flask import Flask, jsonify
import os, psutil, time

app = Flask(__name__)
start_time = time.time()

@app.route('/api/stats')
def stats():
    load1, _, _ = os.getloadavg()
    mem = psutil.virtual_memory()
    uptime_sec = time.time() - start_time
    uptime_str = time.strftime('%H:%M:%S', time.gmtime(uptime_sec))
    return jsonify({
        'cpuLoad': f'{load1:.2f}',
        'memUsage': f'{mem.percent}%',
        'uptime': uptime_str
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9100)
