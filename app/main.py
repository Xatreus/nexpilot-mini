import asyncio
from services import analyze_repository, search_documentation
from models import Task
import time

task = Task(
    id="1",
    title="Sample Task",
    description="This is a sample task.",
    repository_url="github.com/xatreus/nexpilot-mini",
)

print(task.model_dump())


async def main():
    start = time.perf_counter()
    result1, result2 = await asyncio.gather(
        analyze_repository("bad-repository"),
        search_documentation("bad-query"),
    )
    elapsed = time.perf_counter() - start
    print(f"elapsed time: {elapsed:0.2f} seconds")
    print(result1)
    print(result2)


if __name__ == "__main__":
    asyncio.run(main())
