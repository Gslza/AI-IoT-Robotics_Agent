"""Base class for lightweight deterministic agents."""

from __future__ import annotations

from abc import ABC, abstractmethod

from core.models import AgentResult, TaskRequest


class BaseAgent(ABC):
    """Common contract implemented by all domain agents."""

    name: str
    keywords: tuple[str, ...] = ()

    def can_handle(self, request: TaskRequest) -> bool:
        """Return true when the command mentions one of the agent keywords."""

        command = request.command.lower()
        return any(keyword in command for keyword in self.keywords)

    @abstractmethod
    def run(self, request: TaskRequest) -> AgentResult:
        """Execute the agent-specific task."""
