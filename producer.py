import pika
from pika.adapters.blocking_connection import BlockingConnection
from pika.connection import ConnectionParameters


"""Параметры реббит для подключения"""
connection_params = ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials('admin', 'admin') # логин и пароль для менеджмента
)

def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue='messages') # создание очереди

            """отправка сообщений"""
            ch.basic_publish(
                exchange='', #  по дефолту direct.exchange
                routing_key='messages',  # отправка в конкретную очередь
                body='hello Jibek' # тело сообщения
            )
            print('message sent')

if __name__ == '__main__':
    main()
