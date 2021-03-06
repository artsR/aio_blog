from aiohttp import web



async def home(request):
    return web.Response(text='Bienvenido, sientate como en casa')
