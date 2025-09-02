# SQL Chatbot Application

This project is a chatbot that answers user queries based on data retrieved from a SQL database. It supports multiple architectures and frameworks, allowing for flexibility in implementation.

## Project Structure

- **README.md**: Overview of the project, setup instructions, and usage guidelines.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **.env.example**: Example of environment variables needed for the application.
- **docs/**: Documentation for the project.
  - **architecture/**: Architectural documentation.
    - **direct-sql.md**: Architecture for a direct SQL approach.
    - **rag-over-sql.md**: Architecture for a retrieval-augmented generation (RAG) approach over SQL.
- **db/**: Database-related files.
  - **schema.sql**: Defines the schema for the SQL database.
  - **seed.sql**: SQL commands to seed the database with initial data.
  - **migrations/**: Database migration scripts.
- **variants/**: Different implementation variants of the chatbot.
- **packages/**: Different server implementations (Node.js, Python, .NET, Next.js).
- **tests/**: Test files for API and end-to-end testing.
- **docker/**: Docker-related files for containerization.

## Architecture Options

1. **Direct SQL Approach**: 
   - Frameworks: Node.js with Express, Python with Flask or FastAPI, .NET with ASP.NET Core.
   - Directly queries the SQL database to fetch responses based on user input.

2. **RAG Over SQL Approach**: 
   - Frameworks: Node.js with Express, Python with Flask or FastAPI, .NET with ASP.NET Core.
   - Combines SQL queries with a language model to generate more contextually relevant responses.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sql-chatbot-app
   ```

2. Install dependencies for the chosen server implementation (Node.js, Python, or .NET).

3. Set up the database:
   - Run the SQL schema and seed files to initialize the database.

4. Configure environment variables:
   - Copy `.env.example` to `.env` and fill in the required values.

5. Start the server:
   - Follow the instructions in the respective server's README file.

## Usage Guidelines

- Interact with the chatbot through the defined API endpoints.
- Refer to the documentation in the `docs/` directory for detailed architectural insights and implementation specifics.

Feel free to explore the different variants and server implementations to find the best fit for your needs!