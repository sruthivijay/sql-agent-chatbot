# Docker Chatbot Application

This directory contains the necessary files and instructions for running the SQL Chatbot application using Docker.

## Getting Started

To get started with the SQL Chatbot application using Docker, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd sql-chatbot-app
   ```

2. **Build the Docker Images**:
   Use the following command to build the Docker images defined in the `docker-compose.yml` file:
   ```bash
   docker-compose build
   ```

3. **Run the Application**:
   Start the application using Docker Compose:
   ```bash
   docker-compose up
   ```

4. **Access the Application**:
   Once the application is running, you can access it at `http://localhost:3000` (or the port specified in your `docker-compose.yml`).

## Configuration

Make sure to set up your environment variables in a `.env` file based on the `.env.example` provided in the root directory. This file should include database connection details and any other necessary configurations.

## Stopping the Application

To stop the application, you can use:
```bash
docker-compose down
```

## Additional Information

For more details on the architecture and implementation of the chatbot, refer to the documentation in the `docs` directory. You can also explore the different server implementations available in the `packages` directory.

## Troubleshooting

If you encounter any issues while running the application, check the logs for errors:
```bash
docker-compose logs
```

Feel free to reach out for support or contribute to the project!