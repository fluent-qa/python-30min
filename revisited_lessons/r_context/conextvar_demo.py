import asyncio
import contextvars
import threading

context = threading.local()
context.name="current"


request_id = contextvars.ContextVar('request_id_demo')

async def get_id():
    print(f'Request ID: {request_id.get()}')

async def new_request_coro(req_id):
    # Set Value
    request_id.set(req_id)
    await get_id()
    print(f'Request ID (Outer): {request_id.get()}')


async def main():
    tasks = []
    for req_id in range(1, 5):
        tasks.append(asyncio.create_task(new_request_coro(req_id)))

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
