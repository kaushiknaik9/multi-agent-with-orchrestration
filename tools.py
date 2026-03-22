from crewai_tools import YoutubeChannelSearchTool
from crewai.tools import BaseTool
import yt_dlp

# yt_tool = YoutubeChannelSearchTool(
#     youtube_channel_handle="@nesoacademy",
#     config={
#         "llm": {
#             "provider": "ollama",
#             "config": {
#                 "model": "mistral",
#                 "base_url": "http://localhost:11434",
#             },
#         },
#         "embedder": {
#             "provider": "ollama",
#             "config": {
#                 "model": "nomic-embed-text",
#                 "base_url": "http://localhost:11434",
#             },
#         },
#     },
# )


# tools.py
# already installed with crewai-tools


class NesoChannelSearchTool(BaseTool):
    name: str = "NesoAcademy YouTube search"  # ✅ with type annotation
    description: str = (  # ✅ with type annotation
        "Search the @nesoacademy YouTube channel for videos related to a topic "
        "and return titles, short descriptions, and URLs."
    )

    def _run(self, topic: str) -> str:
        search_url = f"https://www.youtube.com/@nesoacademy/search?query={topic}"
        ydl_opts = {
            "quiet": True,
            "skip_download": True,
            "extract_flat": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(search_url, download=False)

        entries = info.get("entries", [])[:10]
        lines = []
        for e in entries:
            title = e.get("title", "")
            desc = (e.get("description") or "")[:300]
            url = f"https://www.youtube.com/watch?v={e.get('id')}"
            lines.append(f"- {title}\n  {desc}\n  {url}")
        return "\n".join(lines) or "No videos found."


tool = NesoChannelSearchTool()
