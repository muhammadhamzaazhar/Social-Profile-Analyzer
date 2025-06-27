import os
from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

from tools.tools import get_profile_url_tavily

load_dotenv()

def linkedin_lookup_agent(user_name: str) -> str:
   try:
        # llm = ChatOpenAI(
        #     model="deepseek/deepseek-r1-0528:free",  
        #     base_url="https://openrouter.ai/api/v1",
        #     api_key= os.environ["OPENROUTER_API_KEY"],
        #     temperature=0,
        # )
        # template = """
        #     Given the full name {name_of_person}, find the direct URL to their LinkedIn profile page.
        #     Your response should contain only the LinkedIn profile URL — no additional text or explanation.
        # """

        # prompt_template = PromptTemplate(
        #     template=template, input_variables=["name_of_person"]
        # )

        # tools_for_agent = [
        #     Tool.from_function(
        #         name="Crawl Google for LinkedIn profile page",
        #         func=lambda user_name: get_profile_url_tavily(user_name, platform="linkedin"),
        #         description="Useful for when you need to get a LinkedIn profile page URL",
        #         sync=True
        #     ),
        # ]

        # react_prompt = hub.pull("hwchase17/react")
        # agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
        # agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True)

        # result = agent_executor.invoke(
        #     input={"input": prompt_template.format_prompt(name_of_person=user_name)}
        # )

        # linked_profile_url = result["output"]
        # return linked_profile_url
        print(f"\n[LinkedIn Lookup] Looking up profile for: {user_name}")
        
        url = get_profile_url_tavily(user_name, platform="linkedin")
        
        print(f"[LinkedIn Lookup] Found URL: {url}")
        print("[LinkedIn Lookup] Exiting linkedin_lookup_agent...\n")
        
        return url
   except Exception as e:
        raise RuntimeError(f"[LinkedIn Agent failed]: {e}")