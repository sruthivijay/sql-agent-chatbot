-- Users table to store user information
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Queries table to store user queries
CREATE TABLE queries (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    query_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Responses table to store chatbot responses
CREATE TABLE responses (
    id SERIAL PRIMARY KEY,
    query_id INT REFERENCES queries(id),
    response_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Metadata table to store additional information
CREATE TABLE metadata (
    id SERIAL PRIMARY KEY,
    query_id INT REFERENCES queries(id),
    key VARCHAR(100),
    value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);