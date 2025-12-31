from fastapi import FastAPI, Request
import uvicorn
import os

app = FastAPI()

@app.post("/hit")
async def receive_hit(request: Request):
    # 1. Parse the JSON payload sent from your monitor
    data = await request.json()
    
    # 2. Log to the Render console
    print("\n🚀 --- NEW COMMENT HIT ---")
    print(f"Author: {data.get('author')}")
    print(f"Comment: {data.get('text')}")
    print(f"Video ID: {data.get('video_id')}")
    print(f"Timestamp: {data.get('timestamp')}")
    print("---------------------------\n")

    # 3. Return a 200 OK status
    return {"status": "received", "comment_id": data.get("comment_id")}

if __name__ == "__main__":
    # Render sets a PORT environment variable automatically
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
