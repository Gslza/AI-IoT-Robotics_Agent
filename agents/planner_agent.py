"""Planner agent that converts a user command into executable steps."""

from __future__ import annotations

from core.models import TaskRequest


class PlannerAgent:
    """Rule-based planner for the first project scaffold."""

    name = "Planner_Agent"

    def create_plan(self, request: TaskRequest) -> list[str]:
        """Create an execution strategy from the command and context."""

        plan = ["Validate user command and context", "Select domain agents"]
        command = request.command.lower()

        if any(word in command for word in ("camera", "kamera", "vision", "ocr", "deteksi", "detect")):
            plan.append("Process camera or image data with Vision Agent")
        if any(word in command for word in ("sensor", "relay", "esp32", "mqtt", "iot", "suhu", "temperature")):
            plan.append("Read or control IoT devices with IoT Agent")
        if any(word in command for word in ("robot", "motor", "servo", "navigation", "navigasi")):
            plan.append("Execute robotics movement or control with Robotics Agent")
        if any(word in command for word in ("network", "jaringan", "device", "ping", "remote")):
            plan.append("Monitor network devices with Networking Agent")

        plan.append("Persist execution context with Memory Agent")
        plan.append("Summarize result for the user")
        return plan
