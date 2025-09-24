import chainlit as cl
from agents import Agent, Runner
from destination_agent import destination_agent
from exploretion_agent import explore_agent
from booking_agent import booking_agent


# --- Helper function to run an agent and return output ---
async def run_agent(agent, history):
    agent_result = await Runner.run(agent, history)
    return agent_result


# --- Chat Start Event ---
@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])
    welcome_message = (
        "🌟 Welcome to your **AI Travel Designer**!\n\n"
        "I can help you with:"
        "🗺️ Destination ideas."
        "🔍 Exploration tips."
        "🏨 Hotel & ✈️ Flight bookings."
        "👉 Just tell me what you're looking for!"
    )
    await cl.Message(welcome_message).send()


# --- On Message Event ---
@cl.on_message
async def on_message(message: cl.Message):
    session_history = cl.user_session.get("history") or []
    session_history.append({"role": "user", "content": message.content})

    loading_message = await cl.Message("🔎 Let me check the best options for you...").send()

    try:
        # --- Step 1: Run Destination Planning Agent ---
        agent_result = await run_agent(destination_agent, session_history)
        final_output = agent_result.final_output

        # --- Step 2: (Optional) Run other agents based on user input ---
        # if "explore" in message.content.lower():
        #     agent_result = await run_agent(explore_agent, agent_result.to_input_list())
        # elif "book" in message.content.lower():
        #     agent_result = await run_agent(booking_agent, agent_result.to_input_list())
        # final_output = agent_result.final_output

        # Update loading message with response
        loading_message.content = final_output
        await loading_message.update()

        # Save updated history
        cl.user_session.set("history", agent_result.to_input_list())

    except Exception as error:
        error_message = f"❌ Oops! Something went wrong: {error}"
        loading_message.content = error_message
        await loading_message.update()
        
