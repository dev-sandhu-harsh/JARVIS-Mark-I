# JARVIS Mark I

A local, offline-first JARVIS-style AI assistant core built with a focus on **systems design**, not prompt hacks.

This repository implements a production-grade agent architecture with deterministic control, safe tool execution, and persistent semantic memory — all running **fully locally**.

---

## ✨ What is JARVIS Mark I

JARVIS Mark I is the foundational core of a personal AI assistant inspired by JARVIS-like systems.

It is **not** a chatbot demo.

It is a **system**.

Key principles:
- The model is untrusted. The system is authoritative.
- Memory is data, not conversation.
- Tools are explicit capabilities, not suggestions.
- Architecture first. Tuning later.

---

## 🚀 Features

- CLI-first assistant for fast iteration and debugging
- Think → Act → Observe agent loop
- Strict JSON-based tool calling
- Safe, whitelisted tool execution
- Local LLM inference via Ollama
- Persistent vector memory with semantic recall
- Deterministic routing and bounded execution
- Hardware-agnostic (Mac, Linux, future edge devices)

---

## 🧱 Architecture Overview

CLI
↓
Orchestrator (control + routing)
↓
LLM Adapter (local inference)
↓
Tools (explicit capabilities)
↓
Memory (vector embeddings)


- The LLM never executes actions directly
- The orchestrator owns control flow
- Tools are validated and sandboxed
- Memory is retrieved before reasoning

---

## 📦 Prerequisites

- Python **3.10+**
- Git
- macOS or Linux (Windows via WSL works)
- **16 GB RAM minimum** recommended

---

## 🛠 Quick Start (Local Setup)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/jarvis.git
cd JARVIS-Mark-I
```
(If you forked the repo, use your fork URL.)

### 2. Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Upgrade pip:
```bash
pip install --upgrade pip
```

### 3. Install Python dependencies
```bash
pip install typer rich pydantic pydantic-settings python-dotenv
pip install sentence-transformers faiss-cpu
pip install ollama
pip install pyttsx3
```

##### Important
Voice output currently uses pyttsx3 (system TTS).
This is intentionally chosen to avoid system-level dependencies.
Neural TTS (Piper / Whisper) is planned in later versions.


### 4. Install Ollama (system dependency)

macOS
```bash
brew install ollama
```

Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Start Ollama service:
```bash
ollama serve
```
**Keep this running in a separate terminal.**

### 5. Pull a local model
```bash
ollama pull phi3:mini
```
(Other models can be swapped later.)

### 6. Run JARVIS
```bash
python -m jarvis.main ask "Hello JARVIS"
```

## Test memory:
```bash
python -m jarvis.main ask "My name is Harsh"
python -m jarvis.main ask "Do you remember my name?"
```



## 🧠 Memory System

Long-term memory uses vector embeddings

Stored locally in model_memory/

Semantic recall (not string matching)

Memory is injected as system facts, not conversation




## 🔐 Tool Safety Model

Tools are explicitly registered

The LLM can only request tools

The orchestrator validates and executes

No eval, no dynamic execution

This prevents hallucinated or unsafe actions.



## 🧪 Current State

### Mark I v1

Text-based assistant

Tool execution

Semantic memory

CLI interface

Voice Output

### Planned future marks:

Mark I v2 → Background tasks & autonomy

Mark I v3 → Proactive behavior & scheduling



## ⚠️ Notes

Runs fully offline

No cloud APIs

No telemetry

Experimental and under active development

Expect rough edges. Architecture is the priority.



## 🤝 Contributing

Fork the repo

Create a feature branch

Keep commits small and scoped

Architecture > polish

A CONTRIBUTING.md will be added later.

---

## FINAL NOTE

This project is about learning how real AI systems are built.

Not prompts.
Not demos.
Systems.
