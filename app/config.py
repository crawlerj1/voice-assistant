from pydantic_settings import BaseSettings, SettingsConfigDict




class VoiceAssisConfig(BaseSettings):

    @property
    def DB_URI(self):
        pass


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
                extra="ignore" 
    )
    

settings=VoiceAssisConfig()