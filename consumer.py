import pika
from pika.adapters.blocking_connection import BlockingConnection
from pika.connection import ConnectionParameters


"""Параметры реббит для подключения"""
connection_params = ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials('admin', 'admin') # логин и пароль для менеджмента
)

def callback(channel, method, props, body):
    print(f'get message: {body.decode()}')

    channel.basic_ack(delivery_tag=method.delivery_tag) # тут у нас удаление сообщения из очереди

def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue='messages') # создание очереди

            """прослушивание сообщений"""
            ch.basic_consume(
                queue='messages',  # прослушивание конкретной очереди
                on_message_callback=callback,
                auto_ack=False
            )
            print('waiting messages')
            ch.start_consuming()

if __name__ == '__main__':
    main()
