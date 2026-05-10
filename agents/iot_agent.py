"""IoT agent for sensors, microcontrollers, and automation devices."""

from __future__ import annotations

from .base import BaseAgent
from core.models import AgentResult, TaskRequest


class IoTAgent(BaseAgent):
    """Handle ESP32, Arduino, MQTT, sensor, and relay requests."""

    name = "IoT_Agent"
    keywords = ("sensor", "relay", "esp32", "arduino", "mqtt", "iot", "suhu", "temperature", "pir", "ldr")

    def run(self, request: TaskRequest) -> AgentResult:
        return AgentResult(
            agent=self.name,
            summary="Prepared IoT monitoring/control action for supported sensors and devices.",
            data={
                "microcontrollers": ["ESP32 DevKit V1", "ESP32-C3", "Arduino Uno"],
                "protocols": ["MQTT", "HTTP", "WebSocket", "I2C", "SPI", "UART"],
                "command": request.command,
            },
        )
