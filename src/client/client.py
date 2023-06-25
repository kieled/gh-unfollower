from python_graphql_client import GraphqlClient
import aiofiles

from .config import settings

client = GraphqlClient(endpoint="https://api.github.com/graphql")


async def load_schema(schema_filename: str):
    async with aiofiles.open(f'./src/graphql/{schema_filename}.graphql', 'r') as f:
        return await f.read()


async def prepare_request(schema_filename: str, variables: dict):
    query = await load_schema(schema_filename)
    return await client.execute_async(query, variables, headers={
        'Authorization': f'Bearer {settings.TOKEN}',
        'User-Agent': settings.UA
    })
