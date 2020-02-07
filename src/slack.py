"""
This file sends slack messages using slack's webhook interface
"""
import os
import datetime
import traceback

import asyncio
from aiohttp import ClientSession

import src.env_var_importer as EnvVars  # pylint: disable=unused-import

SLACK_URL = os.environ.get('SLACK_URL')

async def async_send_slack_message(message="", slack_url=""):
    """
    This function should never be called directly
    Async send slack message to provided webhook url
    """
    if not message:
        print("ERROR: asyncSendSlackMessage called with message length <= 0")
        return

    if not slack_url:
        print("ERROR: SLACK_POST_URL env variable not defined!")
        return

    try:
        async with ClientSession() as session:
            slack_msg = {"text": ("%s > %s" % (
                datetime.datetime.now(), message))}
            async with session.post(slack_url, json=slack_msg) as resp:
                if resp.status != 200:
                    print("ERROR: slack post returned with\n" +
                          "{\n" +
                          "   response_status = %s\n" +
                          "   response_body = %s\n" +
                          "   post_body = %s\n" +
                          "   post_url = %s\n" +
                          "}\n"
                          %
                          resp.status,
                          await resp.text(),
                          formatJson(slack_msg),
                          slack_url)
    except:  # pylint: disable=bare-except
        print("Unexpected error when posting to slack: %s",
              traceback.format_exc())


def send_msg(message="", slack_url=""):
    """
    fire and forget the slack message
    This function can be called to send an async slack message
    """
    loop = asyncio.get_event_loop()
    loop.create_task(async_send_slack_message(message, SLACK_URL))
