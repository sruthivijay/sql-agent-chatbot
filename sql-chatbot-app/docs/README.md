# SQL Chatbot Application

This project is designed to create a chatbot that answers user queries based on data retrieved from a SQL database. The chatbot can be implemented using different architectures and frameworks, allowing flexibility based on your preferences and requirements.

## Project Structure

The project is organized into several directories and files, each serving a specific purpose:

- **README.md**: Overview of the project, setup instructions, and usage guidelines.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **.env.example**: Example of environment variables needed for the application.
- **docs/**: Contains documentation for the project, including architectural details.
  - **architecture/**: Architectural documentation for different approaches.
    - **direct-sql.md**: Architecture for a direct SQL approach.
    - **rag-over-sql.md**: Architecture for a retrieval-augmented generation (RAG) approach over SQL.
- **db/**: Contains SQL database schema, seed data, and migration scripts.
- **variants/**: Different implementation variants of the chatbot.
- **packages/**: Various server implementations (Node.js, Python, .NET) and a Next.js frontend.
- **tests/**: Contains test files for API and end-to-end testing.
- **docker/**: Docker-related files for containerization.

## Architecture Options

1. **Direct SQL Approach**: 
   - **Frameworks**: 
     - Node.js with Express
     - Python with Flask or FastAPI
     - .NET with ASP.NET Core
   - **Description**: This approach directly queries the SQL database to fetch responses based on user input.

2. **RAG Over SQL Approach**: 
   - **Frameworks**: 
     - Node.js with Express
     - Python with Flask or FastAPI
     - .NET with ASP.NET Core
   - **Description**: This approach combines SQL queries with a language model to generate more contextually relevant responses.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sql-chatbot-app
   ```

2. Install dependencies for the chosen server implementation (Node.js, Python, or .NET).

3. Set up the database:
   - Modify the `.env` file with your database credentials.
   - Run the SQL scripts in the `db/` directory to set up the schema and seed data.

4. Start the server:
   - For Node.js: `npm start`
   - For Python: `python src/app.py`
   - For .NET: `dotnet run`

5. Access the chatbot interface through the frontend implementation (Next.js).

## Usage Guidelines

- Interact with the chatbot through the provided frontend interface.
- Ensure the database is populated with relevant data for meaningful responses.
- Explore different architectural approaches by checking the documentation in the `docs/architecture/` directory.

Feel free to contribute to the project by adding new features, improving documentation, or fixing bugs!