from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ : bool = load_dotenv(find_dotenv()) # read local .env file

client : OpenAI = OpenAI()

# API keys are stored in Google Colab's Secret Manager
OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')
FMP_API_KEY = userdata.get('FMP_API_KEY')

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["FMP_API_KEY"] = FMP_API_KEY

client = OpenAI()
