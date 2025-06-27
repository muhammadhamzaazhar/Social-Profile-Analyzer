import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from output_parsers import summary_parser, ice_breaker_parser, topics_of_interest_parser

load_dotenv()

llm = ChatOpenAI(
        model="deepseek/deepseek-r1-0528:free",  
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        temperature=0,
    )

def get_summary_chain() -> RunnableSequence:
    summary_template = """
        Given the LinkedIn information: {information}, and Twitter posts {twitter_posts}.
        1. Write a short summary of the person.
        2. Mention two interesting facts about them.

        Use both the information from LinkedIn and Twitter.
        /n{format_instructions} 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    return summary_prompt_template | llm | summary_parser

def get_interests_chain() -> RunnableSequence:
    interesting_facts_template = """
        Given the information about a person from linkedin {information}, and twitter posts {twitter_posts}.
        - Create 3 Topics that might interest them
        \n{format_instructions}
     """

    interesting_facts_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=interesting_facts_template,
        partial_variables={
            "format_instructions": topics_of_interest_parser.get_format_instructions()
        },
    )

    return interesting_facts_prompt_template | llm | topics_of_interest_parser

def get_ice_breaker_chain() -> RunnableSequence:
    ice_breaker_template = """
        Given the information about a person from linkedin {information}, and twitter posts {twitter_posts}.
        - Create 2 creative Ice breakers with them that are derived from their activity on Linkedin and twitter, preferably on latest tweets
        \n{format_instructions}
     """

    ice_breaker_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"],
        template=ice_breaker_template,
        partial_variables={
            "format_instructions": ice_breaker_parser.get_format_instructions()
        },
    )

    return ice_breaker_prompt_template | llm | ice_breaker_parser