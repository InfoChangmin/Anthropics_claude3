import os
from anthropic import Anthropic
# 보기좋게 가꾸기 위한 패키지. rich
from rich.console import Console
from rich.markdown import Markdown

client = Anthropic(
    api_key="Your-API-Key" # 이곳에 API KEY를 넣으세요! (https://console.anthropic.com/settings/keys)
)

message = client.messages.create(
    max_tokens=2048,
    messages=[
        {
            "role": "user",
            "content": "안녕 클로드야! 나는 울산의 정보교사 홍창민이라고해! 너랑 지금부터 너를 처음 사용하는 사람들을 위한 너의 기능을 소개하고 또 실제로 시연할거야! 관련해서 예상 질문을 10가지 정도 만들어주고 답할 수 있는 예시 코드나 답변도 함께 제공해줘.",
        }
    ],
    model="claude-3-5-sonnet-20240620",
)
response_content = message.content[0].text

console = Console()
md = Markdown(response_content)
console.print(md)