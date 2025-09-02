import express from 'express';
import cors from 'cors';
import { connectToDatabase } from './db/index';
import chatRoutes from './routes/chat';

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Connect to the database
connectToDatabase();

// Routes
app.use('/api/chat', chatRoutes);

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});