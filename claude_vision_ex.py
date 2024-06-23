import base64
from anthropic import Anthropic
from rich.console import Console
from rich.markdown import Markdown

client = Anthropic(
    api_key="Your-API-Key"
)

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        base_64_encoded_data = base64.b64encode(binary_data)
        base64_string = base_64_encoded_data.decode('utf-8')
        return base64_string

message = client.messages.create(
    max_tokens=2048,
    messages=[
        {
            "role": 'user',
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg",
                                             "data": get_base64_encoded_image(
                                                 "IMG_7435.jpeg")}},
                {"type": "text", "text": "사랑스러운 제자들이 준비한 담임선생님을 위한 케익이야. 케익에 어떤 문구가 적혀있는지 봐주고, 이 케익을 받은 사람이 몇 살인지 추측해볼래?"}
            ]
        }
    ],
    model="claude-3-5-sonnet-20240620",
)

response_content = message.content[0].text

console = Console()
md = Markdown(response_content)
console.print(md)