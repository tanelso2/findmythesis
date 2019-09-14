#from flask import Flask, redirect, render_template, url_for
# import werkzeug.exceptions
from aiohttp import web
import aiohttp_jinja2
import jinja2
import asyncio

from thesis import get_thesis_topic, fetch_loop

#app = Flask(__name__)


@aiohttp_jinja2.template('index.html')
async def handle(_):
    return {'thesis': await get_thesis_topic()}

@aiohttp_jinja2.template('index.html')
async def test(_):
    return {'thesis': "Testing: A survey of secret access & simplicity in an age of containers"}


app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/test', test)])
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))


loop = asyncio.get_event_loop()
print("Setting up task")
loop.create_task(fetch_loop())
loop.set_debug(True)


async def handle_404(_, __):
    return web.HTTPFound('/')


def error_pages(overrides):
    async def middleware(app, handler):
        async def middleware_handler(request):
            try:
                response = await handler(request)
                override = overrides.get(response.status)
                if override is None:
                    return response
                else:
                    return await override(request, response)
            except web.HTTPException as ex:
                override = overrides.get(ex.status)
                if override is None:
                    raise
                else:
                    return await override(request, ex)
        return middleware_handler
    return middleware


error_middleware = error_pages({404: handle_404})
app.middlewares.append(error_middleware)

# def thesis():
#     return render_template('index.html', thesis=get_thesis_topic())
#
#
# @app.route('/test')
# def test():
#     return render_template('index.html',
#                            thesis='Testing: A survey of secret access & simplicity in an age of containers')


# @app.errorhandler(werkzeug.exceptions.NotFound)
# def redirect_to_main(_):
#     return redirect(url_for('thesis'))

if __name__ == '__main__':
    web.run_app(app)
