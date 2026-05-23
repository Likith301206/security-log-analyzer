from flask import Flask, request, send_file, jsonify
import sqlite3

app = Flask(__name__)

# DATABASE SETUP
def init_db():

    conn = sqlite3.connect('smart.db')

    cursor = conn.cursor()

    # DEVICE TABLE
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS devices(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        type TEXT,
        location TEXT,
        status TEXT
    )
    ''')

    # LOG TABLE
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id INTEGER,
        activity TEXT
    )
    ''')

    # THREAT TABLE
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS threats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id INTEGER,
        activity TEXT,
        severity TEXT
    )
    ''')

    conn.commit()
    conn.close()

# HOME PAGE
@app.route('/')
def home():
    return send_file('index.html')

# ADD DEVICE
@app.route('/addDevice', methods=['POST'])
def add_device():

    data = request.data.decode()

    values = data.split(',')

    conn = sqlite3.connect('smart.db')

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO devices(name, type, location, status) VALUES (?, ?, ?, ?)",
        (values[0], values[1], values[2], values[3])
    )

    conn.commit()
    conn.close()

    return "Device Added Successfully"

# ADD LOG + THREAT DETECTION
@app.route('/addLog', methods=['POST'])
def add_log():

    data = request.data.decode()

    values = data.split(',')

    device_id = values[0]
    activity = values[1]

    conn = sqlite3.connect('smart.db')

    cursor = conn.cursor()

    # INSERT LOG
    cursor.execute(
        "INSERT INTO logs(device_id, activity) VALUES (?, ?)",
        (device_id, activity)
    )

    # THREAT DETECTION
    severity = "Safe"

    if activity.lower() == "failed login":
        severity = "Medium"

    elif activity.lower() == "unauthorized access":
        severity = "High"

    elif activity.lower() == "malware detected":
        severity = "Critical"

    # INSERT THREAT
    if severity != "Safe":

        cursor.execute(
            "INSERT INTO threats(device_id, activity, severity) VALUES (?, ?, ?)",
            (device_id, activity, severity)
        )

    conn.commit()
    conn.close()

    return f"Log Added | Threat Level: {severity}"

# VIEW DEVICES
@app.route('/getDevices')
def get_devices():

    conn = sqlite3.connect('smart.db')

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM devices")

    devices = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jsonify(devices)

# VIEW THREATS
@app.route('/getThreats')
def get_threats():

    conn = sqlite3.connect('smart.db')

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM threats")

    threats = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return jsonify(threats)

# DELETE ALL DEVICES
@app.route('/clearDevices')
def clear_devices():

    conn = sqlite3.connect('smart.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM devices")

    conn.commit()
    conn.close()

    return "All Devices Deleted"

# DELETE ALL LOGS
@app.route('/clearLogs')
def clear_logs():

    conn = sqlite3.connect('smart.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM logs")

    conn.commit()
    conn.close()

    return "All Logs Deleted"

# DELETE ALL THREATS
@app.route('/clearThreats')
def clear_threats():

    conn = sqlite3.connect('smart.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM threats")

    conn.commit()
    conn.close()

    return "All Threats Deleted"

if __name__ == '__main__':

    init_db()

    app.run(debug=True)