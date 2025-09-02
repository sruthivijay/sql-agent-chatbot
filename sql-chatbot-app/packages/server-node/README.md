# README for SQL Chatbot Application

## Overview

The SQL Chatbot Application is designed to provide intelligent responses to user queries based on data stored in a SQL database. This project supports multiple server implementations, including Node.js, Python, and .NET, allowing developers to choose the framework they are most comfortable with.

## Architecture Options

1. **Direct SQL Approach**: 
   - This architecture directly queries the SQL database to fetch responses based on user input.
   - Frameworks: 
     - Node.js with Express
     - Python with Flask or FastAPI
     - .NET with ASP.NET Core

2. **RAG Over SQL Approach**: 
   - This architecture combines SQL queries with a language model to generate more contextually relevant responses.
   - Frameworks: 
     - Node.js with Express
     - Python with Flask or FastAPI
     - .NET with ASP.NET Core

## Setup Instructions

### Prerequisites

- Node.js (for Node.js implementation)
- Python (for Python implementation)
- .NET SDK (for .NET implementation)
- Docker (optional, for containerized setup)
- A SQL database (e.g., MySQL, PostgreSQL)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sql-chatbot-app
   ```

2. Set up the environment variables:
   - Copy `.env.example` to `.env` and fill in the required values.

3. Install dependencies for the desired server implementation:
   - For Node.js:
     ```
     cd packages/server-node
     npm install
     ```
   - For Python:
     ```
     cd packages/server-python
     pip install -r requirements.txt
     ```
   - For .NET:
     ```
     cd packages/server-dotnet
     dotnet restore
     ```

4. Set up the database:
   - Run the SQL scripts in the `db` directory to create the schema and seed the database.

### Running the Application

- For Node.js:
  ```
  cd packages/server-node
  npm start
  ```

- For Python:
  ```
  cd packages/server-python
  python src/app.py
  ```

- For .NET:
  ```
  cd packages/server-dotnet
  dotnet run
  ```

### Usage

Once the server is running, you can interact with the chatbot via the defined API endpoints. Refer to the respective server implementation's README for specific API details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.