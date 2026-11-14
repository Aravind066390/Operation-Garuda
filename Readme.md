# Operation Garuda

**AI-Powered Civic Intelligence and Complaint Management Platform**

Operation Garuda is an intelligent civic complaint management platform designed to collect, analyze, classify, prioritize, and manage public complaints. It integrates AI-driven complaint processing with a multi-interface application architecture, local databases, and a C/C++ network-based file-transfer system.

---

## 1. Project Overview

Operation Garuda aims to improve civic issue reporting and management through intelligent complaint processing.

The platform handles issues such as:

- Road damage and potholes
- Waste management
- Water supply problems
- Drainage and sanitation
- Public infrastructure issues
- Other community-related complaints

It processes complaints, evaluates their priority, identifies potential duplicates, stores structured records, and transfers complaint data to a separate receiver system.

## 2. Key Features

- **AI-Based Classification:** Automatically analyzes complaint descriptions and assigns relevant categories.
- **Priority Assessment:** Evaluates complaints using priority scores, labels, and reasoning.
- **Duplicate Detection:** Identifies potentially repeated complaints.
- **Location Intelligence:** Associates complaints with geographic and area information.
- **Complaint Management:** Maintains complaint records and their status.
- **Interactive Dashboard:** Displays complaint information and application insights.
- **Admin Interface:** Provides an interface for managing complaints and backend operations.
- **JSON-Based Transfer:** Transfers individual complaint records using the existing C/C++ transfer protocol.
- **Receiver Database:** Imports validated complaint records into a separate SQLite database.

## 3. Technology Stack

| Component | Technology |
|---|---|
| Original dashboard | Python, Streamlit |
| Backend API | Python, FastAPI |
| Frontend | React, Vite, JavaScript |
| AI processing | Python |
| Local database | SQLite |
| Receiver database | SQLite |
| File transfer | C/C++ |
| Data exchange | JSON |
| Operating environment | Linux |

## 4. System Architecture

```text
                      USERS
                        |
             +----------+----------+
             |                     |
        Streamlit UI           React UI
             |                     |
             |                 FastAPI
             |                     |
             |              AI Processing
             |                     |
             |           Classification & Priority
             |                     |
             |               Local SQLite
             |                     |
             |               JSON Generator
             |                     |
             |                server_api
             |                     |
             |                C/C++ Sender
             |                     |
             |               Network Transfer
             |                     |
             |                C/C++ Server
             |                     |
             |              Receiver Storage
             |                     |
             |               JSON Importer
             |                     |
             |              Receiver SQLite
```

The Streamlit dashboard and React interface are separate application interfaces. The React application communicates with the FastAPI backend through HTTP requests.

## 5. Project Structure

```text
Operation-Garuda/
│
├── api/
│   └── main.py
│
├── app/
│   └── main.py
│
├── civiclens/
│   ├── database.py
│   └── ai_engine.py
│
├── frontend/
│   ├── src/
│   │   └── App.jsx
│   ├── package.json
│   └── ...
│
├── receiver/
│   ├── importer.py
│   └── receiver.db
│
├── linux_transfer/
│   ├── server_api
│   ├── sender
│   ├── init_server
│   └── storage/
│       └── users/
│           └── archlinux/
│
├── outgoing_packages/
├── civiclens.db
├── app.py
└── README.md
```

## 6. Installation and Setup

### Requirements

- Linux environment
- Python 3
- Node.js and npm
- GCC compiler
- SQLite
- Required Python packages

### Clone the repository

```bash
git clone <REPOSITORY_URL>
cd Operation-Garuda
```

### Set up Python

```bash
python3 -m venv .venv-linux
source .venv-linux/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Install frontend dependencies

```bash
cd frontend
npm install
cd ..
```

## 7. Running the Applications

### A. Original Streamlit Dashboard

```bash
cd ~/Operation-Garuda
source .venv-linux/bin/activate
streamlit run app.py
```

Open:

`http://localhost:8501`

### B. FastAPI Backend

Open a separate terminal:

```bash
cd ~/Operation-Garuda
source .venv-linux/bin/activate

python -m uvicorn api.main:app \
    --host 127.0.0.1 \
    --port 8000 \
    --reload
```

API documentation:

`http://127.0.0.1:8000/docs`

Health check:

`http://127.0.0.1:8000/api/health`

### C. React Admin Interface

Open another terminal:

```bash
cd ~/Operation-Garuda/frontend
npm run dev -- --host 127.0.0.1
```

Open:

`http://127.0.0.1:5173`

### D. C/C++ Transfer Server

Open another terminal:

```bash
cd ~/Operation-Garuda/linux_transfer
./init_server
```

Keep the server running during transfers.

If required, rebuild the sender and API wrapper:

```bash
gcc -Wall -Wextra -O2 sender.c -o sender
gcc -Wall -Wextra -O2 server_api.c -o server_api
```

## 8. Complaint Processing and Transfer Workflow

1. A user submits a civic complaint.
2. The FastAPI backend receives the complaint.
3. AI processing evaluates its category and priority.
4. Duplicate information and location details are maintained.
5. The complaint is stored in the local SQLite database.
6. A structured JSON file is generated.
7. The existing C/C++ `server_api` initiates the transfer.
8. The C/C++ sender transmits the JSON file.
9. The receiver stores the file in its designated user directory.
10. The Python importer validates the JSON.
11. Validated complaint records are inserted into the receiver database.
12. Successfully imported JSON files are deleted from the receiver inbox.

### JSON Data Format

```json
{
  "schema_version": 1,
  "complaint_uuid": "unique-complaint-identifier",
  "source_complaint_id": 123,
  "complaint": {
    "description": "Road damage reported",
    "category": "Road Infrastructure",
    "area": "Example Area",
    "people_affected": 10,
    "priority": {
      "score": 85,
      "label": "High",
      "reason": "High impact on the public"
    },
    "duplicate": {
      "duplicate_of": null,
      "similarity": null
    },
    "status": "Pending",
    "created_at": "2026-11-14T10:00:00",
    "location": {
      "latitude": 12.0,
      "longitude": 76.0
    }
  }
}
```

The example values are illustrative. Actual values are generated from submitted complaint records.

### Receiver Storage

Incoming JSON files:

```text
linux_transfer/storage/users/archlinux/
```

Receiver database:

```text
receiver/receiver.db
```

The current implementation transfers individual JSON files, not ZIP archives.

## 9. Database Design

| Database | Responsibility |
|---|---|
| `civiclens.db` | Application-side complaint records |
| `receiver/receiver.db` | Successfully imported complaint records |

Receiver records include complaint UUID, description, category, area, coordinates, affected population, priority information, duplicate information, status, and timestamp.

## 10. API Documentation

The FastAPI application exposes its available endpoints through:

`http://127.0.0.1:8000/docs`

Health endpoint:

```http
GET /api/health
```

Refer to the generated API documentation for the current complaint submission and management endpoints.

## 11. Important Notes

- Start the required backend and transfer server processes before using their respective features.
- Keep the C/C++ receiver server running during file transfers.
- Ensure server IP configuration, credentials, and recipient username are correct.
- The React frontend must point to the correct FastAPI URL.
- Failed JSON imports retain their files for investigation.
- Successful file transfer alone does not prove successful database import. Verify the receiver database when testing the complete workflow.
- Never commit passwords, API keys, or other credentials to a public repository.

## 12. Future Enhancements

- Role-based authentication and access control
- Improved AI classification and duplicate detection
- Real-time complaint tracking
- Geospatial complaint visualization
- Advanced civic analytics
- Transfer retry and recovery mechanisms
- Automated integration testing
- Secure remote deployment

---

## Project Vision

**Operation Garuda** aims to bring intelligent civic complaint processing and practical systems engineering together in one integrated platform.

It combines AI, software engineering, database systems, and C/C++ network programming to build a technology-driven approach to civic issue management.

**OPERATION GARUDA — Intelligence. Infrastructure. Impact.**
