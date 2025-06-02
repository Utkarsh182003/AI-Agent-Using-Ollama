# MedAI Agent Suite

A modular, multi-agent AI system for automating and validating medical research article writing, summarization, and data sanitization using LLaMA models via Ollama, with a user-friendly Streamlit interface.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Workflow](#workflow)
- [Installation](#installation)
- [Usage](#usage)
- [Agents](#agents)
- [Logging](#logging)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**MedAI Agent Suite** is an AI-powered application designed to assist researchers, students, and medical professionals in generating, refining, validating, and sanitizing medical research articles and data. It leverages the LLaMA language model (via Ollama) and a modular agent-based architecture to ensure high-quality, privacy-compliant outputs.

---

## Features

- **Summarize Medical Text:**  
  Generate concise summaries of lengthy medical documents, with automated quality validation.

- **Write & Refine Research Articles:**  
  Draft research articles from a topic or outline, refine for clarity and structure, and validate for academic standards.

- **Sanitize Medical Data:**  
  Automatically remove Protected Health Information (PHI) from medical data, with validation to ensure privacy compliance.

- **Validator Agents:**  
  Each main task is paired with a validator agent that reviews and rates the output for quality, accuracy, or privacy.

- **User-Friendly Interface:**  
  Built with Streamlit for easy, interactive use.

- **Robust Logging:**  
  All actions and errors are logged for transparency and debugging.

---

## Architecture

- **Streamlit Frontend:**  
  Provides a simple web interface for user interaction.

- **Agent Manager:**  
  Coordinates the execution of main and validator agents for each task.

- **Agents:**  
  - *SummarizeTool* & *SummarizeValidatorAgent*
  - *WriteArticleTool* & *WriteArticleValidatorAgent*
  - *SanitizeDataTool* & *SanitizeDataValidatorAgent*

- **LLM Integration:**  
  All agents communicate with the LLaMA model via the Ollama API.

- **Logging:**  
  Uses Loguru for structured logging (see `utils/logger.py`).

---

## Workflow

1. **User selects a task** (summarize, write/refine, or sanitize) in the Streamlit app.
2. **User provides input** (text, topic, or data).
3. **Main agent processes the input** using the LLaMA model.
4. **Validator agent reviews the output** for quality, accuracy, or privacy.
5. **Results and validation feedback** are displayed to the user.
6. **All actions are logged** for monitoring and debugging.

---

## Installation

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running with LLaMA model
- pip

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/medai-agent-suite.git
   cd medai-agent-suite
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Start Ollama and ensure the LLaMA model is available.**

4. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

---

## Usage

- Open your browser to the Streamlit URL (usually `http://localhost:8501`).
- Select a task from the sidebar.
- Enter the required input (text, topic, or data).
- View the generated output and validation feedback.

---

## Agents

- **SummarizeTool:** Summarizes medical text.
- **SummarizeValidatorAgent:** Validates summary quality.
- **WriteArticleTool:** Drafts research articles.
- **WriteArticleValidatorAgent:** Validates article structure and academic quality.
- **SanitizeDataTool:** Removes PHI from data.
- **SanitizeDataValidatorAgent:** Validates data sanitization.

Each agent is modular and can be extended or replaced as needed.

---

## Logging

- Logs are stored in the `logs/` directory.
- Logging is handled via Loguru for easy debugging and monitoring.

---

## Customization

- **Add new agents:**  
  Create a new agent class in the `agents/` directory and register it in the agent manager.
- **Change LLM model:**  
  Update the model used in the Ollama API calls in `agent_base.py`.
- **Modify prompts:**  
  Edit the prompt templates in each agent for different behaviors or domains.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or new features.

---

## License

This project is licensed under the MIT License.

---