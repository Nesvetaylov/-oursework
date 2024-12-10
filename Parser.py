import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


url = "https://browser-info.ru/"
#Получаем данные со страницы и записываем ответ
#.text для получения HTNL-кода страницы
response = requests.get(url, headers=header).text
soup = BeautifulSoup(response,'lxml')
block = soup.find('div', id="tool_padding")

check_js = block.find('div', id="javascript_check")
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'

#print(result_js)

#Check Flash
check_flash=block.find('div',id = "flash_version")
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'

#Chtck user.agent
check_user=block.find('div', id = "user_agent").text

print(result_js)
print(result_flash)
print(check_user)




#Открыть в виде html-файла

# with open("1.html", "w", encoding="utf-8") as file:
#     file.write(response)