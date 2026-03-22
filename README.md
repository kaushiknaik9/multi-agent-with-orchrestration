# Multi-Agent YouTube Blog Generator (CrewAI + Ollama + NesoAcademy)

This project is a multi‑agent system built with **CrewAI** and **Ollama** that:

- Searches the **NesoAcademy** YouTube channel for videos on a topic.
- Extracts video titles/descriptions via a custom tool.
- Uses local LLMs (Ollama) to generate a structured blog post (e.g., on Analog Electronics).

No OpenAI API key is required; everything runs locally via Ollama.

---

## Features

- Custom CrewAI tool that searches NesoAcademy’s channel using **yt‑dlp**.
- Two agents:
  - **Blog Researcher** – finds and analyzes relevant videos for `{topic}`.
  - **Writer** – writes a blog-style summary from the research.
- Sequential workflow: research task → writing task.
- Output saved as a Markdown file.

---

## Project Structure

```text
multiagentcrewai/
├─ crew.py          # Crew setup and run (entry point)
├─ agents.py        # Agents (blog_researcher, blog_writter)
├─ tasks.py         # Tasks (research_task, write_task)
├─ tools.py         # Custom NesoChannelSearchTool using yt-dlp
├─ .env             # (optional, not needed for Ollama-only)
├─ requirements.txt # Python dependencies
└─ result.md        # Generated blog post (created at runtime)
