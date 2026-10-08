import asyncio
from exceptions import RepositoryError


async def analyze_repository(repository_url: str) -> str:
    await asyncio.sleep(2)
    if repository_url == "bad-repository":
        raise RepositoryError("Invalid repository URL")
    else:
        return f"Repository analysis for {repository_url} completed."


async def search_documentation(query: str) -> str:
    await asyncio.sleep(1)
    if query == "bad-query":
        raise RepositoryError("Invalid documentation query")
    else:
        return f"Documentation search for '{query}' completed."
