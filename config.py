from pydantic import BaseModel
import os


class Settings(BaseModel):
    APP_NAME: str = os.environ.get("APP_NAME", "demo-app")
    APP_VERSION: str = os.environ.get("APP_VERSION", "0.1.0")
    HOST: str = os.environ.get("HOST", "0.0.0.0")
    PORT: int = os.environ.get("PORT", 8000)
    AUTHOR: str = os.environ.get("AUTHOR", "nobody")
    EMAIL: str = os.environ.get("EMAIL", "nobody@nowhere.com")
    URL: str = os.environ.get("URL", "http://missing.com")
    DESCRIPTION: str = os.environ.get("DESCRIPTION", "demo app description")
    CONTACT: dict = {
        "name": AUTHOR,
        "url": URL,
        "email": EMAIL
    }
    
settings = Settings()