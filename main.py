# Entari distıroyır
#   bu program sözlükte tane tane entry silmekten bıkanlar
#   için geliştirildi. tarayıcınızda hesabınızın açık olması ve kullanıcı adını girmeniz yeterli
#   webdriveda sorun yaşayabilirsiniz. satırı güncellemeniz gerek.giriş sayfasıyla açılabilirdi
#   fakat üşendiğim için ve proje için bir kaç saatlik hevesimi yitirdiğim için daha bir şeyler
#   eklemeyi düşünmüyorum. bu şekilde çalışıyor. 800 entry i sorunsuz şekilde sildi.
#   dockerize etmeye çalışabilirim.kod basit ve selenium kütüphanesini nasıl kullandığımı görebilirsiniz
#   herhangi bir hata ayıklama yada kontrol mekanizması yok. seleniumla ilgili hata verirse chrome web drive ını indirip
#   path e ekleyin.
#
# @version 1.0
# @johnny since   2020-10-06
# @author sabrey


import time
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/sabrey/AppData/Local/Google/Chrome/User Data') #kendi chrome user data pathiniz gelecek
driver = webdriver.Chrome(options=options)


def main():
    print("programı çalıştırmadan önce chrome tarayıcısında hesabınızın açık olması gerekiyor.")
    nick =input("kullanıcı adınız=").replace(' ', '-')
    driver.get("https://eksisozluk.com/biri/"+nick)
    time.sleep(3)
    asagi_in()
    entry_kaydet()
    print("entryler siliniyor...")
    entryleri_sil()


def entryleri_sil():
    elements = driver.find_elements_by_css_selector("[title*='diğer']")
    time.sleep(5)
    a = 0
    for e in elements:
        if a == 0:
            a += 1
            continue
        driver.execute_script("arguments[0].scrollIntoView();", e)
        driver.execute_script("arguments[0].click();", e)
        sil = driver.find_element_by_link_text("sil")
        driver.execute_script("arguments[0].click();", sil)
        time.sleep(2)
        kesin = driver.find_element_by_xpath("//*[contains(text(), 'kesin')]")
        driver.execute_script("arguments[0].click();", kesin)
        print("silindi..")
        time.sleep(60)


def entry_kaydet():
    f = open("silinen_entariler.txt", "w")
    icerikler = []
    basliklar = []
    time.sleep(5)
    for element in driver.find_elements_by_class_name("content"):
        icerikler.append(element.text)
    for element in driver.find_elements_by_xpath('.//span[@itemprop = "name"]'):
        basliklar.append(element.text)
    for i in range(len(basliklar)):
        f.write(basliklar[i])
        f.write(" : \n")
        f.write(icerikler[i + 1])
        f.write("\n \n ")
    f.close()
    print("entryler silinen_entariler.txt dosyasına kaydedildi. \n \n ")


def asagi_in():
    while True:
        elm = driver.find_element_by_class_name('load-more-entries')
        if "yok ki öyle bişey" in driver.page_source:
            break
        driver.execute_script("arguments[0].click();", elm)
    print("tüm entariler hazır gomutanım.")


if __name__ == "__main__":
    main()
