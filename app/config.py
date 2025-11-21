from pydantic_settings import BaseSettings, SettingsConfigDict




class VoiceAssisConfig(BaseSettings):
    POSTGRES_SERVER:str
    POSTGRES_PORT:str
    POSTGRES_USER:str
    POSTGRES_DB:str
    POSTGRES_PASSWORD:str
    GROQ_API_KEY:str
    LLM_MODEL_ID:str
    DEEPGRAM_API_KEY:str


    @property
    def DB_URI(self):
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
                extra="ignore" 
    )
    

settings=VoiceAssisConfig()