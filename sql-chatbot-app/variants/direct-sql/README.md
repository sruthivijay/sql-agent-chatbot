# README for Direct SQL Variant of SQL Chatbot

This README provides an overview of the Direct SQL variant of the SQL Chatbot project. This variant directly queries a SQL database to fetch responses based on user input.

## Overview

The Direct SQL variant of the SQL Chatbot is designed to provide quick and efficient responses by directly interacting with a SQL database. This approach is suitable for scenarios where the responses can be directly mapped to database queries.

## Architecture

The architecture for the Direct SQL variant consists of the following components:

- **Frontend**: A user interface built using Next.js that allows users to interact with the chatbot.
- **Backend**: A server implemented in either Node.js, Python, or .NET that handles incoming requests, queries the SQL database, and returns responses.
- **Database**: A SQL database that stores the data used by the chatbot.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd sql-chatbot-app
   ```

2. **Set Up Environment Variables**:
   Copy the `.env.example` file to `.env` and update the variables as needed.

3. **Database Setup**:
   - Run the SQL schema and seed scripts to set up the database:
     ```bash
     mysql -u <username> -p < database/schema.sql
     mysql -u <username> -p < database/seed.sql
     ```

4. **Install Dependencies**:
   Navigate to the appropriate server implementation directory (e.g., `packages/server-node`, `packages/server-python`, or `packages/server-dotnet`) and install the required dependencies.

   For Node.js:
   ```bash
   npm install
   ```

   For Python:
   ```bash
   pip install -r requirements.txt
   ```

   For .NET:
   ```bash
   dotnet restore
   ```

5. **Run the Application**:
   Start the server using the appropriate command for your implementation.

   For Node.js:
   ```bash
   npm start
   ```

   For Python:
   ```bash
   python src/app.py
   ```

   For .NET:
   ```bash
   dotnet run
   ```

6. **Access the Chatbot**:
   Open your browser and navigate to `http://localhost:3000` (or the appropriate port) to interact with the chatbot.

## Usage Guidelines

- Type your queries in the chat interface, and the chatbot will respond based on the data stored in the SQL database.
- Ensure that the database is populated with relevant data for the chatbot to provide meaningful responses.

## Conclusion

The Direct SQL variant of the SQL Chatbot provides a straightforward approach to building a chatbot that leverages existing SQL databases for quick responses. Choose this variant if you prefer direct database interactions without the complexity of additional layers.