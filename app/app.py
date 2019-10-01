import json
import logging
import os
from redis import Redis
from quart import Quart, request, render_template, redirect

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

app = Quart(__name__)
app.redis = Redis(host='redis', decode_responses = True)

@app.route('/greeter', methods=['POST'])
async def greeter():
    """Endpoint for greeting"""
    form = await request.form
    name = request.args.get('name') or form.get('name')
    with open('../data/visitors.txt', 'w') as f:
        f.writelines([name])
    pubsub = app.redis.pubsub()
    pubsub.subscribe('response:'+name)
    if name:
        app.redis.rpush('queue', json.dumps({'name': name}))
        logging.info(f'Pushed {name} onto queue')
    else:
        return {'error': 'No valid request received. Pass parameters as form- or URL-parameters.'}
    for item in filter(lambda payload: payload.get('type') == 'message', pubsub.listen()):
        data = json.loads(item['data'])['response']
        logging.info(f'Returning {data} to client')
        return {'data': data}

@app.route('/', methods=['GET'])
def get_index_page():
    """Redirect to the orders page"""
    return redirect('/index')

@app.route('/index', methods=['GET'])
async def page():
    return await render_template('/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
