# **Turning Synchronous Code into Asynchronous Code in Python**

## **Introduction**

When working with Python, you may encounter libraries that only support synchronous operations. However, you might need to make these operations run concurrently with other tasks.

In this lesson, we'll explore how to convert synchronous functions into asynchronous ones using `asyncio.to_thread`. We will also see how `asyncio.gather` can be used to run multiple asynchronous tasks concurrently.

---

## **Problem Statement**

You have a synchronous function that makes an HTTP request using the `requests` library. Since `requests` is inherently synchronous, it blocks the execution of other tasks until the request is complete. We want to convert this function to an asynchronous one so that it can run concurrently with other tasks.

---

## **Example Code**

### **Initial Synchronous Implementation**

```python
import asyncio
import time
import requests

async def counter(until: int = 10) -> None:
    now = time.perf_counter()
    print("Started counter")
    for i in range(until):
        last = now
        await asyncio.sleep(0.01)
        now = time.perf_counter()
        print(f"{i}: was asleep for {now - last:.4f}s")

def send_request(url: str) -> int:
    print("Sending HTTP request")
    response = requests.get(url)
    return response.status_code

async def main() -> None:
    status_code = send_request("https://www.google.com")
    print(f"Got HTTP response with status code {status_code}")
    await counter()

if __name__ == "__main__":
    asyncio.run(main())
```

### **Issue in the Above Code**

- The `send_request` function is blocking, meaning the counter starts only after the request completes.
- We want the counter to run concurrently with the HTTP request.

---

## **Converting Synchronous Code to Asynchronous**

To fix this, we use `asyncio.to_thread`, which allows us to run a blocking function asynchronously without modifying its implementation.

### **Updated Code (Using `asyncio.to_thread`)**

```python
async def main() -> None:
    status_code = await asyncio.to_thread(send_request, "https://www.google.com")
    print(f"Got HTTP response with status code {status_code}")
    await counter()
```

**Key Fixes:**

- We wrapped `send_request` with `asyncio.to_thread`.
- This allows the function to execute in a separate thread without blocking the event loop.

---

## **Using `asyncio.gather` for Concurrent Execution**

A better approach is to use `asyncio.gather` to run both the HTTP request and counter concurrently.

### **Final Corrected Code**

```python
async def send_async_request(url: str) -> int:
    return await asyncio.to_thread(send_request, url)

async def main() -> None:
    status_code, _ = await asyncio.gather(
        send_async_request("https://www.google.com"),
        counter()
    )
    print(f"Got HTTP response with status code {status_code}")
```

**Key Improvements:**

- Introduced `send_async_request`, which makes `send_request` asynchronous using `asyncio.to_thread`.
- Used `asyncio.gather` to execute both `send_async_request` and `counter` concurrently.
- Now, the counter starts immediately without waiting for the HTTP response.

---

## **Practical Example from Previous Lecture**

In a previous lesson, we implemented a helper function to make HTTP GET requests asynchronously.

### **Helper Function: `http_get`**

```python
import asyncio
import requests

JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]

def http_get_sync(url: str) -> JSONObject:
    response = requests.get(url)
    return response.json()

async def http_get(url: str) -> JSONObject:
    return await asyncio.to_thread(http_get_sync, url)
```

This function uses `asyncio.to_thread` to convert a synchronous `requests.get` call into an asynchronous function.

---

## **Conclusion**

- `asyncio.to_thread` is a simple way to run synchronous functions asynchronously without modifying their implementation.
- `asyncio.gather` allows multiple asynchronous tasks to run concurrently.
- These techniques are particularly useful when working with I/O-bound operations like API calls and database queries.

By using these concepts, you can make your Python applications more efficient and responsive, especially when dealing with network communication.

**Next Topic:** Iterators in Python 🚀
