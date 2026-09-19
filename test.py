import asyncio
# from mcp_client_test import get_all_tools, tavily_mcp_search
from mcp_client import get_all_tools



if __name__ == "__main__":
    asyncio.run(get_all_tools())
    # query = "What are the top tourist attractions in Paris?"
    # result = asyncio.run(tavily_mcp_search(query))