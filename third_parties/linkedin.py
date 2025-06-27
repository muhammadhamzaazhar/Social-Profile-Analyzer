import os, sys
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    try:
        if mock:
            linkedin_profile_url = "https://gist.githubusercontent.com/muhammadhamzaazhar/3fef245085c729157d405f1338644cd8/raw/1cd4b05c64aa9457726016f8c7ffad373a08779a/muhammad-hamza-azhar-proxycurl.json"
            response = requests.get(
                linkedin_profile_url,
                timeout=10,
            )
        else:
            api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
            header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
            response = requests.get(
                api_endpoint,
                params={"url": linkedin_profile_url},
                headers=header_dic,
                timeout=10,
            )

        data = response.json()
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", None) and k not in ["people_also_viewed", "certifications"]
        }

        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")

        return data
    except Exception as e:
        raise RuntimeError(f"[LinkedIn Scraping Failed]: {e}")