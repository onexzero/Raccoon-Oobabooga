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
        "seed":        ("INT",   {"default": 0,   "min": 0, "max": 0xffffffffffffffff}),
        "max_tokens":  ("INT",   {"default": 200, "min": 0, "max": 0xffffffffffffffff}),
        "temperature": ("FLOAT", {"default": 1.0, "min": 0, "max": 0xffffffffffffffff}),
        "top_p":       ("FLOAT", {"default": 0.9, "min": 0, "max": 0xffffffffffffffff}),        
      }
    }

  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("STRING",)
  FUNCTION = "oobabooga"
  CATEGORY = "Raccoon/Oobabooga"

  def oobabooga(self, host, prompt, character,seed, max_tokens, temperature, top_p):
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
      "max_tokens":  max_tokens,
      "temperature": temperature,
      "top_p":       top_p,
      "seed":        seed,
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    response.raise_for_status()  # Raise exception for non-2xx responses
    answer = response.json()["choices"][0]["message"]["content"]    
    print("LLM RESP:",answer)
    return (answer,)
