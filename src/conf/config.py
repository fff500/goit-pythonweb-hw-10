class Config:
    DB_URL = "postgresql+asyncpg://postgres:567234@localhost:5432/contact_manager"
    JWT_SECRET = "your_jwt_secret"
    JWT_ALGORITHM = "HS256"
    JWT_EXPIRATION_SECONDS = 3600


config = Config
