네, 업데이트된 `README.md` 내용을 한국어로 번역해 드릴게요.

---

# Muse 🔮 - 당신의 AI 기반 학습 동반자

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
<!-- 추후 빌드 상태, Docker Pulls 등 다른 배지 추가 예정 -->

**Muse는 최첨단 AI를 활용하여 학생들이 강의 콘텐츠를 체계적이고 통찰력 있으며 효과적인 학습 노트로 변환하도록 돕는 오픈소스 프로젝트입니다.**

강의를 다시 듣거나 지저분한 노트를 해독하는 데 몇 시간씩 소비하는 데 지치셨나요? Muse는 지루한 노트 필기 과정을 자동화하여, 당신이 이해와 학습에 집중할 수 있도록 돕습니다. 강의 텍스트(향후 오디오 지원 예정!)를 제공하기만 하면, Muse의 AI 엔진이 구조화된 요약, 핵심 포인트 식별, 세부 내용 분석을 생성합니다.

## ✨ 비전: 학습을 위한 체계적인 "Vibe Coding"

우리의 비전은 단순히 정보를 요약하는 것을 넘어, 더 깊은 이해와 비판적 사고를 고취시키는 지능형 학습 보조 도구를 만드는 것입니다 – 당신의 개인적인 학문적 '뮤즈' 역할을 합니다.

저희는 이 프로젝트를 **AI 우선, 인간 감독(AI-first, human-oversight)** 접근 방식으로 구축하고 있습니다. 이는 개발자가 Gemini, Claude, GPT, DeepSeek과 같은 고성능 AI 모델을 활용하여 코드와 콘텐츠를 빠르게 생성하는 **"vibe coding"** 과 유사한 원칙을 수용합니다. 하지만 Muse는 **체계적이고 책임감 있는 접근 방식**을 강조합니다: **인간 개발자가 AI 생성 결과물을 통합하기 전에 엄격하게 검토하고, 테스트하고, *이해*하며 확고하게 통제합니다.** 우리의 목표는 AI의 속도를 활용하면서도 품질, 유지보수성, 책임성을 보장하고, AI 지원 소프트웨어 개발의 미래를 탐구하는 것입니다.

저희는 다음을 제공할 계획입니다:
*   강력한 **오픈소스 버전**(Docker를 통한 셀프 호스팅 가능).
*   잠재적으로, 사용 편의성과 추가 기능을 위한 관리형 **클라우드 버전**.

## 🚀 주요 기능 (현재 및 계획 중)

*   **AI 기반 노트 생성:**
    *   `🔍 강의 요약:` 전체 강의에 대한 간결한 개요.
    *   `💡 핵심 포인트:` 가장 중요한 개념과 요점의 글머리 기호 목록.
    *   `📚 세부 노트:` 주제 및 하위 주제에 대한 구조화된 상세 분석.
*   **입력:** 현재 원시 텍스트 입력을 받습니다.
*   **출력:** 깔끔한 마크다운 형식으로 노트를 생성합니다.
*   **셀프 호스팅:** Docker를 사용한 간편한 배포.
*   **[계획 중]** 오디오 입력: 오디오 파일 업로드 지원 (STT 통해).
*   **[계획 중]** 시각적 요약: 단일 슬라이드 시각적 요약 생성 (SVG).
*   **[계획 중]** 커뮤니티 기능: 노트 공유, 협업 피드백.

## 🛠️ 기술 스택 (초기)

*   **백엔드:** Python (FastAPI)
*   **프론트엔드:** 미정 (React/Next.js 또는 Vue/Nuxt.js 가능성 높음)
*   **AI 모델:** **Google Gemini 2.5 Pro, Anthropic Claude 3.7 Sonnet, OpenAI o1, o3-mini-high, DeepSeek-R1** ([CONTRIBUTING.md](./CONTRIBUTING.md)에서 필수 사용 세부 정보 확인)
*   **배포:** Docker, Docker Compose

## 🏁 시작하기 (Docker로 셀프 호스팅)

1.  **저장소 복제:**
    ```bash
    git clone https://github.com/plaid-ai/muse.git
    cd muse
    ```
2.  **환경 변수 설정:**
    *   필수 AI 모델(Gemini, Claude, OpenAI)용 API 키가 필요합니다. `.env.example`(추가 예정)을 기반으로 `.env` 파일을 만들고 키를 입력하세요.
    ```bash
    cp .env.example .env
    # .env 파일을 편집하여 API 키 입력
    ```
3.  **Docker Compose로 빌드 및 실행:**
    ```bash
    docker-compose up --build -d
    ```
4.  브라우저에서 애플리케이션에 접속합니다 (기본 포트 미정, 예: `http://localhost:3000`).

*(참고: 상세 설정 지침은 프로젝트 진행에 따라 구체화될 예정입니다.)*

## 🤝 기여하기

Muse는 커뮤니티 기여를 통해 성장합니다! 저희는 **"vibe coding"** 원칙에서 영감을 받았지만 **엄격한 인간 감독**에 기반한 독특한 AI 지원 개발 워크플로우를 사용합니다. [CONTRIBUTING.md](./CONTRIBUTING.md) 파일을 주의 깊게 읽어 저희의 구체적인 프로세스, AI 사용 정책(필수 모델 포함), PR 요구사항(프롬프트 제출 포함)을 이해해 주십시오.

**기여자를 위한 핵심 요구사항:**
*   Muse AI 지원 개발 워크플로우 준수.
*   지정된 고성능 AI 모델 사용: **Google Gemini 2.5 Pro, Anthropic Claude 3.7 Sonnet, OpenAI o1, o3-mini-high, DeepSeek-R1**.
*   투명성과 재현성을 위해 Pull Request에 **사용한 프롬프트 필수 포함**.

## 📜 라이선스

이 프로젝트는 **Apache License, Version 2.0**에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](./LICENSE) 파일을 참조하십시오.

---
*Muse가 당신의 학습 여정에 영감을 불어넣도록 하세요!*