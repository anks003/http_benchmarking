from sanic import Sanic
from sanic.response import json

app = Sanic(log_config=None)

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,access_log=False)

