# Muse 🔮 - Your AI-Powered Study Companion

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
<!-- Add other badges later: Build Status, Docker Pulls, etc. -->

**Muse is an open-source project leveraging cutting-edge AI to help students transform lecture content into organized, insightful, and effective study notes.**

Tired of spending hours re-listening to lectures or deciphering messy notes? Muse aims to automate the tedious parts of note-taking, allowing you to focus on understanding and learning. Simply provide your lecture text (or audio in the future!), and Muse's AI engine will generate structured summaries, identify key points, and provide detailed breakdowns.

## ✨ Vision: Structured "Vibe Coding" for Learning

Our vision is to create an intelligent learning assistant that not only summarizes information but also inspires deeper understanding and critical thinking – acting as your personal academic "Muse".

We are building this project with an **AI-first, human-oversight** approach. This embraces principles similar to **"vibe coding"** – where developers guide high-capability AI models like Gemini, Claude, GPT, DeepSeek to generate code and content rapidly. However, Muse emphasizes a **structured and responsible** approach: **human developers remain firmly in control, rigorously reviewing, testing, and *understanding* the AI-generated output before integration.** Our goal is to harness the speed of AI while ensuring quality, maintainability, and accountability, exploring the future of AI-assisted software development itself.

We plan to offer:
*   A robust **open-source version** (self-hostable via Docker).
*   Potentially, a managed **cloud version** for ease of use and additional features.

## 🚀 Key Features (Current & Planned)

*   **AI-Powered Note Generation:**
    *   `🔍 Lecture Summary:` Concise overview of the entire lecture.
    *   `💡 Key Points:` Bulleted list of the most crucial concepts and takeaways.
    *   `📚 Detailed Notes:` Structured breakdown of topics and sub-topics with details.
*   **Input:** Currently accepts raw text input.
*   **Output:** Generates notes in clean Markdown format.
*   **Self-Hosting:** Easy deployment using Docker.
*   **[Planned]** Audio Input: Support for uploading audio files (via STT).
*   **[Planned]** Visual Summary: Generation of single-slide visual summaries (SVG).
*   **[Planned]** Community Features: Sharing notes, collaborative feedback.

## 🛠️ Technology Stack (Initial)

*   **Backend:** Python (FastAPI)
*   **Frontend:** TBD (Likely React/Next.js or Vue/Nuxt.js)
*   **AI Models:** **Google Gemini 2.5 Pro, Anthropic Claude 3.7 Sonnet, OpenAI o1, o3-mini-high, DeepSeek-R1** (See [CONTRIBUTING.md](./CONTRIBUTING.md) for mandatory usage details)
*   **Deployment:** Docker, Docker Compose

## 🏁 Getting Started (Self-Hosting with Docker)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/plaid-ai/muse.git
    cd muse
    ```
2.  **Set up environment variables:**
    *   You'll need API keys for the required AI models (Gemini, Claude, OpenAI). Create a `.env` file based on `.env.example` (to be added) and fill in your keys.
    ```bash
    cp .env.example .env
    # Edit .env with your API keys
    ```
3.  **Build and run with Docker Compose:**
    ```bash
    docker-compose up --build -d
    ```
4.  Access the application in your browser (default port TBD, e.g., `http://localhost:3000`).

*(Note: Detailed setup instructions will be refined as the project progresses.)*

## 🤝 Contributing

Muse thrives on community contributions! We employ a unique AI-assisted development workflow inspired by **"vibe coding"** principles but grounded in **rigorous human oversight**. Please read our **[CONTRIBUTING.md](./CONTRIBUTING.md)** file carefully to understand our specific process, AI usage policies (including mandatory models), and the PR requirements (including prompt submission).

**Key requirements for contributors:**
*   Adherence to the Muse AI-assisted development workflow.
*   Usage of specified high-capability AI models: **Google Gemini 2.5 Pro, Anthropic Claude 3.7 Sonnet, OpenAI o1, o3-mini-high, DeepSeek-R1**.
*   **Mandatory inclusion of used prompts** in Pull Requests for transparency and reproducibility.

## 📜 License

This project is licensed under the **Apache License, Version 2.0**. See the [LICENSE](./LICENSE) file for details.

---
*Let Muse inspire your learning journey!*
