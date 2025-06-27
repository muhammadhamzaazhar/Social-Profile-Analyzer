from typing import Tuple
from dotenv import load_dotenv

from third_parties.linkedin import scrape_linkedin_profile
# from third_parties.twitter import scrape_user_tweets
from third_parties.twitter import scrape_user_tweets_mock
from agents.linkedin_lookup_agent import linkedin_lookup_agent
from agents.twitter_lookup_agent import twitter_lookup_agent
from chains.custom_chains import (
    get_summary_chain,
    get_interests_chain,
    get_ice_breaker_chain,
)
from output_parsers import (
    Summary,
    IceBreaker,
    TopicOfInterest,
)

load_dotenv()

def get_user_profile(name: str) -> Tuple[Summary, TopicOfInterest, IceBreaker, str]:
    try:
        linkedin_url = linkedin_lookup_agent(name)
        if not linkedin_url:
            raise ValueError(f"Could not find LinkedIn URL for: {name}")
        # linkedin_data = scrape_linkedin_profile(linkedin_url)
        linkedin_data = scrape_linkedin_profile(linkedin_url, mock=True)

        twitter_url = twitter_lookup_agent(name)
        if not twitter_url:
            raise ValueError(f"Could not find Twitter URL for: {name}")
        # tweets = scrape_user_tweets(twitter_url)
        tweets = scrape_user_tweets_mock()

        try:
            print("[Chain] Invoking Summary Chain...")
            summary_chain = get_summary_chain()
            summary_and_facts: Summary = summary_chain.invoke(
                input={"information": linkedin_data, "twitter_posts": tweets},
            )
        except Exception as e:
            raise RuntimeError(f"[Summary Generation Failed]: {e}")

        try:
            print("\n[Chain] Invoking Interests Chain...")
            interests_chain = get_interests_chain()
            interests: TopicOfInterest = interests_chain.invoke(
                input={"information": linkedin_data, "twitter_posts": tweets}
            )
        except Exception as e:
            raise RuntimeError(f"[Interests Generation Failed]: {e}")
        
        try:
            print("\n[Chain] Invoking Ice Breaker Chain...")
            ice_breaker_chain = get_ice_breaker_chain()
            ice_breakers: IceBreaker = ice_breaker_chain.invoke(
                input={"information": linkedin_data, "twitter_posts": tweets}
            )
        except Exception as e:
            raise RuntimeError(f"[Ice Breakers Generation Failed]: {e}")

        return (
            summary_and_facts,
            interests,
            ice_breakers,
            linkedin_data.get("profile_pic_url")
        )
    except Exception as e:
        raise RuntimeError(f"[User Profile Generation Failed]: {e}")
