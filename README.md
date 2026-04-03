🚀 AI Resume Analyzer – Microservices DevOps Project
📌 Overview

The AI Resume Analyzer is a cloud-native, microservices-based application designed to analyze resume text and extract meaningful insights such as keyword density and word count.

This project demonstrates end-to-end DevOps implementation, including containerization, CI/CD automation, code quality checks, and security scanning.

🎯 Objectives
Build a scalable microservices architecture
Implement CI/CD pipeline using Jenkins
Integrate code quality analysis (SonarQube)
Perform container security scanning (Trivy)
Deploy services using Docker Compose
Simulate real-world DevOps workflow
🏗️ System Architecture
Client Request
     ↓
API Gateway (FastAPI)
     ↓
-------------------------
|        |              |
Parser   AI Service   (Future Services)
Service
🔹 Components
1. API Gateway
Entry point for all client requests
Routes requests to appropriate microservices
Built using FastAPI
2. Parser Service
Extracts:
Word count
Keywords
Lightweight and fast
3. AI Service (Optional Enhancement)
Can integrate NLP models (spaCy / Transformers)
Enables advanced resume analysis
⚙️ Technology Stack
Category	Tools Used
Backend Framework	FastAPI (Python)
Containerization	Docker
Orchestration	Docker Compose
CI/CD	Jenkins
Code Quality	SonarQube
Security Scanning	Trivy
Version Control	Git & GitHub
📁 Project Structure
ai-project/
│
├── api-gateway/
│   ├── main.py
│   └── Dockerfile
│
├── parser-service/
│   ├── main.py
│   └── Dockerfile
│
├── ai-service/
│   ├── main.py
│   └── Dockerfile
│
├── docker-compose.yml
├── requirements.txt
└── README.md
🚀 Setup & Installation
🔹 Prerequisites

Make sure you have installed:

Docker
Docker Compose
Python (optional for local testing)
Git
🔹 Step 1: Clone Repository
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
🔹 Step 2: Build & Run Containers
docker-compose up -d --build
🔹 Step 3: Verify Running Services
docker ps

Expected services:

api-gateway
parser-service
ai-service
🌐 API Usage
✅ Base URL
http://localhost:8000
🔹 1. Health Check
GET /

Response:

{
  "service": "Running"
}
🔹 2. Resume Parsing (Browser Friendly)
GET /parse?text=your_resume_text

Example:

http://localhost:8000/parse?text=I am a DevOps Engineer skilled in Docker Kubernetes
🔹 Sample Response
{
  "word_count": 10,
  "keywords": ["I", "am", "a", "DevOps", "Engineer"]
}
🐳 Docker Configuration

Each microservice contains:

Dockerfile
Lightweight Python image
FastAPI server
🔹 Docker Compose Responsibilities
Network creation
Service communication
Container orchestration
🔄 CI/CD Pipeline (Jenkins)
Pipeline Flow:
Pull code from GitHub
Build Docker images
Run containers
Perform quality checks
Scan images for vulnerabilities
📊 Code Quality – SonarQube
Features:
Detects bugs
Identifies code smells
Measures coverage
Setup Steps:
Run SonarQube server
Generate token
Add sonar-project.properties
Run scanner in Jenkins
🔐 Security Scanning – Trivy
Scan Docker Images
trivy image ai-service
What it detects:
OS vulnerabilities
Library issues
Security risks
⚡ Challenges Faced
Docker build failures due to space issues
Port conflicts between services
Service communication debugging
Dependency management
🚀 Future Enhancements
🔹 Kubernetes deployment (EKS / AKS)
🔹 CI/CD using GitHub Actions
🔹 Advanced NLP scoring
🔹 Frontend UI (React)
🔹 Monitoring (Prometheus + Grafana)
📈 DevOps Highlights

✔ Microservices architecture
✔ Containerized deployment
✔ Automated CI/CD pipeline
✔ Code quality integration
✔ Security scanning implemented

👨‍💻 Author

MHA.Ramayya
