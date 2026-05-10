"""Robotics agent for movement, motors, servos, and navigation."""

from __future__ import annotations

from .base import BaseAgent
from core.models import AgentResult, TaskRequest


class RoboticsAgent(BaseAgent):
    """Handle robot movement and autonomous control requests."""

    name = "Robotics_Agent"
    keywords = ("robot", "motor", "servo", "navigation", "navigasi", "obstacle", "avoidance", "movement")

    def run(self, request: TaskRequest) -> AgentResult:
        return AgentResult(
            agent=self.name,
            summary="Prepared robotics control action for movement, obstacle avoidance, or sensor fusion.",
            data={
                "supported_functions": [
                    "Autonomous Navigation",
                    "Obstacle Avoidance",
                    "Motor Control",
                    "Servo Control",
                    "Remote Operation",
                    "Sensor Fusion",
                ],
                "command": request.command,
            },
        )
