"""Vision agent for object detection, OCR, and image understanding."""

from __future__ import annotations

from .base import BaseAgent
from core.models import AgentResult, TaskRequest


class VisionAgent(BaseAgent):
    """Handle camera, YOLO, OCR, and safety monitoring requests."""

    name = "Vision_Agent"
    keywords = ("camera", "kamera", "vision", "ocr", "yolo", "deteksi", "detect", "image", "gambar", "bottle", "human")

    def run(self, request: TaskRequest) -> AgentResult:
        return AgentResult(
            agent=self.name,
            summary="Prepared computer vision pipeline using YOLO11 detection and PaddleOCR recognition.",
            data={
                "object_detection_framework": "YOLO11",
                "ocr_framework": "PaddleOCR",
                "tasks": ["Object Detection", "Human Detection", "Bottle Detection", "Text Recognition"],
                "command": request.command,
            },
        )
