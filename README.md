# sprout-ai-exam

# Sprout AI Exam – Complete Setup Guide

---

## Table of Contents

- [Quick Start](#-quick-start)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Project Overview](#-project-overview)
- [Running the Services](#-running-the-services)
- [API Endpoints](#-api-endpoints)
- [Streamlit Chat UI](#-streamlit-chat-ui)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [System Requirements](#-system-requirements)
- [Agent Decision Logic](#-agent-decision-logic)
- [Additional Resources](#-additional-resources)
- [License](#-license)

---

## Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/joanmarievale-collab/sprout-ai-exam.git
cd sprout-ai-exam

# Create environment file
cp .env.example .env
# Edit .env and add your GROQ_API_KEY

# Build and start all services
docker-compose up --build
