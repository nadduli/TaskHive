# TaskHive

TaskHive is a modern task management system built with FastAPI, offering a robust and scalable solution for task organization and collaboration.

## Features

- 🚀 **Fast and Modern**: Built with FastAPI and Python 3.8+
- 🌐 **Internationalization**: Multi-language support (currently English and Spanish)
- 🔐 **Authentication**: Secure user authentication system
- 📝 **Task Management**: Create, update, and track tasks
- 🎯 **Status Tracking**: Monitor task progress with different status levels
- 🔄 **RESTful API**: Well-documented API endpoints
- 🐳 **Docker Support**: Easy deployment with Docker and docker-compose

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker and docker-compose (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/TaskHive.git
cd TaskHive
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

### Example Endpoints

- `GET /health`: Health check endpoint
- `GET /welcome`: Welcome message with i18n support

## Internationalization (i18n)

TaskHive supports multiple languages through its i18n system. Currently supported languages:
- English (en)
- Spanish (es)

To use different languages, set the `Accept-Language` header in your requests:

```bash
# For English
curl -H "Accept-Language: en" http://localhost:8000/welcome

# For Spanish
curl -H "Accept-Language: es" http://localhost:8000/welcome
```

### Adding New Languages

1. Create a new translation file in `app/translations/` (e.g., `fr.json` for French)
2. Follow the same JSON structure as existing translation files
3. The system will automatically detect and use the new language

## Project Structure

```
TaskHive/
├── app/
│   ├── api/           # API routes
│   ├── core/          # Core functionality
│   ├── database/      # Database models and config
│   ├── models/        # Data models
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # Business logic
│   ├── translations/  # i18n translation files
│   └── utils/         # Utility functions
├── tests/             # Test files
├── docker-compose.yml # Docker compose config
├── dockerfile        # Docker config
└── requirements.txt  # Python dependencies
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FastAPI framework
- SQLAlchemy
- Python-i18n