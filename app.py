import psycopg2
from gevent.pywsgi import WSGIServer
from source.server import app


conexion = psycopg2.connect("dbname=inventory user=postgres password=c1nc005os")
cur = conexion.cursor()
cur.execute("select * from tienda")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
