import asyncio
import logging
import sys
import os
import shutil

import microcore as mc
import async_typer
import typer
import requests

from .constants import ENV_CONFIG_FILE
from .bootstrap import bootstrap


app = async_typer.AsyncTyper(
    pretty_exceptions_show_locals=False,
)


if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@app.callback(invoke_without_command=True)
def cli(ctx: typer.Context, input=typer.Argument("", help="Input text for the LLM")):
    bootstrap()
    if not ctx.invoked_subcommand:
        asyncio.run(llm(filters=input))


@app.async_command()
async def llm(input: str = typer.Option(..., help="Input text for the LLM")):
    from rich.pretty import pprint
    pprint(input)
