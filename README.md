# MessedUpFarm

A game about a cow, a pig and potentially a goat but haven't gotten that far yet.

## Repo Layout

docs/ - Alright we got docs for docs.
client/ - We are using the game engine of unity. That's how we play. Need to know (or learn) C#
server/ - Server is good old python. We know it. We like it.
scripts/ - For any task you are going to do more then once. We don't like wasted time. We like automation or at least tyler does. Remember DRY (Don't Repeat Yourself).

Note we need to figure out how a Makefile works.

### Server

#### TECH STACK

- Python (>=3.12)
- uv instead of pip.

```
pip install uv
uv add {package}
```

- Code Style

Follow PEP-8
We are using mypy for type checking. ruff for linting black for formatting.

For our server, we are using FastAPI to handle requests. With FastAPI we can do some cool things and we get some swag swagger docs! (If you don't know what swagger docs are ask chat.) Run the server with the following. `uv run uvicorn server.src.server:app --reload` and then go to this address http://127.0.0.1:8000/docs for the docs.

So our flow is going to be the following:

Server --> Handler --> Service --> DB

### Client

#### TECH STACK

- C#
- Unity

:
