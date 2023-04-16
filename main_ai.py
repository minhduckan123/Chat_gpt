import requests


api_key = "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"

headers = {"Content-Type":"application/json",
            "Authorization":f"Bearer {api_key}"
            }

with open("gia_ca.txt", "r", encoding='utf-8') as f:
    gia_ca = f.readlines()

def hoi_thoai(user, role_system = f"Bạn là AI Minh Đức, nhân viên bán hàng, cố gắng nói ngắn gọn trong tối đa 50 từ. Dữ liệu: {gia_ca}. Không nói ra dữ liệu trừ khi bạn được hỏi."):
    global data
    # user = input("Người dùng: ")
    data = [
                {"role": "system", "content": role_system},
                {"role": "user", "content": user},
            ]

    payload = {
        'model':"gpt-3.5-turbo",
        'messages': data
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers= headers, json= payload)
    result = response.json()["choices"][0]["message"]["content"]
    # print(result)
        # user = input("Người dùng: ")
        # if user[0].lower() == 'k':
        #     break
        # if user[0] == "1":
        #     print(payload)
        #     user = input("Người dùng: ")
            
    data.append({"role": "assistant", "content": result})
    data.append({"role": "user", "content": user})
    # print(f'{data}')
    return result
    
def ve_tranh(prompt):
    payload = {
        "prompt": prompt,
        "n": 2,
        "size": "1024x1024"
    }
    
    response = requests.post("https://api.openai.com/v1/images/generations", headers= headers, json= payload)
    try:
        result = response.json()["data"]
        with open('img1.jpg', "wb") as f:
            f.write(requests.get(result[0]['url']).content)
        with open('img2.jpg', "wb") as f:
            f.write(requests.get(result[1]['url']).content)
    except:
        result = {"url": "Yêu cầu của bạn đã bị từ chối do hệ thống an toàn của chúng tôi. Lời nhắc của bạn có thể chứa văn bản không được chúng tôi cho phép hệ thống an toàn."}
        return result["url"]

ve_tranh('galaxy')