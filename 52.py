import asyncio
from audio_processor.client import AudioClient, ProcessingSettings

class VoiceControlHandler:
    def init(self, neuroair_controller):
        self.client = AudioClient(base_url="http://audio-processor:8000")
        self.neuroair = neuroair_controller
        self.commands = {
            "включи аромат": self.neuroair.turn_on,
            "выключи аромат": self.neuroair.turn_off,
            "усиль аромат": lambda: self.neuroair.adjust_intensity(+1),
            "уменьши аромат": lambda: self.neuroair.adjust_intensity(-1)
        }
    
    async def process_command(self, audio_stream):
        async with self.client:
            settings = ProcessingSettings(
                mode="stt",
                format_output="json",
                transcription_settings={
                    "emotional": True,
                    "language": "ru"
                }
            )
            
            async for result in self.client.stream_audio(audio_stream, settings):
                text = result.get("text", "").lower()
                emotion = result.get("emotion", "neutral")
                
                # Обработка команд
                for cmd, action in self.commands.items():
                    if cmd in text:
                        await action()
                        # Адаптация аромата под эмоциональное состояние
                        await self._adjust_for_emotion(emotion)
                        return True
        return False
    
    async def _adjust_for_emotion(self, emotion):
        emotion_profiles = {
            "happy": {"intensity": 2, "scent": "citrus"},
            "sad": {"intensity": 1, "scent": "lavender"},
            "angry": {"intensity": 1, "scent": "mint"},
            "neutral": {"intensity": 1, "scent": "default"}
        }
        profile = emotion_profiles.get(emotion, emotion_profiles["neutral"])
        await self.neuroair.set_profile(**profile)