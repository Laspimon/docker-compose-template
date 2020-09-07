import logging
import os
import json
from redis import Redis

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

def consumer(redis, queues = None):
    if queues is None:
        queues = ['queue']
    while True:
        consume(redis, queues)

def consume(redis, queues):
    popped = redis.blpop(queues)
    if popped is None:
        return
    payload = json.loads(popped[1])
    name = payload.get('name')

    logging.info(f'2 Popped {name} off of the queue')
    if name:
        logging.info(f'3 Publishing {name} to response:{name}')
        redis.publish('response:'+name, json.dumps({'response': 'Hello ' + name}))

if __name__ == '__main__':
    redis = Redis(host='redis', decode_responses=True)
    consumer(redis)