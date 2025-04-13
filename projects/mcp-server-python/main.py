from fastapi import FastAPI
from modelcontext.fastapi import create_mcp_app
from tools.orders import tools

# Create the FastAPI app with MCP tools
app = create_mcp_app(tools=tools)