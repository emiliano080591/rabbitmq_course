import pika


def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue="hello")

    for n in range(1, 20):
        message = 'Sent hello world->{}'.format(n)
        channel.basic_publish(exchange="", routing_key="hello", body=message)
        print("[x] {}".format(message))

    connection.close()


if __name__ == "__main__":
    run()
