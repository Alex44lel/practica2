import asyncio
import logging

logging.basicConfig(level=logging.INFO)

# A coroutine that will be run as a Task


async def my_task():
    logging.info("Task started")
    await asyncio.sleep(2)  # Simulate some asynchronous work
    logging.info("Task finished")
    return "Task result"

# A function to set a result in a Future after a delay


async def set_future_value(future):
    logging.info("Setting future value...")
    await asyncio.sleep(1)  # Simulate some delay
    future.set_result("Future result")
    logging.info("Future value set")


async def main():
    logging.info("Main started")

    # Create and run a Task
    task = asyncio.create_task(my_task())
    print(task)

    # Create a Future
    future = asyncio.Future()
    print(future)

    # Set the Future result after some delay
    asyncio.create_task(set_future_value(future))

    # Wait for both the Task and the Future to complete
    task_result = await task
    future_result = await future

    # Log the results of both
    logging.info(f"Task result: {task_result}")
    logging.info(f"Future result: {future_result}")

    logging.info("Main finished")

# Run the main function
asyncio.run(main())
