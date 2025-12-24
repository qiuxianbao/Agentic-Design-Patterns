# 🚀 Agentic Design Patterns - Complete Real-World Projects

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Stars](https://img.shields.io/github/stars/josephsenior/Agentic-design-patterns-)](https://github.com/josephsenior/Agentic-design-patterns-/stargazers)
[![Issues](https://img.shields.io/github/issues/josephsenior/Agentic-design-patterns-)](https://github.com/josephsenior/Agentic-design-patterns-/issues)

This repository contains complete, production-ready implementations of all 21 design patterns from the Agentic Design Patterns book. Each project demonstrates a specific pattern with a practical, runnable application.

> **Note**: This is an educational resource for learning AI agent design patterns. All code is MIT licensed and ready for experimentation.

## 📋 Table of Contents

- [🚀 All 21 Patterns Implemented](#-all-21-patterns-implemented)
  - [Core Patterns (Chapters 1-8)](#core-patterns-chapters-1-8)
  - [Advanced Patterns (Chapters 9-14)](#advanced-patterns-chapters-9-14)
  - [Specialized Patterns (Chapters 15-21)](#specialized-patterns-chapters-15-21)
- [🛠️ Quick Start](#️-quick-start)
- [🏗️ Project Structure](#️-project-structure)
- [📊 Pattern Categories](#-pattern-categories)
- [📦 Requirements](#-requirements)
- [💻 Usage Examples](#-usage-examples)
- [📚 Learning Path](#-learning-path)
- [🔧 Integration](#-integration)
- [📈 Status](#-status)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🚀 All 21 Patterns Implemented

### 🏗️ Core Patterns (Chapters 1-8)

| # | Pattern | Project | Description |
|---|---------|---------|-------------|
| 1 | **Prompt Chaining**<br>`prompt_chaining/` | Document Analysis Pipeline | Sequential multi-step processing<br>📝 Extract → Entities → Summary → JSON |
| 2 | **Routing**<br>`routing/` | Smart Request Router | Request classification and delegation<br>🔀 Route to specialized handlers |
| 3 | **Parallelization**<br>`parallelization/` | Parallel Document Processor | Concurrent task execution<br>⚡ 5 parallel analysis tasks with synthesis |
| 4 | **Reflection**<br>`reflection/` | Self-Improving Content Generator | Generate → Critique → Refine<br>🔄 Iterative content improvement |
| 5 | **Tool Use**<br>`tool_use/` | Research Assistant with Tools | Function calling and tool integration<br>🛠️ Search, calculate, analyze with tools |
| 6 | **Planning**<br>`planning/` | Task Planning System | Goal decomposition and execution<br>📋 Break goals into actionable tasks |
| 7 | **Multi-Agent**<br>`multi_agent/` | Collaborative Team System | Multiple specialized agents working together<br>👥 Research → Write → Edit → Coordinate |
| 8 | **Memory**<br>`memory/` | Conversation Memory System | State persistence and context management<br>🧠 Maintain conversation history |

### ⚡ Advanced Patterns (Chapters 9-14)

| # | Pattern | Project | Description |
|---|---------|---------|-------------|
| 9 | **Adaptation**<br>`adaptation/` | Adaptive Agent | Learning from feedback<br>📈 Improve over time based on experience |
| 10 | **MCP**<br>`mcp/` | Model Context Protocol Integration | Standardized agent communication<br>🔗 Tool sharing and resource access |
| 11 | **Goal Setting**<br>`goal_setting/` | Goal-Oriented Agent | Goal breakdown and progress tracking<br>🎯 Set goals, track progress, achieve objectives |
| 12 | **Exception Handling**<br>`exception_handling/` | Robust Agent with Fallback | Error handling and recovery<br>🛡️ Graceful failure handling |
| 13 | **Human-in-the-Loop**<br>`human_in_loop/` | Interactive Agent | Human escalation and feedback<br>👤 Customer support with escalation |
| 14 | **RAG**<br>`rag/` | Knowledge Retrieval System | Retrieval-Augmented Generation<br>📚 Document-based Q&A |

### 🎯 Specialized Patterns (Chapters 15-21)

| # | Pattern | Project | Description |
|---|---------|---------|-------------|
| 15 | **Inter-Agent Communication**<br>`inter_agent/` | Agent Communication System | Agent-to-agent messaging<br>💬 Agents collaborating via messages |
| 16 | **Resource Optimization**<br>`resource_optimization/` | Resource Optimizer | Efficient resource usage<br>⚡ Caching, batching, cost optimization |
| 17 | **Reasoning**<br>`reasoning/` | Chain-of-Thought Agent | Step-by-step reasoning<br>🧠 Complex problem solving |
| 18 | **Guardrails**<br>`guardrails/` | Safety Agent | Content validation and filtering<br>🔒 Safety and compliance checking |
| 19 | **Evaluation**<br>`evaluation/` | Agent Evaluation System | LLM-as-a-Judge<br>📊 Quality assessment and monitoring |
| 20 | **Prioritization**<br>`prioritization/` | Task Prioritization System | Priority-based task management<br>📋 Rank and order tasks |
| 21 | **Exploration**<br>`exploration/` | Exploration Agent | Experimental discovery<br>🔍 Multiple approach testing |

## 🛠️ Quick Start

Getting started with any project is straightforward:

```bash
# 1. Navigate to the project you want to explore
cd agentic_patterns_projects/prompt_chaining/

# 2. Install the dependencies
pip install -r requirements.txt

# 3. Set up your environment variables
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# 4. Run the example
python example.py  # Note: Use example.py, not main_file.py
```

## 🏗️ Project Structure

Each project follows a consistent structure that makes it easy to understand and extend:

```
📁 prompt_chaining/
├── 🔧 document_analyzer.py  # Core implementation
├── 📝 example.py            # Usage examples
├── 📖 README.md             # Project documentation
├── 📦 requirements.txt      # Python dependencies
└── ⚙️ .env.example          # Environment template
```

## 📊 Pattern Categories

I've organized the patterns into categories to help you understand how they relate:

| Category | Patterns | Description |
|----------|----------|-------------|
| **🔄 Sequential Patterns** | Prompt Chaining, Planning | Linear workflows and goal decomposition |
| **⚡ Parallel Patterns** | Parallelization | Concurrent task execution |
| **🎯 Decision Patterns** | Routing, Reflection, Prioritization | Request routing and iterative improvement |
| **🔗 Integration Patterns** | Tool Use, Multi-Agent, Inter-Agent Communication, MCP | Agent coordination and tool integration |
| **🧠 State Patterns** | Memory Management, Goal Setting | State persistence and goal tracking |
| **🛡️ Quality Patterns** | Exception Handling, Guardrails, Evaluation | Error handling and quality assurance |
| **🚀 Advanced Patterns** | Adaptation, RAG, Reasoning, Human-in-the-Loop, Resource Optimization, Exploration | Cutting-edge agent capabilities |

## 📦 Requirements

Most projects share similar requirements:

- 🐍 **Python 3.8 or higher**
- 🔑 **Gemini API key** (set in your `.env` file)
- 📚 **LangChain libraries** (installed via requirements.txt)

## 💻 Installation

To get started, install the common dependencies:

```bash
# Install common dependencies
pip install langchain langchain-google-genai langchain-community python-dotenv

# For specific projects, check their requirements.txt for any additional packages
```

> **Note**: Make sure you have a valid Gemini API key. You can get one from [Google AI Studio](https://makersuite.google.com/app/apikey).

## 💻 Usage Examples

Here are some quick examples to get you started:

### 📝 Example 1: Prompt Chaining
```python
from document_analyzer import DocumentAnalyzer

analyzer = DocumentAnalyzer()
result = analyzer.analyze("Your document text...")
print(result)  # Returns structured JSON with extracted entities and summary
```

### 🔀 Example 2: Routing
```python
from smart_router import SmartRouter

router = SmartRouter()
result = router.route("Book me a flight to Paris next week")
print(result)  # Routes to travel booking handler
```

### 👥 Example 3: Multi-Agent Collaboration
```python
from collaborative_team import CollaborativeTeam

team = CollaborativeTeam()
result = team.collaborate("Create a blog post", "Requirements...")
print(result)  # Coordinated output from research, writing, and editing agents
```

## 📚 Learning Path

If you're new to agentic design patterns, here's a suggested learning path:

### 🏗️ Phase 1: Core Patterns (Chapters 1-8)
**Focus**: Fundamentals of agent workflows
- Learn sequential and parallel processing
- Understand basic agent coordination
- Build foundation for advanced patterns

### ⚡ Phase 2: Advanced Patterns (Chapters 9-14)
**Focus**: Production-ready capabilities
- Master adaptation and memory systems
- Implement RAG and human interaction
- Build on core concepts with real-world features

### 🎯 Phase 3: Specialized Patterns (Chapters 15-21)
**Focus**: Enterprise-grade agent systems
- Resource optimization and cost management
- Safety, evaluation, and quality assurance
- Advanced techniques for production deployment

## 🔧 Integration

One of the coolest things about these patterns is that you can combine them:

| Pattern Combination | Use Case |
|-------------------|----------|
| **Routing + Multi-Agent** | Complex workflow orchestration |
| **RAG + Tool Use** | Enhanced knowledge retrieval with external tools |
| **Guardrails + Any Agent** | Safety and compliance across all systems |
| **Evaluation + Planning** | Quality monitoring of goal execution |
| **Memory + Adaptation** | Learning systems with persistent state |

Feel free to experiment and mix patterns to solve your specific problems!

## 📈 Status

✅ **All 21 patterns are complete and ready to use**

Every pattern has been implemented as a production-ready project with:
- Comprehensive documentation and examples
- Proper error handling and type hints
- Architecture diagrams and explanations
- Ready-to-run code with minimal setup

## 🤝 Contributing

We welcome contributions! Each project is self-contained and can be extended independently.

### Ways to Contribute
- 📝 Add more examples and use cases
- 🔧 Integrate with your own systems
- 🔗 Combine patterns in new ways
- 🚀 Extend functionality and add new features
- 🐛 Report bugs and suggest improvements
- 📖 Improve documentation

### Getting Started
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

These are educational examples, so feel free to experiment and build on them!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

These projects are educational examples demonstrating agentic design patterns. Use them to learn, experiment, and build your own systems.

---

## 📞 Contact & Support

- 🐛 **Issues**: [Report bugs or request features](https://github.com/josephsenior/Agentic-design-patterns-/issues)
- 💬 **Discussions**: [Join community discussions](https://github.com/josephsenior/Agentic-design-patterns-/discussions)
- 📧 **Questions**: Open an issue with the "question" label

Happy building! 🚀

