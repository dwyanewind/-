import requests
import json

api_key = '更换成你的api_key'
api_secret = '更换成你的api_secret'
assistant_id = "智能体ID"

# 全局变量保存 access_token 和 conversation_id
access_token = None
conversation_id = None


def get_access_token(api_key, api_secret):
    url = "https://chatglm.cn/chatglm/assistant-api/v1/get_token"
    data = {"api_key": api_key, "api_secret": api_secret}
    response = requests.post(url, json=data)
    token_info = response.json()
    return token_info['result']['access_token']


# 启动程序先获取token
access_token = get_access_token(api_key, api_secret)


def handle_response(data_dict):
    message = data_dict.get("message")
    if not message:
        return ""

    content = message.get("content")
    if not content:
        return ""

    response_type = content.get("type")
    if response_type == "text":
        return content.get("text", "")
    return ""


def send_message_streaming(assistant_id, access_token, prompt):
    global conversation_id  # 用于保持上下文连续

    url = "https://chatglm.cn/chatglm/assistant-api/v1/stream"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "assistant_id": assistant_id,
        "prompt": prompt,
        "conversation_id": conversation_id
    }

    last_length = 0
    with requests.post(url, json=data, headers=headers, stream=True) as response:
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data:'):
                        data_dict = json.loads(decoded_line[5:])
                        # ⚠ 每次更新 conversation_id
                        if data_dict.get("conversation_id"):
                            conversation_id = data_dict["conversation_id"]
                        content = handle_response(data_dict)
                        if content and len(content) > last_length:
                            new_content = content[last_length:]
                            yield new_content
                            last_length = len(content)
        else:
            yield f"[请求失败: {response.status_code} {response.text}]"
