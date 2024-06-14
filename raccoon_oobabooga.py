import random
import requests

class RaccoonOobabooga:
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "host": ( "STRING", {
          "default": "http://127.0.0.1:5000",
        }),
        "prompt": ( "STRING", {
          "multiline": True,
          "default": "A beautiful girl is sitting on a bench in the park.".strip(),
        }),
        "character": ( "STRING", {
          "default": "Describer",
        }),        
      }
    }

  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("response",)
  FUNCTION = "oobabooga"
  CATEGORY = "Raccoon/Oobabooga"

  def oobabooga(self, host, prompt, character):
    url = "/v1/chat/completions"
    url = host + url

    headers = {
        "Content-Type": "application/json"
    }

    data = {
      "mode": "chat-instruct",
      "character": character,
      "messages": [
          {
            "role": "user",
            "content": prompt,
          }
      ],      
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    response.raise_for_status()  # Raise exception for non-2xx responses
    answer = response.json()["choices"][0]["message"]["content"]    

    return(answer, )
