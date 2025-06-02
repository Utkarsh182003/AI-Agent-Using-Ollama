# Multi-Agent AI System

A modular, multi-agent AI system for text summarization, research article writing, and data sanitization using LLaMA models via Groq, with a user-friendly Streamlit interface.

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

This **Multi-Agent AI System** is designed to assist users in generating summaries, writing research articles, and sanitizing sensitive data. It leverages the Groq API and implements a modular agent-based architecture to ensure high-quality outputs with validation at each step.

---

## Features

- **Text Summarization:**  
  Generate concise summaries of any text with automated quality validation.

- **Research Article Writing & Refinement:**  
  Draft research articles from topics or outlines, refine for clarity and structure, and validate for academic standards.

- **Data Sanitization:**  
  Automatically identify and remove sensitive information from data, with validation to ensure privacy compliance.

- **Validator Agents:**  
  Each main task is paired with a validator agent that reviews and rates the output for quality and accuracy.

- **User-Friendly Interface:**  
  Built with Streamlit for easy, interactive use.

- **Robust Logging:**  
  Comprehensive logging system for transparency and debugging.

---

## Architecture

- **Streamlit Frontend:**  
  Provides an intuitive web interface for user interaction.

- **Agent Manager:**  
  Coordinates the execution of main and validator agents for each task.

- **Agents:**  
  - *SummarizeTool* & *SummarizeValidatorAgent*
  - *WriteArticleTool* & *WriteArticleValidatorAgent*
  - *SanitizeDataTool* & *SanitizeDataValidatorAgent*

- **LLM Integration:**  
  All agents communicate with language models via the Groq API.

- **Logging:**  
  Uses Loguru for structured logging (see `utils/logger.py`).

---

## Installation

### Prerequisites

- Python 3.8+
- Groq API key
- pip

### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/multi-agent-ai-system.git
   cd multi-agent-ai-system
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file with:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

4. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```

---

## Usage

1. Open your browser to the Streamlit URL (usually `http://localhost:8501`).
2. Select a task from the sidebar:
   - Summarize Text
   - Write and Refine Research Article
   - Sanitize Data
3. Enter the required input
4. Click the corresponding button to process
5. View the generated output and validation feedback

---

## Agents

- **SummarizeTool:** Creates concise summaries of any text.
- **SummarizeValidatorAgent:** Validates summary quality and accuracy.
- **WriteArticleTool:** Drafts research articles from topics.
- **WriteArticleValidatorAgent:** Validates article structure and quality.
- **SanitizeDataTool:** Removes sensitive information from data.
- **SanitizeDataValidatorAgent:** Validates sanitization completeness.

Each agent is modular and can be extended or modified as needed.

---

## Logging

- Logs are stored in the `logs/` directory
- Comprehensive logging via Loguru for debugging and monitoring
- Tracks all agent interactions and potential errors

---

## Customization

- **Add new agents:**  
  Create new agent classes in the `agents/` directory and register them in the agent manager.
- **Modify prompts:**  
  Edit the prompt templates in each agent for different behaviors or requirements.
- **Configure API settings:**  
  Adjust API parameters in the configuration files for different models or requirements.

---

## Contributing

Contributions are welcome! Please feel free to:
- Open issues for bugs or feature requests
- Submit pull requests for improvements
- Suggest new agent types or functionalities

---

## License

This project is licensed under the MIT License.

---