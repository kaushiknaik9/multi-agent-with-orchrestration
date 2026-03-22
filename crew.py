from crewai import Crew, Process
from agents import blog_researcher, blog_writter
from tools import tool
from tasks import research_task, write_task


crew = Crew(
    agents=[blog_researcher, blog_writter],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
)


# start task execution process with enhanced feedback
result = crew.kickoff(inputs={"topic": "Analog Electronics"})

print(result)
