"""Memory agent for short-term and long-term execution context."""

from __future__ import annotations

from core.models import AgentResult, TaskRequest


class MemoryAgent:
    """In-memory store suitable for local development and tests."""

    name = "Memory_Agent"

    def __init__(self) -> None:
        self._events: list[dict[str, object]] = []

    @property
    def events(self) -> list[dict[str, object]]:
        """Return a copy of saved events."""

        return list(self._events)

    def remember(self, request: TaskRequest, plan: list[str], agent_names: list[str]) -> AgentResult:
        event = {"command": request.command, "plan": plan, "agents": agent_names, "context": request.context}
        self._events.append(event)
        return AgentResult(
            agent=self.name,
            summary="Stored task context in short-term memory.",
            data={"event_count": len(self._events), "last_event": event},
        )
