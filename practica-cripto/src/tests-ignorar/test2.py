import asyncio
import logging

logging.basicConfig(level=logging.INFO)


async def my_task():
    logging.info("Task started")
    logging.info("Task started")
    await asyncio.sleep(5)  # Simulate some asynchronous work
    logging.info("Task finished")
    return "Task result"


async def main():
    logging.info("Main started")

    # Create and run a Task
    logging.info("enteringted")

    task = await my_task()
    task2 = await my_task()

    await asyncio.sleep(3)

    # Set the Future result after some delay

    # Log the results of both
    logging.info(f"Task result: {task}")

    logging.info("Main finished")

# Run the main function
asyncio.run(main())
