from core.models import TaskRequest
from core.orchestrator import Orchestrator


def test_orchestrator_routes_iot_and_vision_requests() -> None:
    orchestrator = Orchestrator()
    response = orchestrator.handle(TaskRequest(command="monitor suhu dan deteksi manusia dari kamera"))

    agent_names = [result.agent for result in response.results]

    assert "Vision_Agent" in agent_names
    assert "IoT_Agent" in agent_names
    assert "Memory_Agent" in agent_names
    assert any("Vision Agent" in step for step in response.plan)
    assert any("IoT Agent" in step for step in response.plan)


def test_orchestrator_returns_planning_only_when_no_domain_matches() -> None:
    orchestrator = Orchestrator()
    response = orchestrator.handle(TaskRequest(command="buat ringkasan tujuan proyek"))

    agent_names = [result.agent for result in response.results]

    assert "Orchestrator_Agent" in agent_names
    assert "Memory_Agent" in agent_names
    assert response.final_response.startswith("Workflow completed")
