 NeuroAIR Smart Home Integration

![NeuroAIR Logo](https://via.placeholder.com/150x50?text=NeuroAIR)  
*Умная ароматизация вашего дома*

 📌 О проекте

NeuroAIR — это интеллектуальная система ароматизации, интегрируемая с популярными платформами умного дома. Проект позволяет:

- Управлять ароматизацией голосом через Яндекс.Алису, Google Assistant и другие платформы
- Автоматически адаптировать ароматы под эмоциональное состояние пользователя
- Создавать сложные сценарии взаимодействия с другими IoT-устройствами

 🌟 Основные возможности

- 🎤 Голосовое управление с поддержкой 50+ команд
- 😊 Эмоциональный анализ голоса в реальном времени
- 🏠 Глубокая интеграция с Яндекс.Алисой, Google Home, Home Assistant
- ⏱️ Автоматические сценарии (утренний, вечерний, для сна)
- 📊 Аналитика использования и персонализация ароматов

⚙️ Технологический стек

- Python 3.9+ (основной язык)
- Asyncio для асинхронной работы
- WebSockets для потоковой передачи аудио
- Pydantic для валидации данных
- SoundDevice/PyAudio для работы с микрофонами
- FastAPI (серверная часть)

🚀 Быстрый старт

Предварительные требования

- Python 3.9 или новее
- PortAudio (системная зависимость)
- Микрофон (для тестирования голосовых команд)

 Установка

bash
Клонирование репозитория
git clone https://github.com/yourrepo/neuroair-smarthome.git
cd neuroair-smarthome

 Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate    # Windows

 Установка зависимостей
pip install -r requirements.txt


Конфигурация

Создайте файл .env в корне проекта:

ini
 Базовые настройки
NEUROAIR_API_KEY=your_api_key
AUDIO_SERVER_URL=http://localhost:8000

 Настройки платформ
YANDEX_OAUTH_TOKEN=your_token
GOOGLE_ACTIONS_KEY=your_key


 Запуск

bash
# Основной сервис интеграции
python -m neuroair.main

 Тестовый клиент для проверки аудиообработки
python -m tests.audio_client_test


📚 Документация

Полная документация доступна в следующих разделах:

1. [Интеграция с платформами](docs/platforms.md)
2. [API Reference](docs/api.md)
3. [Разработка сценариев](docs/scenarios.md)
4. [Тестирование](docs/testing.md)

🛠 Интеграция с платформами

 Яндекс.Алиса
from neuroair.platforms.yandex import YandexAliceHandler

handler = YandexAliceHandler(config_path="config/yandex.yaml")

Google Home
from neuroair.platforms.google import GoogleHomeIntegration

google_home = GoogleHomeIntegration()
await google_home.sync_devices()

 Home Assistant

Добавьте в configuration.yaml:
neuroair:
  host: 192.168.1.100
  port: 8123
  emotional_analysis: true

 🤝 Как внести вклад

1. Форкните репозиторий
2. Создайте ветку для вашей фичи (`git checkout -b feature/amazing-feature`)
3. Сделайте коммит изменений (`git commit -m 'Add some amazing feature'`)
4. Запушьте в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

📞 Контакты

Разработчики: Полынкин Семен & Малашенко Никита
Email: semenpolynkin2898@gmail.com  
Telegram: @Saim000n & @k0l1tka


*© 2023 SIMINS Project. Все права защищены.*
