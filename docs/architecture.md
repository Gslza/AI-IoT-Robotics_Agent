# Architecture

The system uses a lightweight multi-agent architecture where the Orchestrator Agent receives user commands, asks the Planner Agent for an execution strategy, dispatches matching domain agents, stores execution context through the Memory Agent, and returns a consolidated response.

## Agent Responsibilities

- **Orchestrator Agent:** workflow control and response aggregation.
- **Planner Agent:** converts natural language goals into ordered execution steps.
- **Memory Agent:** stores task context, selected agents, and plans.
- **Vision Agent:** prepares YOLO11 object detection and PaddleOCR OCR workflows.
- **IoT Agent:** prepares ESP32, Arduino, MQTT, sensor, and relay workflows.
- **Robotics Agent:** prepares motor, servo, navigation, and obstacle avoidance workflows.
- **Networking Agent:** prepares device monitoring, remote access, and real-time communication workflows.
- **Tool Agent:** prepares Python, API, database, shell, and automation workflows.

## Current Implementation Scope

This initial scaffold is intentionally deterministic and safe. Agent implementations prepare structured action plans and metadata without directly controlling physical hardware or executing shell commands. Hardware adapters, model inference, database persistence, and dashboard features can be added behind the same agent interfaces.
