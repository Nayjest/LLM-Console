import asyncio
import sys
from collections import deque

import microcore as mc
from lm_cli.utils import print_stream
from microcore import ui
from pywin.framework.toolmenu import tools
from rich.pretty import pprint

from .bootstrap import bootstrap

def app():
    asyncio.run(main())

async def main():
    bootstrap()
    if len(sys.argv) <= 1:
        print("LLM is configured and ready for work")
        exit()
    args = sys.argv[1:]
    await ai(args)

async def ai(args):
    prompt_parts = args.copy()
    callbacks = []
    print_result = False

    def set_streaming(enabled: bool):
        nonlocal print_result
        nonlocal callbacks
        print_result = not enabled
        if enabled:
            if print_stream not in callbacks:
                callbacks.append(print_stream)
        else:
            if print_stream in callbacks:
                callbacks.remove(print_stream)

    set_streaming("--no-stream" not in args)
    if "--no-stream" in args:
        prompt_parts.remove("--no-stream")

    if "--explain" in args:
        mc.use_logging()
        set_streaming(False)
        prompt_parts.remove("--explain")

    if args[0] == "--show-mcp":
        mcp_url = args[1]
        await explore_mcp(mcp_url)
        exit()

    use_mcp = False
    mcp: mc.mcp.MCPConnection | None = None
    if "--mcp" in args:
        set_streaming(False)
        use_mcp = True
        mcp_url = args[args.index("--mcp") + 1]
        mcp = await mc.mcp.MCPServer(name="mcp", url=mcp_url).connect()

        prompt_parts.remove("--mcp")
        prompt_parts.remove(mcp_url)
        prompt_parts = ["[User Request]\n"] + prompt_parts
        prompt_parts.append("\n"+mc.prompt("""
        [Tools]
        Use tools to satisfy the user request.
        {{ tools }}}
        (!) Answer with valid JSON to use a tool
        """, tools=mcp.tools, remove_indent=True))

    prompt = " ".join(prompt_parts)
    hist = [mc.UserMsg(prompt)]
    llm_answer = await mc.allm(hist, callbacks=callbacks)
    mcp_res = ...
    while use_mcp:
        try:
            mcp_res = await llm_answer.to_mcp(mcp)
        except mc.mcp.WrongMcpUsage as e:
            break
        if mcp_res is not ...:
            hist.append(mc.AssistantMsg("MCP Response:"+mcp_res))
            llm_answer = await mc.allm(hist)

    if print_result:
        print(llm_answer)

async def explore_mcp(mcp_url: str):
    print("Exploring MCP at:", ui.green(mcp_url), "...")
    mcp = await mc.mcp.MCPServer(name="examinee", url=mcp_url).connect()
    print(ui.gray("Connected to MCP server!"))
    tools = mcp.tools
    print(f"Available tools:\n{ui.cyan(tools)}")
