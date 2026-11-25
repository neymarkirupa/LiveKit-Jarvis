# LiveKit Jarvis

A voice-based AI Assistant backend powered by **LiveKit** and **FastAPI**, modeled after an Iron Man-style AI named "Nova".

## Features
- Real-time voice interaction using Google's generative AI (Aoede voice).
- A REST API endpoint (`/api/ask`) via FastAPI for text-based fallback or integration.
- Custom assistant persona ("Nova"): acts as a classy, slightly sarcastic butler.
- Tool-calling framework setup (currently empty, ready for expansion).

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables:**
   Create a `.env` file in the root directory (you can use `.env.example` as a template) and add your LiveKit credentials:
   ```env
   LIVEKIT_API_KEY="your_api_key_here"
   LIVEKIT_API_SECRET="your_api_secret_here"
   ```

3. **Generate a Client Token:**
   If you need a token to connect a web client for testing, run the token generation script:
   ```bash
   python generate_token.py
   ```
   *This will output a JWT you can use to connect to `test-room`.*

4. **Run the Server:**
   Start the FastAPI backend:
   ```bash
   python server.py
   ```
   The API will be available at `http://localhost:5000/api/ask`.

## Architecture
- `agent.py`: Defines the `Assistant` class leveraging the LiveKit Agent framework and Google Realtime Model.
- `server.py`: FastAPI application serving the assistant endpoints.
- `prompts.py`: System prompts controlling the AI's persona and behavior.
- `tools.py`: Placeholder for custom functions the AI can invoke.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).
