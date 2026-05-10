# AI IoT Robotics Agent System

Sistem **AI Agent** berbasis multi-agent architecture untuk reasoning, monitoring sensor, kontrol perangkat IoT, computer vision, robotics control, networking, dan automation.

## Tujuan Utama

Membangun sistem AI Agent cerdas yang mampu melakukan:

- Reasoning dan planning berbasis tujuan pengguna.
- Monitoring sensor dan kontrol perangkat IoT.
- Komunikasi antar-agent yang terkoordinasi.
- Object detection, OCR, dan image understanding.
- Kontrol robot, motor, servo, dan autonomous movement.
- Autonomous decision making untuk skenario edge AI dan smart automation.

## Arsitektur Multi-Agent

| Agent | Peran |
| --- | --- |
| Orchestrator Agent | Mengatur workflow dan komunikasi antar agent. |
| Planner Agent | Menganalisis tujuan dan membuat rencana aksi. |
| Memory Agent | Menyimpan short-term dan long-term memory. |
| Vision Agent | Melakukan object detection, OCR, dan image understanding. |
| IoT Agent | Mengontrol sensor, relay, ESP32, MQTT, dan perangkat IoT. |
| Robotics Agent | Mengontrol robot, motor, servo, dan autonomous movement. |
| Networking Agent | Mengelola komunikasi jaringan dan monitoring device. |
| Tool Agent | Menjalankan tools seperti Python, API, database, shell, dan automation. |

## Workflow

1. User memberikan perintah.
2. Orchestrator Agent menerima request.
3. Planner Agent membuat strategi eksekusi.
4. Agent terkait dipanggil sesuai kebutuhan.
5. Vision Agent memproses kamera jika diperlukan.
6. IoT Agent membaca sensor atau mengontrol device.
7. Robotics Agent menjalankan aksi fisik.
8. Memory Agent menyimpan hasil dan konteks.
9. Orchestrator Agent menghasilkan response akhir.

## Integrasi Utama

- **IoT:** ESP32 DevKit V1, ESP32-C3, Arduino Uno, MQTT, HTTP, WebSocket, I2C, SPI, UART.
- **Computer Vision:** YOLO11 untuk object detection dan PaddleOCR untuk OCR.
- **Robotics:** autonomous navigation, obstacle avoidance, motor control, servo control, remote operation, dan sensor fusion.
- **Networking:** device monitoring, real-time communication, cloud integration, edge computing, remote access, dan smart home communication.
- **Deployment:** Linux, Docker, cloud server, edge device, dan Raspberry Pi.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
uvicorn api.main:app --reload
```

Contoh request:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H 'Content-Type: application/json' \
  -d '{"command":"monitor suhu dan deteksi manusia dari kamera"}'
```

## Struktur Project

```text
agents/      Implementasi agent spesifik domain
core/        Model data dan orchestration core
api/         FastAPI entrypoint
configs/     Konfigurasi sistem
memory/      Penyimpanan memori agent
vision/      Adapter computer vision
iot/         Adapter IoT dan device control
robotics/    Adapter robotics control
networking/  Adapter monitoring jaringan
frontend/    Placeholder aplikasi web
mobile/      Placeholder aplikasi mobile
datasets/    Dataset eksperimen
models/      Model AI/ML lokal
docs/        Dokumentasi teknis
tests/       Test otomatis
```
