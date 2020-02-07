#! /usr/bin/env pipenv run python3

"""
This file is the entry point for the server.
It should always be called from the command line.
"""
import os
import re

import traceback
import aiohttp
from aiohttp import web

import src.env_var_importer  # pylint: disable=unused-import
import src.slack as Slack

async def server_entry_point(request):
    """Entry point for all requests to the server"""
    if 'secret' in request.headers:
      if request.headers['secret'] == '12345':
        return web.json_response(status=200, data={"message": "well done"})

    return web.json_response(status=403, data={"error": "thanks but no thanks"})


if __name__ == '__main__':
    #Slack.send_msg("Server has come online")
    LISTEN_PORT = 12021
    try:
        LISTEN_PORT = os.environ['PORT']
    except KeyError:
        print(
            "PORT environment variable doesn't exist, using default port = %s" % LISTEN_PORT)

    APP = web.Application()
    APP.add_routes([web.route('*', r'/{tail:.*}', server_entry_point)])
    web.run_app(APP, port=LISTEN_PORT)
