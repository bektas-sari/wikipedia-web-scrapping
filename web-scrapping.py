import requests
from bs4 import BeautifulSoup   

# Rastgele wikipedia makalesi
url = "https://tr.wikipedia.org/wiki/%C4%B0stanbul"

#Taryıcı gibi görünmesi için User-agent ekliyoruz
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} 

# İstek yapılıyor
response = requests.get(url, headers=headers)

# İstek başarılı ise
if response.status_code == 200:
    # İçeriği alıyoruz
    html_icerigi = response.content
    # BeautifulSoup nesnesi oluşturuyoruz
    soup = BeautifulSoup(html_icerigi, "html.parser")
    # İçerikteki başlıkları alıyoruz
    basliklar = soup.find_all("h2")
    # Başlıkları yazdırıyoruz
    for baslik in basliklar:
        print(baslik.text)
else:
    print("İstek başarısız oldu. Hata kodu: ", response.status_code)


