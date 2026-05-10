"""Shared data models for multi-agent workflows."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class TaskRequest:
    """User command accepted by the orchestrator."""

    command: str
    context: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.command.strip():
            raise ValueError("command must not be empty")


@dataclass(slots=True)
class AgentResult:
    """Normalized response from a domain agent."""

    agent: str
    summary: str
    status: str = "ok"
    data: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class TaskResponse:
    """Final orchestrator response returned to clients."""

    plan: list[str]
    results: list[AgentResult]
    final_response: str
    task_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
