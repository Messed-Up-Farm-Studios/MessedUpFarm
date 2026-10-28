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

##### Tests

We are actually going to do it this time! Postive and Negative tests please and cover edge cases. If you're a boss you'll write your tests first.

We will be using pytest. Make sure the test folder mimics src in folder layout and file layout just with 'test\_' infront.

### Client

#### TECH STACK

- C#
- Unity

Unity deals with scenes and objects.

Bootstrap --> SplashScreen --> LoadingScreen --> MainMenu

Awake() at the start
INitalize - right after start

Scripts:

- GameState

- GameManager

##### GameState

- Gamestate is an enum. Holds what states the game can be in.

##### GameManager

- GameManager tracks game state and coordinates game play
