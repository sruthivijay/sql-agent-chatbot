// src/types/index.ts

export interface UserInput {
    userId: string;
    message: string;
    timestamp: Date;
}

export interface ChatResponse {
    responseId: string;
    message: string;
    timestamp: Date;
}

export interface DatabaseRecord {
    id: string;
    content: string;
    createdAt: Date;
    updatedAt: Date;
}