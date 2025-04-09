# Contributing to Muse 🔮

First off, thank you for considering contributing to Muse! We're excited to build this AI-powered study companion with the community.

Muse is not just about the end product; it's also an experiment in **AI-assisted software development**. We aim to leverage powerful AI models for tasks like code generation, design ideation, and documentation, with humans providing oversight, guidance, and final validation.

## Our Approach: Structured "Vibe Coding" with Human Responsibility

We embrace elements of what's recently been termed **"vibe coding"**: using natural language prompts to guide powerful Large Language Models (LLMs) in generating software components rapidly. This allows us to potentially accelerate development and explore creative solutions.

However, the Muse project adopts a **structured and responsible approach** to this paradigm. While we encourage leveraging the specified high-capability AI models, **we strictly require rigorous human involvement:**

*   **Understanding is Mandatory:** Unlike some interpretations of "vibe coding" where developers might accept code without full comprehension, Muse contributors **must review, test, and fully understand** any AI-generated code or content before submitting it.
*   **Human Oversight is Key:** Humans define the requirements, design the prompts, critically evaluate the AI's output, perform necessary modifications, and take **full responsibility** for the final integrated code.
*   **Transparency:** The AI models used and the exact prompts are required in Pull Requests to ensure transparency and allow for reproducibility and learning within the community.

Our goal is to harness the *speed and capability* of AI while mitigating the risks (like hidden bugs or security flaws) associated with unverified code, ensuring a high-quality, maintainable, and trustworthy open-source project.

## Code of Conduct

This project and everyone participating in it are governed by the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior. *(Note: Add a CODE_OF_CONDUCT.md file)*

## ❓ How Can I Contribute?

*   Reporting Bugs
*   Suggesting Enhancements or New Features
*   Writing or Improving Documentation
*   Submitting Pull Requests for Code Changes (following our specific workflow below)
*   Providing Feedback on AI-generated outputs

## 🤖 The Muse AI-Assisted Development Workflow ("Structured Vibe Coding")

Our core development process relies heavily on AI collaboration, guided by human expertise:

1.  **Issue Identification:** A bug report or feature request is created as a GitHub Issue. Clear requirements and acceptance criteria are defined by humans.
2.  **Design & Prompt Engineering (Human + AI Assist):**
    *   Humans define the overall approach, architecture, or design concept.
    *   Humans craft detailed prompts for one of the **required AI models**, specifying the task, constraints, desired output, etc.
3.  **AI Generation (AI):** Use one of the **required AI models** (see below) to generate code, design elements, text, or documentation based on the human-engineered prompt.
4.  **Human Review, Understanding & Refinement (Human - CRITICAL STEP):**
    *   **Thoroughly review** the AI's output for correctness, efficiency, security, adherence to style guides, and alignment with project goals.
    *   **Ensure you fully understand** the logic and implications of the generated code/content. **Do not integrate code you don't understand.**
    *   Debug, refactor, and modify the AI-generated code as needed. You are the final owner and responsible party for the code.
    *   Iterate with the AI if necessary, refining prompts for better results.
5.  **Integration & Testing (Human + Tools):** Integrate the *understood and verified* code. Write or update unit/integration tests (AI can assist in drafting these, but they require rigorous human review and validation). Ensure all tests pass.
6.  **Documentation (AI Assist + Human):** Update relevant documentation. AI can help draft these, but final review and accuracy checks are human responsibilities.
7.  **Pull Request (Human):** Submit a Pull Request following the guidelines below, **mandatorily including the AI model used and the full prompts**.

## 🧠 Required AI Models (Mandatory for AI-Generated Contributions)

To ensure a high standard of AI assistance, consistency, and explore the capabilities of state-of-the-art models, contributions involving AI generation **must** use one of the following specific models:

*   **Google Gemini w.5 Pro**
*   **Anthropic Claude 3.7 Sonnet**
*   **OpenAI o1**
*   **OpenAI o3-mini-high**
*   **DeepSeek-R1**

Using other models for AI-generated contributions is **not accepted** at this time. This policy helps us maintain a quality baseline and focus our exploration. Please clearly state which required model you used in your Pull Request.

## Pull Request (PR) Process

1.  **Fork & Branch:** Fork the repository and create a new branch from `main` for your work.
2.  **Commit Changes:** Make your changes, adhering to the Muse AI-Assisted Workflow. Write clear commit messages.
3.  **Ensure Tests Pass:** Run relevant tests locally.
4.  **Submit PR:** Push your branch to your fork and open a Pull Request against the `plaid-ai/muse:main` branch.
5.  **PR Template (Fill Thoroughly - Mandatory Fields):**
    *   Clear description of changes.
    *   Issue number(s) addressed.
    *   `**AI Tool Used:**` (Specify the **required model** used, e.g., `Google Gemini 2.5 Pro via API`)
    *   `**Prompt(s) Used:**` **(MANDATORY)** Provide the **exact, full prompts** used. Use collapsible sections (`<details>`) or link to a Gist if very long.
    *   `**Summary of AI Output:**` Briefly describe what the AI generated.
    *   `**Human Review & Modifications:**` **(MANDATORY)** Detail your review process, confirming your understanding, and list any significant changes made to the AI output. This demonstrates responsible AI usage.
6.  **Code Review:** Respond to feedback and make necessary adjustments.

## 💻 Setting Up Your Development Environment

*(Instructions to be added here as the project structure solidifies.)*

## 🎨 Coding Style & Conventions

*   **Python:** Follow PEP 8. Use `black` for formatting and `flake8`/`ruff` for linting.
*   **Frontend (TBD):** Use `prettier`.
*   Strive for clear, readable, well-commented code, especially clarifying the integration points and logic of AI-generated parts.

## 📜 License

By contributing to Muse, you agree that your contributions will be licensed under the Apache License, Version 2.0.

---
Thank you for helping Muse become an amazing tool for students, and for participating in our exploration of responsible AI-assisted development!