import express from 'express';
import { retrieveResponse } from '../services/retriever';
import { logChatMessage } from '../services/llm';

const router = express.Router();

// POST route to handle chat messages
router.post('/chat', async (req, res) => {
    const userMessage = req.body.message;

    try {
        // Retrieve response from the database or language model
        const response = await retrieveResponse(userMessage);
        
        // Log the chat message if necessary
        await logChatMessage(userMessage, response);

        res.json({ response });
    } catch (error) {
        console.error('Error handling chat message:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// GET route to fetch chat history (optional)
router.get('/chat/history', async (req, res) => {
    // Logic to fetch chat history can be implemented here
    res.json({ message: 'Chat history not implemented yet.' });
});

export default router;