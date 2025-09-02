# README.md for SQL Chatbot Application

# SQL Chatbot Application

This project is a chatbot that answers user queries based on data retrieved from a SQL database. It offers two architectural approaches: a Direct SQL approach and a Retrieval-Augmented Generation (RAG) approach over SQL. The application is designed to be modular, allowing for easy integration of different server implementations and frontend frameworks.

## Architecture Options

1. **Direct SQL Approach**: 
   - This approach directly queries the SQL database to fetch responses based on user input.
   - Frameworks: 
     - Node.js with Express
     - Python with Flask or FastAPI
     - .NET with ASP.NET Core

2. **RAG Over SQL Approach**: 
   - This approach combines SQL queries with a language model to generate more contextually relevant responses.
   - Frameworks:
     - Node.js with Express
     - Python with Flask or FastAPI
     - .NET with ASP.NET Core

## Project Structure

- **db/**: Contains SQL database schema, seed data, and migration scripts.
- **docs/**: Documentation for the project, including architectural details.
- **packages/**: Different server implementations (Node.js, Python, .NET) and the Next.js frontend.
- **tests/**: Contains test files for API and end-to-end testing.
- **docker/**: Docker configuration for setting up the application environment.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sql-chatbot-app
   ```

2. Install dependencies for the desired server implementation:
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

3. Set up the database:
   - Update the `.env` file with your database configuration.
   - Run the migration scripts to set up the database schema.

4. Start the server:
   - For Node.js:
     ```
     npm start
     ```
   - For Python:
     ```
     python src/app.py
     ```
   - For .NET:
     ```
     dotnet run
     ```

5. Run the Next.js frontend:
   ```
   cd packages/web-nextjs
   npm install
   npm run dev
   ```

## Usage Guidelines

- Access the chatbot interface through the Next.js frontend.
- Interact with the chatbot by typing your queries, and it will respond based on the data from the SQL database.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.