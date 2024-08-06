# Social Network Analysis

This project is a Social Network Analysis API built using FastAPI and Neo4j. It allows you to add users, create friendships, and retrieve friends.

## Requirements

- Python 3.7+
- Neo4j
- FastAPI
- Uvicorn

## Setup

1. Install Neo4j and create a new database.
2. Set up a username and password for the database.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd social_network_analysis
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

5. The API will be available at `http://127.0.0.1:8000`

## API Endpoints

- `POST /add_user`: Add a new user.
- `POST /add_friend`: Create a friendship between two users.
- `GET /friends/{username}`: Retrieve friends of a user.
