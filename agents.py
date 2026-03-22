from crewai import Agent
from tools import tool

from crewai import LLM

# blog content research

llm = LLM(model="ollama/mistral", base_url="http://localhost:11434", temperature=0.2)


blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="get the relevant video content for the topic: {topic} from YT channel",
    llm=llm,
    verbose=True,
    # name
    # description
    memory=True,
    backstory=(
        "Expert in understanding videos in VLSI Analog circuits and entire ECE provideing suggestions"
    ),
    tools=[tool],
    allow_delegation=True,  # do I need to transfer work to next agent after mine is done
)


# second blog writter with YT tool

blog_writter = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about the video for the topic: {topic}, from YT channel",
    llm=llm,
    verbose=True,
    # name
    # description
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "with engaging narratives that captivates and educate, bringing new"
        "discoveries to light in accessible manner"
    ),
    tools=[tool],
    allow_delegation=False,
)
