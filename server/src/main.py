from fastapi import FastAPI, WebSocket, WebSocketDisconnect, status, BackgroundTasks
from pydantic import BaseModel, Field

players = []

def save_player(player):
    players.append(player)

class Player(BaseModel):
    name: str = Field(..., min_length=1, max_length=20, description="Player's Real Name", example="Tyler")
    age: int = Field(ge=13, le=100, description="Players Age", example=23)

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_text()
            await ws.send_text(f"Server received: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")

@app.get("/heath")
def health_check():
    return {"status": "ok"}

@app.post("/create/player", status_code=status.HTTP_201_CREATED, tags=["Player", "Create"])
def create_player(player: Player, background_tasks: BackgroundTasks):
    background_tasks.add_task(save_player, player)
    return {"msg": "player created"}

@app.get("/list/players", tags=["Player", "List"])
def list_players():
    return {"msg": "players list",
            "players": players}

