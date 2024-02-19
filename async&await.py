import asyncio

async def greet_after_delay(delay):
    print("Hello")
    await asyncio.sleep(delay)  # Pause execution for 'delay' seconds
    print("World!")

async def main():
    await greet_after_delay(40)

asyncio.run(main())  # Run the main async function
