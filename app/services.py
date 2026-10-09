import asyncio
from exceptions import DocumentationError, RepositoryError
import logging

logger = logging.getLogger(__name__)


async def analyze_repository(repository_url: str) -> str:
    logger.info("Starting repository analysis: %s", repository_url)
    await asyncio.sleep(2)
    try:
        if repository_url == "bad-repository":
            raise RepositoryError("Invalid repository URL")

        return f"Repository analysis for {repository_url} completed."
    except RepositoryError:
        logger.exception(
            "Repository analysis failed: %s",
            repository_url,
        )
        raise


async def search_documentation(query: str) -> str:
    logger.info("Starting documentation search: %s", query)
    await asyncio.sleep(1)

    try:
        if query == "bad-query":
            raise DocumentationError("Invalid documentation query")

        return f"Documentation search for '{query}' completed."
    except DocumentationError:
        logger.exception("Error occurred while searching documentation: %s", query)
        raise
