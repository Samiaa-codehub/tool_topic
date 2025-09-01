import rich
from agents import Agent,Runner,function_tool
from connection import config
import asyncio
from dotenv import load_dotenv

load_dotenv()
@function_tool(name_override="info_get_info",description_override="Get information about various topics.")
def get_info():
    ## Doc-string
    """
    Get information about various topics.
    """
    return "You are a helpful assistant that provides information about various topics."
info_agent=Agent(
    name="InfoAgent",
    instructions="An agent that provides information on various topics.",
    tools=[get_info],
)
async def main():
    response = await Runner.run(info_agent,"what is the capital of France?",run_config=config)
    rich.print(response.new_items)
    print("Response:", response.final_output)
if __name__ == "__main__":
    asyncio.run(main())