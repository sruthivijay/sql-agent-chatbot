import React, { useState } from 'react';
import Chat from '../components/Chat';

const Home: React.FC = () => {
    const [messages, setMessages] = useState<string[]>([]);
    const [input, setInput] = useState<string>('');

    const handleSendMessage = () => {
        if (input.trim()) {
            setMessages([...messages, input]);
            setInput('');
            // Here you would typically send the input to the server and get a response
        }
    };

    return (
        <div>
            <h1>Chatbot</h1>
            <Chat messages={messages} />
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                placeholder="Type your message..."
            />
            <button onClick={handleSendMessage}>Send</button>
        </div>
    );
};

export default Home;