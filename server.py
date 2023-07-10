from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def display_ads():
    conn = psycopg2.connect(
        host="db",
        database="postgres",
        user="postgres",
        password="Maradona1!"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ads LIMIT 500")
    ads = cursor.fetchall()
    conn.close()
    return render_template('index.html', ads=ads)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
