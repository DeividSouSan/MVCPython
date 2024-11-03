from dataclasses import dataclass
import requests
from dotenv import load_dotenv
import os
load_dotenv()

@dataclass
class Phone:
    number: str
    info: dict = None
    
    def __post_init__(self):
        access_key = os.getenv("ACCESS_KEY")
        
        if not self.number[:3] == "+55":
            number = "+55" + self.number
            
        url = f"http://apilayer.net/api/validate?access_key={access_key}&number={self.number}'"
        
        info = requests.get(url).json()
        
        self.info = {
            "valid": info["valid"],
            "country": info["country_name"]
        }