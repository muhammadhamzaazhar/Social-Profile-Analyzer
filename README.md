
# Social Profile Analyzer (Agentic AI Project)

This project is an intelligent **Agentic AI web application** built using LangChain and OpenRouter’s DeepSeek model. It takes a person's name as input and returns a professional profile summary, interesting facts, potential ice-breakers, and topics of interest based on publicly available data from LinkedIn and Twitter.

<p align="center">
  <img src="https://github.com/user-attachments/assets/6c0dc4d3-97e1-4836-b511-43b02ef877ee" alt="App Screenshot" width="500"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/264e13e2-29fb-468e-9081-a70ef62d1277" alt="App Screenshot" width="500"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/5ac2a517-36b5-401d-a6d8-14ff353006ef" alt="App Screenshot" width="500"/>
</p>

## 💡 Features

- 🔍 **Name-based Profile Search** (LinkedIn & Twitter)
- 📄 **Summarized Bio & Facts**
- 💬 **Conversation Starters & Ice-breakers**
- 📚 **Topics of Interest**
- 🧠 Powered by LangChain + DeepSeek: R1 0528 (free)

---

## 📦 Tech Stack

- 🦜 LangChain (Agents + Tools)
- 🌐 Flask (Frontend + Backend)
- 🧠 Deepseek R1 LLM
- 🕸️ Tavily Search API
- 🐦 Twitter API (via Tweepy)
- 🔗 Proxycurl (LinkedIn scraping)
- 🧪 LangSmith (Optional for tracing/debugging)

---

## 🔐 Environment Variables

To run this project locally or on Hugging Face, you **must create a `.env` file** in the root directory with the following keys:

```bash
OPENROUTER_API_KEY
PROXYCURL_API_KEY
TAVILY_API_KEY

TWITTER_API_KEY
TWITTER_API_KEY_SECRET
TWITTER_BEARER_TOKEN
TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET

LANGCHAIN_TRACING              # (Optional)
LANGSMITH_ENDPOINT             # Required if tracing enabled
LANGCHAIN_API_KEY              # Required if tracing enabled
LANGCHAIN_PROJECT              # Required if tracing enabled
```
---

## 🤖 LLM Configuration

This project uses the `deepseek/deepseek-r1-0528:free` model via [OpenRouter](https://openrouter.ai) for language generation.

If you want to use a different OpenRouter-compatible LLM, make sure to update the `model` parameter accordingly:

```python
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",  
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0,
)
```

## 💵 Note on API Usage

This project uses **paid API services**:
> - [Proxycurl](https://nubela.co/proxycurl/) for **LinkedIn data scraping**  
  *(Includes 10 free credits to start)*  
> - **Twitter API** *(paid)* for accessing Twitter data

---

### 🔄 Behavior with Mock Data

Because these APIs are paid, the deployed version **uses mock data**.

📝 **What does that mean?**

- If you enter *any* name, the app will always return a **hardcoded mock profile**.
- This allows the demo to work **without requiring paid API keys**.

---

### 🔧 How to Enable Real-time Data Scraping

To fetch real LinkedIn and Twitter data, follow these steps:

1. **Purchase API keys** for Proxycurl and Twitter.
2. **Set the keys** in your `.env` file.
3. **Modify the file** `profile_analyzer.py`:

```python
# 🔄 Replace this mock logic:
linkedin_data = scrape_linkedin_profile(linkedin_url, mock=True)
tweets = scrape_user_tweets_mock()

# ✅ With this:
linkedin_data = scrape_linkedin_profile(linkedin_url)
tweets = scrape_user_tweets(twitter_url)
```
---

## 🙌 Contributing

Contributions are welcome! If you find a bug or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

## 📬 Contact

For any questions or feedback, reach out to **me** via [LinkedIn](https://www.linkedin.com/in/muhammad-hamza-azhar-996289314/) or open an issue on this repository.

---

## ⭐️ Show Your Support

If you like this project, please give it a ❤️ on [Huggingface](https://huggingface.co/spaces/mhamza-007/Social-Profile-Analyzer)!

---
