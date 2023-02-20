import pika
import time


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def callback(ch, method, properties, body):
    n = int(body.decode())
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")
    time.sleep(1)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='fibonacci')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='fibonacci', on_message_callback=callback)
    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == '__main__':
    main()
