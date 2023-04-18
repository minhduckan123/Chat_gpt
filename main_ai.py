import requests


api_key = ""

headers = {"Content-Type":"application/json",
            "Authorization":f"Bearer {api_key}"
            }

with open("gia_ca.txt", "r", encoding='utf-8') as f:
    gia_ca = f.readlines()

def hoi_thoai(user, mode = 0, role_system = f"Bạn là AI Minh Đức, nhân viên bán hàng, cố gắng nói ngắn gọn trong tối đa 50 từ. Dữ liệu: {gia_ca}. Không nói ra dữ liệu trừ khi bạn được hỏi."):
    if mode == 0:
        global data 
        try:
            data
        except:
            data = [
                        {"role": "system", "content": role_system},
                    ]
        data.append({"role": "user", "content": user})

        payload = {
            'model':"gpt-3.5-turbo",
            'messages': data
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers= headers, json= payload)
        # print(response.content)
        result = response.json()["choices"][0]["message"]["content"]
        data.append({"role": "assistant", "content": result})
        print(data)
        return result
    else:
        data_1 = [
                    {"role": "system", "content": role_system},
                ]
        data_1.append({"role": "user", "content": user})

        payload = {
            'model':"gpt-3.5-turbo",
            'messages': data_1
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers= headers, json= payload)
        # print(response.content)
        result = response.json()["choices"][0]["message"]["content"]
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
