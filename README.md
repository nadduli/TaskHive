# SkillBridge

SkillBridge is a dynamic platform that connects unemployed youth with micro-opportunities in their local communities while enabling small businesses to find affordable local talent. Built with FastAPI, it offers a scalable solution for bridging the employment gap and fostering community growth.

## Features

- 🤝 **Community Connection**: Match local talent with nearby opportunities
- 💼 **Micro-Opportunities**: Short-term, flexible work arrangements
- 🎯 **Skill Matching**: Smart matching system based on skills and requirements
- 📈 **Growth Tracking**: Monitor progress and skill development
- ⭐ **Rating System**: Build reputation through completed work
- 🔐 **Secure Platform**: Safe and verified user authentication
- 🌐 **Internationalization**: Multi-language support for diverse communities
- 📱 **Mobile Responsive**: Access opportunities on any device

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker and docker-compose (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SkillBridge.git
cd SkillBridge
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

#### Using Python directly:
```bash
python -m app.main
```

#### Using Docker:
```bash
docker-compose up --build
```

The application will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

### Core Endpoints

- `GET /opportunities`: Browse available opportunities
- `GET /skills`: List available skill categories
- `POST /matches`: Create new job matches
- `GET /profile`: User profile and history

## Internationalization (i18n)

SkillBridge supports multiple languages to serve diverse communities. Currently supported languages:
- English (en)
- Spanish (es)

To use different languages, set the `Accept-Language` header in your requests:

```bash
# For English
curl -H "Accept-Language: en" http://localhost:8000/welcome

# For Spanish
curl -H "Accept-Language: es" http://localhost:8000/welcome
```

## Project Structure

```
SkillBridge/
├── app/
│   ├── api/           # API routes
│   ├── core/          # Core functionality
│   ├── database/      # Database models and config
│   ├── models/        # Data models
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # Business logic
│   ├── matching/      # Matching algorithm
│   ├── translations/  # i18n translation files
│   └── utils/         # Utility functions
├── tests/             # Test files
├── docker-compose.yml # Docker compose config
├── dockerfile         # Docker config
└── requirements.txt   # Python dependencies
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Impact

SkillBridge aims to:
- Reduce youth unemployment in local communities
- Support small business growth through affordable talent
- Build professional experience for young workers
- Strengthen local economic ecosystems
- Create sustainable employment pathways