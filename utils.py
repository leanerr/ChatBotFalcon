from dotenv import load_dotenv
import os

def load_env_variables():
    load_dotenv()
    return os.getenv('API_KEY')
