import asyncio
import sys

import microcore as mc
from microcore import ui
import async_typer
import typer
from .bootstrap import bootstrap

app = async_typer.AsyncTyper(
    pretty_exceptions_show_locals=False,
)

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@app.callback(invoke_without_command=True)
def cli(
    ctx: typer.Context,
    prompt: str = typer.Argument(
        None,
        show_default=False,
        help="Input text for the LLM. If not a subcommand, this will be passed as prompt to the LLM."
    ),
):
    bootstrap()
    if not ctx.invoked_subcommand:
        # if prompt is None or blank, show usage/help or maybe launch in REPL/interactive mode
        if prompt is not None:
            asyncio.run(llm(prompt=prompt))
        else:
            # Show help if no subcommand and no prompt
            typer.echo(ctx.get_help())
            raise typer.Exit()


@app.async_command()
async def llm(
    prompt: str = typer.Argument(
        ...,
        help="Input text for the LLM."
    ),
    clean_out: bool = typer.Option(default=False)
):
    def cprint(text):
        print(ui.cyan(text), end='')
    if clean_out:
        print(mc.allm(prompt))
    else:
        await mc.allm(prompt, callbacks=[cprint])