<p align="center">
  <img src="./assets/typing-header.svg" alt="Hi, I'm Rajan Kumar Singh - Full-Stack MERN Developer building production systems with Agentic AI" width="100%">
</p>

<p align="center">
  <img src="./assets/terminal-v3.svg" alt="Rajan Kumar Singh - terminal profile card" width="100%">
</p>

<p align="center">
  <a href="./assets/Rajan_Kumar_Singh_Resume.pdf"><img src="https://img.shields.io/badge/Resume-E11D48?style=for-the-badge&logo=adobeacrobatreader&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/rajankumarsingh01/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:cpsrajan2002@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://rajankumarsingh.me/"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=firefox&logoColor=#FF7139"/></a>
  <a href="https://leetcode.com/u/rajankumarsingh02/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/></a>
</p>

---

### 💫 About Me

- 🎓 Final-year B.Tech CSE student, building **production-ready systems**, not tutorial clones.
- 🧠 Core focus: **MERN stack + Agentic AI** — RAG, LangGraph workflows, tool-calling chatbots, event-driven architecture.
- 🛠️ Comfortable across the stack: React/Next.js on the frontend, Node.js/Express/FastAPI on the backend, MongoDB/PostgreSQL/Redis for data, Docker/Kubernetes for deployment.
- 🚀 Live demos and source code are linked under every project wherever they exist.
- 📫 Reach me: **cpsrajan2002@gmail.com**
- 💼 Open to: **MERN / Full-Stack Developer internships & entry-level roles**, especially at startups building AI-integrated products.

---

## 🔥 Featured Projects

### 🤖 AI-Augmented API Observability & Auto-Remediation Platform
> Event-driven API monitoring system with an AI layer that detects, diagnoses, and remediates production incidents.

- Built an event-driven microservices system on RabbitMQ, using a **Circuit Breaker**, retry-with-backoff, and **Dead Letter Queues** so a failing service doesn't quietly drop data.
- Added a **4-stage AI pipeline**: Z-score anomaly detection → LLM root-cause analysis → auto-restart/scale of the affected Kubernetes service, or human approval first when the fix looks risky.
- React dashboard to watch incidents and approve fixes live.
- Stack: `Node.js` `Express` `RabbitMQ` `MongoDB` `PostgreSQL` `React (Vite)` `Kubernetes` `OpenRouter LLM API`
- 🔗 [GitHub](https://github.com/rajankumarsingh01/api_monitoring_with_ai_agents)

<p align="center">
  <img src="./assets/api-monitor-login.jpg" width="38%" alt="API Monitor dashboard login">
  <br><sub>API Monitor dashboard (React + Vite)</sub>
</p>

<details>
<summary><b>🧭 See the architecture</b></summary>

```mermaid
flowchart LR
    API["Monitored APIs"] -->|metrics & events| BUS

    subgraph BUS["RabbitMQ event bus"]
        direction LR
        S1["1 · Alerting<br/>rule-based"] --> S2["2 · Anomaly detection<br/>Z-score"]
        S2 --> S3["3 · Root-cause analysis<br/>LLM via OpenRouter"]
        S3 --> S4["4 · Remediation planner<br/>risk-scored"]
    end

    S4 -->|low risk| K8S["Kubernetes API<br/>restart / scale"]
    S4 -->|high risk| HUM["Human approval<br/>React dashboard"]
    HUM -->|approved| K8S
    BUS -. "retries with backoff,<br/>then dead-letter" .-> DLQ[("Dead Letter Queue")]
    BUS --> DB[("MongoDB · PostgreSQL<br/>incidents & data")]
    DB --> DASH["React dashboard<br/>live incidents"]
```

</details>

<details>
<summary><b>🧠 Design decisions</b></summary>
<br>

**Why a human-approval step before some fixes?**  
Restarting or scaling a service is low-risk, but some fixes can make an outage worse. Each fix is risk-scored: low-risk ones run automatically, high-risk ones wait for approval on the dashboard.

**Why a Circuit Breaker, retries and Dead Letter Queues?**  
So a failing service never quietly drops data. Messages are retried with backoff, and anything that still fails is dead-lettered where it can be inspected instead of being lost.

**Why detect anomalies with Z-score before calling the LLM?**  
A cheap statistical check decides *when* something is wrong, so the LLM is only asked to explain real anomalies instead of every metric.

</details>

---

### 🎓 Kaksha — Multi-Tenant Coaching Institute SaaS + Agentic AI Microservice
> SaaS platform for coaching institutes across 5 roles, with a RAG-based AI doubt tutor running as its own service.

- Multi-tenant platform with per-institute data isolation, JWT access/refresh auth across 20+ modules, Razorpay payments, and a companion React Native (Expo) Android app.
- AI split into a separate **FastAPI + LangChain/LangGraph microservice**, called by the Node backend over internal HTTP.
- Doubt tutor answers from the institute's own notes using **RAG over MongoDB Atlas Vector Search**; a LangGraph flow retrieves, answers, then self-checks before replying.
- Also: AI question generator with a second validation pass, and a small custom eval script (RAGAS was too heavy for the free-tier setup).
- Stack: `Node.js` `Express` `MongoDB` `React` `React Native (Expo)` `FastAPI` `LangGraph` `Razorpay`
- 🔗 [Live Demo](https://coaching-management-system-three.vercel.app/) • [GitHub](https://github.com/rajankumarsingh01/coaching_management_system) • [Android APK](https://expo.dev/accounts/rajankumarsingh/projects/sankalp/builds/35ebd860-dfad-4056-91d1-105a7ff1810d)

<p align="center">
  <img src="./assets/kaksha-dashboard.jpg" width="68%" alt="Kaksha admin dashboard">
  <img src="./assets/kaksha-mobile.jpg" width="20%" alt="Kaksha mobile app login">
  <br><sub>Admin web dashboard (React) and companion Android app (React Native)</sub>
</p>

<details>
<summary><b>🧠 Design decisions</b></summary>
<br>

**Why is the AI a separate FastAPI service?**  
The LangChain/LangGraph stack is Python-first, and keeping it out of the Node backend lets the core platform and the AI side change and deploy independently. The backend calls it over internal HTTP.

**Why RAG instead of a plain LLM answer?**  
The tutor should answer from the institute's own notes, not from general knowledge. A LangGraph flow retrieves, answers, then checks itself before returning.

**Why a custom eval script instead of RAGAS?**  
RAGAS was too heavy for the free-tier setup, so a small script covers what was actually needed.

</details>

---

### 🍽️ QR Food Ordering System
> QR-based restaurant ordering platform with a tool-calling AI chatbot and real-time order tracking.

- Deployed end-to-end (Vercel + Render); customers scan → browse → chat with an AI assistant → pay → track live.
- AI chatbot (Gemini via OpenRouter) uses **native function-calling** (`search_menu`, `get_order_status`) with Redis-backed session memory — grounded in real data, not hallucinated.
- **76 automated tests** (Jest + Supertest) with a GitHub Actions CI/CD pipeline; Sentry error monitoring in production.
- Stack: `Next.js` `TypeScript` `Node.js` `MongoDB` `Redis` `Socket.IO` `Razorpay`
- 🔗 [Live Demo](https://qr-food-ordering-system-nine.vercel.app) • [GitHub](https://github.com/rajankumarsingh01/qr_food_ordering_system)

<p align="center">
  <img src="./assets/qr-landing.jpg" width="30%" alt="QR Food landing page">
  <img src="./assets/qr-menu.jpg" width="62%" alt="QR Food menu page">
  <br><sub>Landing page with customer, admin and kitchen entry points, and the table-side menu</sub>
</p>

<details>
<summary><b>🧠 Design decisions</b></summary>
<br>

**Why function-calling instead of a free-form chatbot?**  
`search_menu` and `get_order_status` fetch real data, so answers come from the live menu and order state instead of guesses.

**Why Redis for chat memory?**  
Session context needs to be fast and short-lived, so Redis keeps it per session without touching the main database.

</details>

---

<details>
<summary><b>📦 More Projects</b> (click to expand)</summary>
<br>

| Project | Description | Stack | Links |
|---|---|---|---|
| **DocFinder** | Claim-based platform to recover lost documents across India | React, Node.js, MongoDB, Cloudinary | [Live](https://docfounder-india.vercel.app/) • [GitHub](https://github.com/rajankumarsingh01/docfounder_india) |
| **AI Interview Platform** | Voice-interactive AI mock-interview tool with performance analytics | React, Node.js, Firebase, OpenRouter | [Live](https://ai-interview-platform-client.onrender.com/) • [GitHub](https://github.com/rajankumarsingh01/AI_Interview_Platform) |

</details>

---

## 🛠️ Tech Stack

**Languages:** ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)

**Frontend:** ![React](https://img.shields.io/badge/-React-20232A?style=flat-square&logo=react&logoColor=61DAFB) ![Next.js](https://img.shields.io/badge/-Next.js-000000?style=flat-square&logo=next.js&logoColor=white) ![React Native](https://img.shields.io/badge/-React_Native-20232A?style=flat-square&logo=react&logoColor=61DAFB) ![Tailwind](https://img.shields.io/badge/-TailwindCSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)

**Backend:** ![Node.js](https://img.shields.io/badge/-Node.js-6DA55F?style=flat-square&logo=node.js&logoColor=white) ![Express](https://img.shields.io/badge/-Express-404D59?style=flat-square&logo=express) ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Socket.IO](https://img.shields.io/badge/-Socket.IO-010101?style=flat-square&logo=socket.io)

**Databases:** ![MongoDB](https://img.shields.io/badge/-MongoDB-4EA94B?style=flat-square&logo=mongodb&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![Redis](https://img.shields.io/badge/-Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

**AI / Agentic:** ![LangGraph](https://img.shields.io/badge/-LangChain%20%2F%20LangGraph-1C3C3C?style=flat-square) ![RAG](https://img.shields.io/badge/-RAG%20%2B%20Vector%20Search-6D28D9?style=flat-square) ![Gemini](https://img.shields.io/badge/-Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white) ![OpenRouter](https://img.shields.io/badge/-OpenRouter-000000?style=flat-square)

**DevOps:** ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Kubernetes](https://img.shields.io/badge/-Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white) ![RabbitMQ](https://img.shields.io/badge/-RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/-GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

---

## 🌱 Currently Exploring

![Kubernetes](https://img.shields.io/badge/-Kubernetes%20(kind%2Fk3d)-326CE5?style=flat-square&logo=kubernetes&logoColor=white) ![LangGraph](https://img.shields.io/badge/-Multi--Agent%20Orchestration-1C3C3C?style=flat-square) ![System Design](https://img.shields.io/badge/-High--Scale%20System%20Design-4B0082?style=flat-square)

Deepening my understanding of container orchestration, multi-agent AI pipelines, and distributed system design — going beyond "it works" to "I can explain every design decision."

---

## 📈 GitHub Activity

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=rajankumarsingh01&theme=tokyonight&hide_border=true" />
</p>

### 🕒 Recently shipped

<!--RECENT_ACTIVITY:START-->
- [**sarkari-yojana-finder**](https://github.com/rajankumarsingh01/sarkari-yojana-finder) · _pushed 1d ago_
- [**secret-chat-app**](https://github.com/rajankumarsingh01/secret-chat-app) · _pushed 2d ago_
- [**Mern_Portfolio**](https://github.com/rajankumarsingh01/Mern_Portfolio) · _pushed 3d ago_
- [**devmark**](https://github.com/rajankumarsingh01/devmark) · _pushed 4d ago_
- [**rajan-copilot**](https://github.com/rajankumarsingh01/rajan-copilot) — AI-powered dev copilot — built phase-by-phase while learning Agentic AI · _pushed 16d ago_
<!--RECENT_ACTIVITY:END-->

<p align="center">
  <sub>Building at the intersection of full-stack engineering and agentic AI — one deployed project at a time.</sub>
</p>
