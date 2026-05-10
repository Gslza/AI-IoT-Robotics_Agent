"""FastAPI application for the AI IoT Robotics Agent System."""

from __future__ import annotations

from fastapi import FastAPI

from core.models import TaskRequest, TaskResponse
from core.orchestrator import Orchestrator

app = FastAPI(
    title="AI IoT Robotics Agent System",
    version="1.0.0",
    description="Multi-agent API for IoT, robotics, computer vision, networking, and automation workflows.",
)
orchestrator = Orchestrator()


@app.get("/health")
def health() -> dict[str, str]:
    """Return service health status."""

    return {"status": "ok", "service": "ai-iot-robotics-agent-system"}


@app.post("/tasks", response_model=TaskResponse)
def create_task(request: TaskRequest) -> TaskResponse:
    """Execute a user command through the orchestrator."""

    return orchestrator.handle(request)
