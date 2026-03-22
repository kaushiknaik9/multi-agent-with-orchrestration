from crewai import Task
from tools import tool
from agents import blog_researcher, blog_writter


# research task

research_task = Task(
    description=(
        "identify the video: {topic}"
        "get detailed information about the video from the yt channel."
    ),
    expected_output="A comprehensive 3 paragraphs long report based on the {topic} of the video content",
    tools=[tool],
    agent=blog_researcher,
)

write_task = Task(
    description=("get the info from the youtube channel on the topic: {topic}."),
    expected_output="Summarize the info from the youtube channe; video on the topic: {topic} and create the content for blog",
    context=[research_task],
    tools=[tool],
    agent=blog_researcher,
    async_execution=False,
    output_file="result.md",
)
