from mcp.server.fastmcp import FastMCP
from tools.orders import register_tools

mcp = FastMCP("Orders MCP Server")
register_tools(mcp)

app = mcp