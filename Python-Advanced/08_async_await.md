# Asynchronous Programming with `async` and `await`

## Key Concepts

### 1. **`async` Keyword**

- The `async` keyword is used to define an **asynchronous function** (also called a **coroutine**).
- When you mark a function with `async`, it becomes capable of running concurrently with other tasks. However, it doesn't automatically run concurrently; it needs to be awaited or scheduled using an event loop.
- Example:
  ```python
  async def fetch_data():
      # Simulate a network request
      return "Data fetched"
  ```

### 2. **`await` Keyword**

- The `await` keyword is used to pause the execution of an asynchronous function until the awaited task completes.
- It ensures that the next line of code runs only after the awaited operation finishes.
- Example:
  ```python
  async def main():
      data = await fetch_data()  # Wait for fetch_data to complete
      print(data)
  ```

---

## Why Use Asynchronous Programming?

Asynchronous programming is particularly useful when dealing with **I/O-bound tasks**, such as:

- Making API requests.
- Reading/writing files.
- Querying databases.

In these cases, the program often has to wait for external systems to respond. Using `async` and `await` allows the program to perform other tasks while waiting, improving efficiency.

---

## Example: Fetching Pokémon Data

### Code Example 1: Basic `async` and `await`

```python
import asyncio
from random import randint
from req_http import JSONObject, http_get

MAX_POKEMON = 898

async def get_pokemon(pokemon_id: int) -> JSONObject:
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    return await http_get(pokemon_url)  # Wait for the API response

async def main() -> None:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon = await get_pokemon(pokemon_id)  # Wait for the Pokémon data
    print(pokemon["name"])

if __name__ == "__main__":
    asyncio.run(main())  # Run the main coroutine
```

#### Explanation:

1. **`get_pokemon` Function**:

   - Fetches Pokémon data from the PokéAPI using an asynchronous HTTP GET request.
   - The `await` keyword ensures the function waits for the API response before proceeding.

2. **`main` Function**:

   - Generates a random Pokémon ID and fetches the corresponding Pokémon data.
   - The `await` keyword ensures the program waits for the data before printing the Pokémon's name.

3. **`asyncio.run`**:
   - This function runs the `main` coroutine and manages the event loop.

---

### Code Example 2: Synchronous vs Asynchronous Execution

```python
import asyncio
from random import randint
from time import perf_counter
from req_http import http_get, http_get_sync

MAX_POKEMON = 898

def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)  # Synchronous request
    return str(pokemon["name"])

async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)  # Asynchronous request
    return str(pokemon["name"])

async def main() -> None:
    # Synchronous version
    time_before = perf_counter()
    for _ in range(20):
        get_random_pokemon_name_sync()
    print(f"Total time (synchronous): {perf_counter() - time_before}")

    # Asynchronous version
    time_before = perf_counter()
    await asyncio.gather(*[get_random_pokemon_name() for _ in range(20)])
    print(f"Total time (asynchronous): {perf_counter() - time_before}")

if __name__ == "__main__":
    asyncio.run(main())
```

#### Explanation:

1. **Synchronous Execution**:

   - The `get_random_pokemon_name_sync` function makes 20 sequential API requests.
   - Each request waits for the previous one to complete, resulting in slower execution.

2. **Asynchronous Execution**:

   - The `get_random_pokemon_name` function makes 20 concurrent API requests using `asyncio.gather`.
   - All requests are launched simultaneously, significantly reducing the total execution time.

3. **Performance Comparison**:
   - Synchronous: Takes ~2 seconds (each request waits for the previous one).
   - Asynchronous: Takes ~0.9 seconds (requests are made concurrently).

---

## Key Takeaways

1. **Concurrency with `asyncio.gather`**:

   - `asyncio.gather` allows you to run multiple asynchronous tasks concurrently.
   - Example:
     ```python
     await asyncio.gather(task1(), task2(), task3())
     ```

2. **Rate Limiting**:

   - APIs often have rate limits to prevent abuse.
   - Ensure your application respects these limits by controlling the number of concurrent requests.

3. **Event Loop**:

   - Asynchronous programming in Python relies on an **event loop** to manage and schedule tasks.
   - Use `asyncio.run` to start the event loop and execute your coroutines.

4. **Error Handling**:
   - Always handle exceptions in asynchronous code to avoid unhandled errors crashing your program.

---

## Common Mistakes and Fixes

1. **Forgetting to `await`**:

   - Mistake:
     ```python
     async def main():
         data = fetch_data()  # Missing await
         print(data)
     ```
   - Fix:
     ```python
     async def main():
         data = await fetch_data()  # Correct
         print(data)
     ```

2. **Running Coroutines Without `asyncio.run`**:

   - Mistake:
     ```python
     main()  # Coroutine not awaited
     ```
   - Fix:
     ```python
     asyncio.run(main())  # Correct
     ```

3. **Ignoring Rate Limits**:
   - Mistake:
     ```python
     await asyncio.gather(*[fetch_data() for _ in range(1000)])  # Too many requests
     ```
   - Fix:
     ```python
     # Use a semaphore to limit concurrency
     semaphore = asyncio.Semaphore(10)  # Limit to 10 concurrent requests
     async def limited_fetch():
         async with semaphore:
             return await fetch_data()
     await asyncio.gather(*[limited_fetch() for _ in range(1000)])
     ```

---

## Conclusion

Asynchronous programming with `async` and `await` is a powerful tool for improving the performance of I/O-bound applications. By running tasks concurrently, you can significantly reduce waiting times and make your applications more efficient. However, always be mindful of API rate limits and ensure proper error handling to build robust systems.
