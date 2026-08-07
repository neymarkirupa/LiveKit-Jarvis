from dotenv import load_dotenv
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import google
from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION

load_dotenv()

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTION,
            llm=google.beta.realtime.RealtimeModel(
                voice="Aoede",
                temperature=0.8,
            ),
        )

    async def generate_reply(self, instructions: str, user_text: str) -> str:
        session = AgentSession()
        await session.start(
            agent=self,
            room_input_options=RoomInputOptions(video_enabled=False),
        )
        reply = await session.generate_reply(instructions, user_text)
        return reply
