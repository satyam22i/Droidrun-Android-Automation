import asyncio
import os
from dotenv import load_dotenv
from droidrun import DroidAgent, DroidrunConfig
from llama_index.llms.gemini import Gemini

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found in .env")
    exit(1)

async def main():
    config = DroidrunConfig()
    config.agent.app_cards.enabled = True
    config.agent.app_cards.app_cards_dir = "config/app_cards"
    config.agent.codeact.vision = True


    gemini_llm = Gemini(model="models/gemini-2.0-flash", temperature=0.7)
    
    llm_map = {
        "codeact": gemini_llm,
        "app_opener": gemini_llm,
        "planner": gemini_llm
    }

   
    video_context = "A futuristic AI robot writing code automatically on a laptop"
    

    goal = f"""
    1. Open Instagram.
    2. Follow the 'Create Reel' workflow to select the latest video.
    3. When you reach the caption screen:
       - THINK of a short, viral, exciting caption about: "{video_context}"
       - Include 3 relevant hashtags.
       - Type that generated caption into the field.
    4. Complete the process by tapping Share.
    """

    agent = DroidAgent(
        goal=goal,
        config=config,
        llms=llm_map
    )

    print(f"Starting... Topic: {video_context}")
    result = await agent.run()
    print(f"Task finished: {result.success}")

if __name__ == "__main__":

    asyncio.run(main())
