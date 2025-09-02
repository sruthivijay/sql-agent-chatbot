# README for SQL Chatbot Application

## Overview

This project is a chatbot application that retrieves answers based on data from a SQL database. It supports multiple server implementations, including Node.js, Python, and .NET, allowing for flexibility in deployment and development.

## Architecture Options

The project offers two main architectural approaches:

1. **Direct SQL Approach**: 
   - This approach directly queries the SQL database to fetch responses based on user input.
   - Frameworks: Node.js with Express, Python with Flask or FastAPI, or .NET with ASP.NET Core.

2. **RAG Over SQL Approach**: 
   - This approach combines SQL queries with a language model to generate more contextually relevant responses.
   - Frameworks: Node.js with Express, Python with Flask or FastAPI, or .NET with ASP.NET Core.

## Setup Instructions

### Prerequisites

- Python 3.x or Node.js or .NET SDK
- SQL Database (e.g., PostgreSQL, MySQL)
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sql-chatbot-app
   ```

2. Set up the environment variables:
   - Copy `.env.example` to `.env` and fill in the required values.

3. Install dependencies:
   - For Python:
     ```
     cd packages/server-python
     pip install -r requirements.txt
     ```
   - For Node.js:
     ```
     cd packages/server-node
     npm install
     ```
   - For .NET:
     ```
     cd packages/server-dotnet
     dotnet restore
     ```

4. Set up the database:
   - Run the SQL scripts in the `db` directory to create the schema and seed the database.

### Running the Application

- For Python:
  ```
  cd packages/server-python
  python src/app.py
  ```

- For Node.js:
  ```
  cd packages/server-node
  npm start
  ```

- For .NET:
  ```
  cd packages/server-dotnet
  dotnet run
  ```

### Usage

Once the server is running, you can interact with the chatbot through the defined API endpoints. Refer to the documentation in the `docs` directory for detailed usage instructions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.