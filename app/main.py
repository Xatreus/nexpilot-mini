import asyncio
from exceptions import RepositoryError, DocumentationError
from services import analyze_repository, search_documentation
from models import Task
import time
import logging

task = Task(
    id="1",
    title="Sample Task",
    description="This is a sample task.",
    repository_url="github.com/xatreus/nexpilot-mini",
)

print(task.model_dump())

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    logger.info("Starting main function")

    results = await asyncio.gather(
        analyze_repository("bad-repository"),
        search_documentation("bad-query"),
        return_exceptions=True,
    )

    for result in results:
        if isinstance(result, Exception):
            logger.error(
                "Operation failed: %s",
                result,
                exc_info=result,
            )
            print(f"Operation failed: {result}")
        else:
            print(f"Operation succeeded: {result}")


if __name__ == "__main__":
    asyncio.run(main())
