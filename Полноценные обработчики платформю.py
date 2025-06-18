class YandexAliceHandler:
    """Полнофункциональный обработчик для Яндекс.Алисы"""
    
    def init(self, integration: NeuroAirSmartHomeIntegration):
        self.integration = integration
        
    async def handle_request(self, request: Dict) -> Dict:
        """Обрабатывает входящий запрос от Яндекс.Алисы"""
        response = {
            'version': request['version'],
            'session': request['session'],
            'response': {
                'end_session': False
            }
        }
        
        try:
            # Получаем аудио из запроса
            audio_stream = self._get_audio_stream(request)
            
            # Обрабатываем команду
            processed = await self.integration.process_voice_command(audio_stream)
            
            if processed:
                response['response']['text'] = "Выполняю вашу команду"
            else:
                response['response']['text'] = "Не поняла вашу команду"
                
        except Exception as e:
            logger.error(f"Yandex Alice error: {e}")
            response['response']['text'] = "Произошла ошибка"
            
        return response
        
    def _get_audio_stream(self, request: Dict) -> AsyncGenerator[bytes, None]:
        """Извлекает аудиопоток из запроса Алисы"""
        # Здесь будет реальная реализация получения аудио
        async def dummy_stream():
            yield b''
            
        return dummy_stream()

class GoogleHomeHandler:
    """Расширенный обработчик для Google Home/Assistant"""
    
    def init(self, integration: NeuroAirSmartHomeIntegration):
        self.integration = integration
        self.device_map = {}
        
    async def sync_devices(self):
        """Синхронизирует устройства с Google Home"""
        self.device_map = {
            'neuroair': {
                'id': 'neuroair-1',
                'type': 'AIR_FRESHENER',
                'traits': [
                    'OnOff', 'StartStop', 'Toggles', 
                    'Modes', 'FanSpeed', 'SensorState'
                ],
                'name': {
                    'name': 'NeuroAIR Ароматизатор'
                },
                'willReportState': True,
                'roomHint': 'Living Room',
                'deviceInfo': {
                    'manufacturer': 'NeuroAIR',
                    'model': 'NA-2023',
                    'hwVersion': '1.0',
                    'swVersion': '1.2.5'
                }
            }
        }
        
    async def execute_command(self, command: Dict) -> Dict:
        """Выполняет команду от Google Home"""
        response = {'status': 'SUCCESS', 'states': {}}
        
        try:
            if 'audio' in command:
                # Обработка голосовой команды
                audio_stream = self._get_audio_stream(command['audio'])
                await self.integration.process_voice_command(audio_stream)
            else:
                # Обработка стандартной команды
                await self._handle_standard_command(command)
                
            # Обновляем состояние устройства
            response['states'] = self._get_current_state()
            
        except Exception as e:
            logger.error(f"Google Home error: {e}")
            response['status'] = 'ERROR'
            
        return response
        
    def _get_audio_stream(self, audio_data: Dict) -> AsyncGenerator[bytes, None]:
        """Подготовка аудиопотока для Google Home"""
        # Реальная реализация будет декодировать аудио от Google
        async def dummy_stream():
            yield b''
            
        return dummy_stream()
    class HomeAssistantHandler:
    """Комплексный обработчик для Home Assistant"""
    
    def init(self, integration: NeuroAirSmartHomeIntegration):
        self.integration = integration
        self._setup_entities()
        
    def _setup_entities(self):
        """Настраивает сущности для Home Assistant"""
        self.entities = {
            'switch.neuroair': {
                'name': 'NeuroAIR',
                'state': 'off',
                'attributes': {
                    'intensity': 0,
                    'current_profile': None,
                    'available_profiles': list(self.integration.scent_profiles.keys()),
                    'emotion_status': 'neutral'
                }
            },
            'sensor.neuroair_emotion': {
                'name': 'NeuroAIR Emotion',
                'state': 'neutral',
                'attributes': {
                    'confidence': 0,
                    'last_updated': None
                }
            }
        }
        
    async def handle_service_call(self, service: str, data: Dict) -> Dict:
        """Обрабатывает вызов сервиса Home Assistant"""
        response = {'success': True}
        
        try:
            if service == 'turn_on':
                await self.integration.turn_on()
            elif service == 'turn_off':
                await self.integration.turn_off()
            elif service == 'set_profile':
                await self._handle_set_profile(data)
            elif service == 'process_audio':
                await self._handle_audio_processing(data)
                
            self._update_entity_states()
            
        except Exception as e:
            logger.error(f"Home Assistant error: {e}")
            response['success'] = False
            
        return response
        
    async def _handle_set_profile(self, data: Dict):
        """Обрабатывает установку профиля"""
        profile = data.get('profile')
        intensity = data.get('intensity')
        
        if profile not in self.integration.scent_profiles:
            raise ValueError(f"Invalid profile: {profile}")
            
        await self.integration.set_profile(profile, intensity)
        
    async def _handle_audio_processing(self, data: Dict):
        """Обрабатывает аудио из Home Assistant"""
        audio_stream = self._get_audio_stream(data)
        await self.integration.process_voice_command(audio_stream)
        
    def _get_audio_stream(self, data: Dict) -> AsyncGenerator[bytes, None]:
        """Подготавливает аудиопоток"""
        # Реальная реализация будет работать с аудио от Home Assistant
        async def dummy_stream():
            yield b''
            
        return dummy_stream()