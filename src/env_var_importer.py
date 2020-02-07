"""
This module imports environment variables from file
The module also creates some global variables
"""

import os
import re
import aiohttp

print("Import Environment Variables")

# load the environment variables if they haven't been loaded yet
if not os.environ.get('SECRET'):
    print("Environment variables don't exist. Importing from local dotenv")
    from dotenv import load_dotenv  # pylint: disable=import-error
    from pathlib import Path
    ENV_PATH = "%s/.env.development" % Path('.')
    print("ENV_PATH = %s" % ENV_PATH)
    load_dotenv(dotenv_path=ENV_PATH)