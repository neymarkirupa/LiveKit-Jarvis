import os
from dotenv import load_dotenv
from livekit import api

load_dotenv()

API_KEY = os.getenv("LIVEKIT_API_KEY")
API_SECRET = os.getenv("LIVEKIT_API_SECRET")

def create_token(room="test-room", identity="user1"):
    grant = api.VideoGrants(
        room_join=True,
        room=room,
    )

    at = api.AccessToken(API_KEY, API_SECRET)
    at.identity = identity
    at.grants = grant

    return at.to_jwt()

if __name__ == "__main__":
    token = create_token()
    print("\n=== Your LiveKit Client Token ===\n")
    print(token)
    print("\nPaste this token into your LiveKit web client!\n")