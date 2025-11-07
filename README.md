# NEURA - AI Voice Assistant

**NEURA** is an intelligent voice assistant built with LiveKit, Google Realtime AI, and memory persistence. It features dynamic tool integration, real-time voice processing, and personalized interactions through persistent memory.

## 🚀 Features

- **Real-time Voice Processing** with Google Realtime AI (Aoede voice)
- **Persistent Memory** using Mem0 for personalized conversations
- **Dynamic Tool Integration** via N8N MCP (Model Context Protocol)
- **Built-in Tools**: Weather, Web Search, Email
- **Noise Cancellation** with BVC (Background Voice Cancellation)
- **Memory-Aware Responses** for continuous context across sessions

## 🏗️ System Architecture

```
User Input → LiveKit Session → NEURA Assistant → Tools/APIs → Response
     ↓                              ↓
Memory Store ←── Mem0 Client ←── Context Manager
     ↓                              ↓
N8N Workflows ←── MCP Integration ←── Dynamic Tools
```

## 📋 Prerequisites

- Python 3.9+
- LiveKit account and credentials
- Google API key for Realtime AI
- Mem0 API key
- N8N instance (optional, for MCP tools)
- Email credentials (for email tool)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd NEURA
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   Create a `.env` file with the following:
   ```env
   # LiveKit Configuration
   LIVEKIT_URL=wss://your-livekit-url.livekit.cloud
   LIVEKIT_API_KEY=your_livekit_api_key
   LIVEKIT_API_SECRET=your_livekit_api_secret
   
   # AI Models
   GOOGLE_API_KEY=your_google_api_key
   
   # Memory System
   MEM0_API_KEY=your_mem0_api_key
   
   # MCP Integration (Optional)
   N8N_MCP_SERVER_URL=http://localhost:5678/mcp/your-workflow-id
   
   # Email Configuration (Optional)
   EMAIL_USER=your_email@example.com
   EMAIL_PASSWORD=your_email_password
   ```

## 🏃‍♂️ Quick Start

1. **Start the assistant**
   ```bash
   python agent.py
   ```

2. **Connect via LiveKit client**
   - Use any LiveKit-compatible client
   - Connect to your LiveKit room
   - Start voice conversation with NEURA

## 📁 Project Structure

```
NEURA/
├── agent.py              # Main agent implementation
├── prompts.py            # System prompts and instructions
├── tools.py              # Built-in tools (weather, search, email)
├── test_mem0.py          # Memory system testing
├── requirements.txt      # Python dependencies
├── .env                  # Environment configuration
└── mcp_client/           # MCP integration
    ├── __init__.py
    ├── server.py         # MCP server connection
    └── agent_tools.py    # MCP tools integration
```

## 🔧 Configuration

### LiveKit Setup
1. Create a LiveKit project at [LiveKit Cloud](https://cloud.livekit.io/)
2. Get your API credentials
3. Update `.env` with your LiveKit configuration

### Memory System (Mem0)
1. Sign up at [Mem0](https://mem0.ai/)
2. Get your API key
3. Update `MEM0_API_KEY` in `.env`

### N8N MCP Integration (Optional)
1. Set up N8N instance
2. Create MCP workflow
3. Update `N8N_MCP_SERVER_URL` with your workflow endpoint

## 🎯 Usage

### Basic Voice Interaction
```
User: "Hey NEURA, what's the weather like?"
NEURA: "Right away, Karthika! [Gets weather and responds]"
```

### Memory-Aware Conversations
```
User: "Remember I like morning coffee"
NEURA: "I'll remember that you like morning coffee, Karthika!"

[Later session]
User: "What do you know about my preferences?"
NEURA: "I remember you like morning coffee!"
```

### Tool Usage
- **Weather**: "What's the weather in New York?"
- **Search**: "Search for latest AI news"
- **Email**: "Send an email to john@example.com"

## 🧠 Memory System

NEURA uses Mem0 for persistent memory:
- **User ID**: "Karthika" (configurable in `agent.py`)
- **Memory Storage**: Automatic conversation context saving
- **Context Retrieval**: Memories loaded on session start
- **Memory Filtering**: Duplicate content prevention

## 🔨 Built-in Tools

### Weather Tool (`get_weather`)
- Provides current weather information
- Location-based queries
- Temperature, conditions, and forecasts

### Web Search Tool (`search_web`)
- Real-time web search capabilities
- Returns relevant search results
- Multiple search engines support

### Email Tool (`send_email`)
- Send emails via SMTP
- Configurable email credentials
- Rich text and attachments support

## 🌐 MCP Integration

NEURA supports dynamic tool loading via N8N MCP:
- **SSE Connection**: Real-time tool updates
- **Dynamic Registration**: Tools loaded from N8N workflows
- **Cache Support**: Improved performance with tool caching

## 🔍 Testing

Run memory system tests:
```bash
python test_mem0.py
```

## 📊 Performance Features

- **Real-time Processing**: Low-latency voice responses
- **Memory Efficiency**: Optimized context management
- **Tool Caching**: Fast tool execution
- **Noise Cancellation**: Clear audio processing

## 🛡️ Security

- **Environment Variables**: Secure credential storage
- **API Key Management**: Encrypted key handling
- **Memory Privacy**: User-specific memory isolation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Troubleshooting

### Common Issues

1. **LiveKit Connection Failed**
   - Check your LiveKit credentials
   - Verify network connectivity
   - Ensure WebSocket support

2. **Memory Not Working**
   - Verify Mem0 API key
   - Check user ID configuration
   - Test memory client connection

3. **Tools Not Loading**
   - Check API keys for external services
   - Verify N8N MCP server URL
   - Test individual tool functions

### Debug Mode
Enable debug logging in `agent.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📞 Support

For support and questions:
- Check the [Issues](https://github.com/your-repo/issues) page
- Review the documentation
- Contact the development team

---

**NEURA** - Making AI assistants more intelligent, one conversation at a time! 🤖✨
