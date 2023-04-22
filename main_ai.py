# Đoạn mã sử dụng thư viện "requests" để gửi các yêu cầu HTTP đến API của OpenAI để tương tác với mô hình GPT-3.
import requests # nhập thư viện requests


api_key = "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" # đặt khóa api chat gpt

headers = {"Content-Type":"application/json",
            "Authorization":f"Bearer {api_key}"
            } 
# Biến "headers" chứa thông tin đầu mối gửi yêu cầu, bao gồm kiểu nội dung là "application/json" và mã xác thực dựa trên khóa API.

with open("gia_ca.txt", "r", encoding='utf-8') as f: 
    gia_ca = f.readlines()
# Dòng này mở tệp "gia_ca.txt" với chế độ đọc ("r") và mã hóa UTF-8 (encoding='utf-8'), sau đó đọc tất cả các dòng trong tệp và lưu vào biến gia_ca dưới dạng một danh sách các chuỗi.

def hoi_thoai(user, mode = 0, role_system = f"Bạn là AI Minh Đức, nhân viên bán hàng, cố gắng nói ngắn gọn trong tối đa 50 từ. Dữ liệu: {gia_ca}. Không nói ra dữ liệu trừ khi bạn được hỏi."):
# Hàm "hoi_thoai" được định nghĩa để thực hiện cuộc hội thoại giữa người dùng và mô hình GPT-3. Đầu vào của hàm gồm "user" (nội dung người dùng nhập vào) và các đối số "mode" và "role_system" (có giá trị mặc định là 0 và một chuỗi dùng để mô tả vai trò của hệ thống trong cuộc hội thoại). Hàm này dùng để gửi yêu cầu POST đến API của OpenAI để hoàn thành câu hỏi dựa trên dữ liệu đầu vào và trả về câu trả lời của trợ lý ảo GPT-3.
    if mode == 0:
        global data 
        # Dòng này khai báo biến data là một biến toàn cục.
        try:
            data
        except:
            data = [
                        {"role": "system", "content": role_system},
                    ]
        # try-except là câu lệnh xử lý lỗi. Nếu data có tồn tại thì câu lệnh sẽ bỏ qua except nếu data không tồn tại thì sẽ chạy câu lệnh except.
        data.append({"role": "user", "content": user})
        #Dòng này thêm một đối tượng từ điển vào danh sách data, với khóa "role" là "user" và giá trị "content" là giá trị của biến user.
        payload = {
            'model':"gpt-3.5-turbo",
            'messages': data
        }
        # payload là thư viện chứa "model" là loại botchat "gpt-3.5-turbo", "message" là thư viện "data" chứa dữ liệu của cuộc hội thoại
        response = requests.post("https://api.openai.com/v1/chat/completions", headers= headers, json= payload)
        # Hàm gửi yêu cầu POST đến API của OpenAI với payload được tạo ra, sau đó lấy câu trả lời từ phản hồi của API và trả về nội dung của câu trả lời của mô hình GPT-3 dưới dạng một chuỗi ký tự.
        result = response.json()["choices"][0]["message"]["content"]
        # phân tích nội dung của câu trả lời của mô hình GPT-3 dưới dạng một chuỗi ký tự lấy ra phần trả lời tin nhắn.
        data.append({"role": "assistant", "content": result})
        #Dòng này thêm một đối tượng từ điển vào danh sách data, với khóa "role" là "assistant" và giá trị "content" là giá trị của biến result.
        print(data)
        return result
        # hàm trả về biến result 
    else:
        # là một phiên bản khác của mode 1 đơn giản hơn với không có thư viện data để lưu dữ liệu chat. Mục đích để phục vụ cho hàm ve_tranh().
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
# Hàm "ve_tranh" được định nghĩa để tạo ra hai hình ảnh được sinh ra bởi mô hình GPT-3 dựa trên một lời nhắc (prompt) được nhập vào. Hàm này cũng sử dụng API của OpenAI để gửi yêu cầu POST và nhận về các đường dẫn URL của hai hình ảnh được sinh ra, sau đó lưu trữ chúng vào hai tệp ảnh định dạng JPEG. Nếu yêu cầu bị từ chối bởi hệ thống an toàn của OpenAI, hàm sẽ trả về một thông báo lỗi.
# Hàm nhận vào một đoạn "prompt" làm đầu vào, được truyền vào thông qua tham số "prompt".
    payload = {
        "prompt": prompt,
        "n": 2,
        "size": "1024x1024"
    }
    # Hàm tạo một payload chứa thông tin về "prompt", số lượng tranh cần tạo ("n") và kích thước của tranh ("size").
    response = requests.post("https://api.openai.com/v1/images/generations", headers= headers, json= payload)
    # Hàm gọi API của OpenAI với endpoint là "https://api.openai.com/v1/images/generations", và truyền payload vào trong request.
    try:
        result = response.json()["data"]
        with open('img1.jpg', "wb") as f:
            f.write(requests.get(result[0]['url']).content)
        with open('img2.jpg', "wb") as f:
            f.write(requests.get(result[1]['url']).content)
    # Sau đó, hàm xử lý kết quả trả về từ API, lưu lại hai bức tranh vào hai file ảnh "img1.jpg" và "img2.jpg" bằng cách ghi dữ liệu nhận được từ response của API vào hai file này.
    except:
        result = {"url": "Yêu cầu của bạn đã bị từ chối do hệ thống an toàn của chúng tôi. Lời nhắc của bạn có thể chứa văn bản không được chúng tôi cho phép hệ thống an toàn."}
        return result["url"]
    # Nếu không có kết quả trả về từ API, hàm sẽ trả về một thông báo lỗi "Yêu cầu của bạn đã bị từ chối do hệ thống an toàn của chúng tôi. Lời nhắc của bạn có thể chứa văn bản không được chúng tôi cho phép hệ thống an toàn."
