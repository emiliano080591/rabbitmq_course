import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='br_exchange', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

print("Subscriber queue_name =", queue_name)

channel.queue_bind(exchange='br_exchange', queue=queue_name)

print('[*] waiting for the messages')


def callback(ch, method, properties, body):
    print('[x] %r' % body)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
