import React, { useState } from 'react';

const Chat: React.FC = () => {
    const [messages, setMessages] = useState<{ user: string; bot: string }[]>([]);
    const [input, setInput] = useState('');

    const handleSendMessage = () => {
        if (input.trim()) {
            const newMessage = { user: input, bot: '...' }; // Placeholder for bot response
            setMessages([...messages, newMessage]);
            setInput('');

            // Here you would typically call your API to get the bot's response
            // For example:
            // fetch('/api/chat', { method: 'POST', body: JSON.stringify({ message: input }) })
            //     .then(response => response.json())
            //     .then(data => {
            //         setMessages(prev => [...prev, { user: input, bot: data.response }]);
            //     });
        }
    };

    return (
        <div>
            <div className="chat-window">
                {messages.map((msg, index) => (
                    <div key={index}>
                        <strong>You:</strong> {msg.user}
                        <br />
                        <strong>Bot:</strong> {msg.bot}
                        <br />
                    </div>
                ))}
            </div>
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

export default Chat;