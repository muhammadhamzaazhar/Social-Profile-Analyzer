import os
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from dotenv import load_dotenv

from tools.tools import get_profile_url_tavily

load_dotenv()

def twitter_lookup_agent(user_name: str) -> str:
    try:
        # llm = ChatOpenAI(
        #     model="deepseek/deepseek-r1-0528:free",  
        #     base_url="https://openrouter.ai/api/v1",
        #     api_key= os.environ["OPENROUTER_API_KEY"],
        #     temperature=0,
        # )

        # template = """
        #     Given the full name {name_of_person}, your task is to find the link to their Twitter (X) profile page by searching online.
        #     Once you have the profile URL (e.g., https://x.com/USERNAME), extract only the username from the URL.
        #     Only return the username, nothing else. 
        # """
        
        # tools_for_agent_twitter = [
        #     Tool.from_function(
        #         name="Crawl Google 4 Twitter profile page",
        #         func=lambda user_name: get_profile_url_tavily(user_name, platform="twitter"),
        #         description="Useful for when you need to get a Twitter profile page URL",
        #         sync=True
        #     ),
        # ]

        # prompt_template = PromptTemplate(
        #     input_variables=["name_of_person"], template=template
        # )

        # react_prompt = hub.pull("hwchase17/react")
        # agent = create_react_agent(
        #     llm=llm, tools=tools_for_agent_twitter, prompt=react_prompt
        # )
        # agent_executor = AgentExecutor(
        #     agent=agent, tools=tools_for_agent_twitter, verbose=True, handle_parsing_errors=True
        # )

        # result = agent_executor.invoke(
        #     input={"input": prompt_template.format_prompt(name_of_person=user_name)}
        # )

        # twitter_username = result["output"]

        # return twitter_username
        print(f"\n[Twitter Lookup] Looking up profile for: {user_name}")
        
        user_name = get_profile_url_tavily(user_name, platform="twitter")
        
        print(f"[Twitter Lookup] Found URL: {user_name}")
        print("[Twitter Lookup] Exiting linkedin_lookup_agent...\n")
        
        return user_name
    except Exception as e:
        raise RuntimeError(f"[Twitter Agent failed]: {e}")
