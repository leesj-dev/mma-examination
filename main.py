from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

link = "https://mwpt.mma.go.kr/caisBMHS/index_mwps.jsp?menuNo=22223"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(link)
time.sleep(5)
driver.switch_to.frame(driver.find_element(By.ID, "main"))
driver.execute_script("gf_moveMeNyu_ID(22018)")
driver.execute_script("f_moveMWSCHwaMyeon_ID();")
time.sleep(1)
driver.switch_to.alert.accept()
driver.find_element(By.XPATH, "//*[@id='uimuja']").click()

# 본인인증은 직접 해야 함.
dummy = input("본인인증이 완료되었으면 아무 글자나 입력하세요: ")
driver.execute_script("f_moveMWSCHwaMyeon_ID();")
time.sleep(2)
driver.execute_script("f_moveBYPJGSBISTIJBGongSeokJH_P();")
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
select_month = driver.find_elements(
    By.XPATH, "//*[@id='contents']/div/form/table/tbody/tr/td[1]/select[2]/*"
)
for option in select_month:
    option_text = option.get_attribute("text")
    print(option_text[1] if option_text[0] == "0" else option_text, end=" ")

month = input("중 희망 월을 입력하세요: ")
if len(month) == 1:
    month = "0" + month
Select(
    driver.find_element(
        By.XPATH, "//*[@id='contents']/div/form/table/tbody/tr/td[1]/select[2]"
    )
).select_by_visible_text(month)

while True:
    driver.execute_script("f_moveBYPJGSBISTIJBGongSeokJH_P();")
    try:
        js = driver.find_element(
            By.XPATH, "/html/body/div/div/div/table/tbody/tr[1]"
        ).get_attribute("onclick")
        if js is not None:
            driver.execute_script(js)
            break
        else:
            time.sleep(2)
    except:
        time.sleep(2)

driver.switch_to.window(driver.window_handles[0])
driver.switch_to.frame(driver.find_element(By.ID, "main"))
time.sleep(1)
driver.execute_script("f_registMinWon_JS();")
driver.switch_to.alert.accept()

time.sleep(10000)
