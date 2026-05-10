"""Workflow orchestration for the multi-agent system."""

from __future__ import annotations

from agents.iot_agent import IoTAgent
from agents.memory_agent import MemoryAgent
from agents.networking_agent import NetworkingAgent
from agents.planner_agent import PlannerAgent
from agents.robotics_agent import RoboticsAgent
from agents.tool_agent import ToolAgent
from agents.vision_agent import VisionAgent
from core.models import AgentResult, TaskRequest, TaskResponse


class Orchestrator:
    """Coordinate planning, domain-agent execution, memory, and final response."""

    def __init__(self) -> None:
        self.planner = PlannerAgent()
        self.memory = MemoryAgent()
        self.domain_agents = [
            VisionAgent(),
            IoTAgent(),
            RoboticsAgent(),
            NetworkingAgent(),
            ToolAgent(),
        ]

    def handle(self, request: TaskRequest) -> TaskResponse:
        """Run the multi-agent workflow for a user task."""

        plan = self.planner.create_plan(request)
        selected_agents = [agent for agent in self.domain_agents if agent.can_handle(request)]

        if not selected_agents:
            results: list[AgentResult] = [
                AgentResult(
                    agent="Orchestrator_Agent",
                    summary="No specialized agent matched the command; returning a planning-only response.",
                    data={"command": request.command},
                )
            ]
        else:
            results = [agent.run(request) for agent in selected_agents]

        memory_result = self.memory.remember(request, plan, [result.agent for result in results])
        results.append(memory_result)

        agent_list = ", ".join(result.agent for result in results)
        final_response = f"Workflow completed with agents: {agent_list}."
        return TaskResponse(plan=plan, results=results, final_response=final_response)
