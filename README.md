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
```

---

### Option 2: Manual Setup (Development)

```bash
# 1. Clone the repository
git clone https://github.com/joanmarievale-collab/sprout-ai-exam.git
cd sprout-ai-exam

# 2. Create virtual environment
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Create .env file
nano .env  # or use any text editor

# 5. Start services (in separate terminals)
# Terminal 1:
cd sentiment_api_service
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2:
cd agent_system
python main.py

# Terminal 3:
streamlit run streamlit/chat_ui.py
```
---

### Prerequisites
- [Python 3.8+ (for manual setup)]
- [Docker & Docker Compose (for Docker setup)]
- [Git]
- [Groq API Key]

---

### Step-by-Step Setup

#### Step 1: Clone the Repository

```bash
git clone https://github.com/joanmarievale-collab/sprout-ai-exam.git
cd sprout-ai-exam
```
---

#### Step 2: Create .env File

```bash
# Create empty .env file
touch .env
```
##### Add the following content to .env:

---


