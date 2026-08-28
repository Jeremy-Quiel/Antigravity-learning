# Model Documentation - Antigravity SDK

This document explains the Artificial Intelligence models compatible with the **Google Antigravity SDK** tool. The system is designed to work with autonomous agents. These models assist agents in reasoning, tool usage, policy enforcement, and subagent orchestration.

## Fast Processing and Agent Orchestration (Low Latency)

These models provide fast responses, agile decision-making, and manage the full lifecycle of autonomous agents.

### Gemini 3.7 Flash
* **Key Features:** The primary default model in the Antigravity SDK since mid-to-late 2026. Optimized and co-trained for the Antigravity *harness*, providing high speed for tool calling and subagent delegation.
* **Recommended Usage:** Ideal as the base model for general-purpose agents, high-speed automated workflows, terminal interactions, and standard tasks requiring near-instant responses.

### Gemini 3.5 Flash
* **Key Features:** The initial default model at the launch of Antigravity 2.0. Highly reliable for agent state management, custom tool registration, and lifecycle hook execution.
* **Recommended Usage:** Excellent for backwards compatibility with legacy agents, regression testing, or auxiliary tasks where resource usage must be minimized without losing agentic capabilities.

## Deep Analysis and Complex Tasks (High Reasoning)

High-capacity models designed for long contexts, advanced reasoning, and solving complex algorithmic challenges.

### Gemini 3.1 Pro
* **Key Features:** "Pro" variant focused on deep logical comprehension, whole-repository codebase analysis, and multi-step planning.
* **Recommended Usage:** Large-scale code refactoring, new system architecture design, in-depth security audits, and complex research requiring retention and cross-referencing of extensive repository data.

### Claude 4.6 (Opus)
* **Key Features:** The most capable model in the Anthropic family supported on the platform. Excels at assimilating large contexts, clear technical writing, and abstract logical reasoning.
* **Recommended Usage:** Authoring extensive technical manuals, analyzing cross-dependencies in legacy monolithic projects, and solving high-level software architectural challenges.

## Versatile and Interactive Workflows

Balanced models offering an optimal ratio between intelligence, context retention, and response latency.

### Claude 4.6 (Sonnet)
* **Key Features:** Optimized Anthropic variant combining strong comprehension of natural language and code (similar to Opus) with reduced response times.
* **Recommended Usage:** Interactive code assistance, pair-programming in Antigravity IDE, Pull Request reviews, and rapid unit test generation for newly authored code.

## Private Deployments and Open Ecosystem (Open Source)

Models designed for strict data privacy policies, isolated environments, or open research needs.

### GPT-OSS-120B
* **Key Features:** Large-scale open-weights language model (120 billion parameters). Provides a robust alternative to proprietary models in the SDK, allowing full inspection and transparency of weights and runtime.
* **Recommended Usage:** Local on-premise agent deployments where corporate data cannot leave the private network, compliance with strict air-gapped security policies, or low-level customizations for scientific research.