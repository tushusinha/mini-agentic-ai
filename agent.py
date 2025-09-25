import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from duckduckgo_search import DDGS
from safe_utils import simple_calculator, read_file

# Load environment variables from .env
load_dotenv()

# Fetch the Weather API from .env
weather_api_key = os.getenv("WEATHER_API_KEY")

# Ensure API key exists
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("❌ Please set OPENAI_API_KEY in your .env file")
if not weather_api_key:
    raise ValueError("❌ Please set WEATHER_API_KEY in your .env file")

# Initialize OpenAI LLM (use GPT-3.5 for cost efficiency)
llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # cost-effective model
    temperature=0
)


# 1. Web Search Tool
def search_duckduckgo(query: str) -> str:
    with DDGS() as ddgs:
        results = ddgs.text(
            query,
            max_results=2
        )
        return "\n".join([r["title"] + ": " + r["body"] for r in results])


search_tool = Tool(
    name="Web Search",
    func=search_duckduckgo,
    description="Use this to search for current events or general knowledge."
)


# 2. Calculator Tool
calc_tool = Tool(
    name="Calculator",
    func=simple_calculator,
    description="Use this to solve math problems. Input like '25*42'."
)


# 3. File Reader Tool
file_tool = Tool(
    name="File Reader",
    func=read_file,
    description="Use this to read local text files. Input = file path."
)


# 4. Weather Tool
def get_weather(city: str) -> str:
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric"
    }
    response = requests.get(
        url,
        params=params
    )
    data = response.json()

    if data.get("cod") != 200:
        return f"Fetch plm weather for {city}: {data.get('message', 'Unknown error')}"

    main = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    return f"Weather in {city}: {main}, {temp}°C (feels like {feels}°C)."


weather_tool = Tool(
    name="Weather",
    func=get_weather,
    description="Get current weather for a city. Input should be a city name."
)


# Initialize the agent with multiple tools
agent = initialize_agent(
    tools=[search_tool, calc_tool, file_tool, weather_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


def run_agent(query: str) -> str:
    """Run the agent on a given query."""
    return agent.run(query)
