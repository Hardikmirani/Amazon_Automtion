from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("C:/Users/Hardik/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://www.amazon.in/ap/signin?_encoding=UTF8&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1")

driver.find_element_by_id("ap_email").send_keys("************")
driver.find_element_by_id("continue").click()

driver.find_element_by_id("ap_password").send_keys("**********")
driver.find_element_by_id("signInSubmit").click()

driver.find_element_by_id("twotabsearchtextbox").send_keys("smart watch")

driver.find_element_by_id("nav-search-submit-button").click()

driver.find_element_by_xpath("//*[@id='search']/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a").click()

print(driver.current_url)
driver.switch_to.window(driver.window_handles[1])

driver.find_element_by_id("submit.buy-now").click()


print(driver.current_url)


driver.find_element_by_xpath("//input[@value='instrumentId=0h_PE_CUS_18b1c868-2e63-40e2-8b24-414fe05d88c8%2FCash&isExpired=false&paymentMethod=COD&tfxEligible=false']").click()


driver.find_element_by_name("ppw-widgetEvent:SetPaymentPlanSelectContinueEvent").click()


driver.find_element_by_name("placeYourOrder1").click()






























