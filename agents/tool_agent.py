"""Tool agent for safe automation placeholders."""

from __future__ import annotations

from .base import BaseAgent
from core.models import AgentResult, TaskRequest


class ToolAgent(BaseAgent):
    """Handle API, database, Python, shell, and automation requests."""

    name = "Tool_Agent"
    keywords = ("python", "api", "database", "shell", "automation", "otomasi", "tool")

    def run(self, request: TaskRequest) -> AgentResult:
        return AgentResult(
            agent=self.name,
            summary="Prepared tool automation workflow without executing unsafe side effects.",
            data={"tools": ["Python", "API", "database", "shell", "automation"], "command": request.command},
        )
