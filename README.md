<h1 align="center">Hi, I'm Rajan Kumar Singh 👋</h1>
<h3 align="center">Full-Stack MERN Developer building production systems with Agentic AI</h3>

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
- 💻 Currently a **Full Stack Developer Intern at FluentFeed**, shipping features into a real AI English-learning codebase (React, TypeScript, Node.js, Gemini API).
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

---

### 🎓 Kaksha — Multi-Tenant Coaching Institute SaaS + Agentic AI Microservice
> SaaS platform for coaching institutes across 5 roles, with a RAG-based AI doubt tutor running as its own service.

- Multi-tenant platform with per-institute data isolation, JWT access/refresh auth across 20+ modules, Razorpay payments, and a companion React Native (Expo) Android app.
- AI split into a separate **FastAPI + LangChain/LangGraph microservice**, called by the Node backend over internal HTTP.
- Doubt tutor answers from the institute's own notes using **RAG over MongoDB Atlas Vector Search**; a LangGraph flow retrieves, answers, then self-checks before replying.
- Also: AI question generator with a second validation pass, and a small custom eval script (RAGAS was too heavy for the free-tier setup).
- Stack: `Node.js` `Express` `MongoDB` `React` `React Native (Expo)` `FastAPI` `LangGraph` `Razorpay`
- 🔗 [Live Demo](https://coaching-management-system-three.vercel.app/) • [GitHub](https://github.com/rajankumarsingh01/coaching_management_system) • [Android APK](https://expo.dev/accounts/rajankumarsingh/projects/sankalp/builds/35ebd860-dfad-4056-91d1-105a7ff1810d)

---

### 🍽️ QR Food Ordering System
> QR-based restaurant ordering platform with a tool-calling AI chatbot and real-time order tracking.

- Deployed end-to-end (Vercel + Render); customers scan → browse → chat with an AI assistant → pay → track live.
- AI chatbot (Gemini via OpenRouter) uses **native function-calling** (`search_menu`, `get_order_status`) with Redis-backed session memory — grounded in real data, not hallucinated.
- **76 automated tests** (Jest + Supertest) with a GitHub Actions CI/CD pipeline; Sentry error monitoring in production.
- Stack: `Next.js` `TypeScript` `Node.js` `MongoDB` `Redis` `Socket.IO` `Razorpay`
- 🔗 [Live Demo](https://qr-food-ordering-system-nine.vercel.app) • [GitHub](https://github.com/rajankumarsingh01/qr_food_ordering_system)

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

<p align="center">
  <sub>Building at the intersection of full-stack engineering and agentic AI — one deployed project at a time.</sub>
</p>
