from  behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

@given('launch chrome broweser')
def launch_broweser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(20)

@when('open the goibibo browser')
def open_browser(context):
    context.driver.get("https://www.goibibo.com/bus/")
    context.driver.maximize_window()
    time.sleep(2)

@then('enter the arrival place "{arival}"')
def FROM(context,arival):
    context.driver.find_element_by_id('autosuggestBusSRPSrcHome').send_keys(arival)
    time.sleep(2)
    context.driver.find_element("xpath", '''(// section[@class ="AutoSuggeststyles__AutoSuggest-sc-aqwuwp-0 fTGPNO"]) // div[@ role='option'][1]''').click()
    time.sleep(2)

@then(u'enter the destination place "{destination}"')
def TO(context,destination):
    context.driver.find_element_by_id('autosuggestBusSRPDestHome').send_keys(destination)
    context.driver.find_element("xpath", '''(//section[@class="AutoSuggeststyles__AutoSuggest-sc-aqwuwp-0 fTGPNO"])//div[@role='option'][1]''').click()
    time.sleep(2)

@then(u'click on search')
def search(context):
    context.driver.find_element("xpath", "//button[text()='Search Bus']").click()
    time.sleep(2)

@then(u'apply filter1')
def apply_filter1(context):
    context.driver.find_element("xpath", '''(//span[@class='Checkboxstyles__Checkmark-sc-17an8c7-1 cXxQSq'])[1]''').click()
    time.sleep(2)

@then(u'apply filter2')
def apply_filter2(context):
    context.driver.find_element("xpath", '''(//div[@class='FiltersBlockstyles__BusTypeFilterTab-sc-v6hq3g-12 djZxHm'])[1]''').click()
    time.sleep(2)

@then(u'click on SELECT SEAT button')
def click_select_SEAT_buton(context):
    context.driver.find_element("xpath", '''(//span[@class='SrpActiveCardstyles__PayTxtSpan-sc-yk1110-31 klFZUT'])[1]''').click()
    time.sleep(2)

@then(u'select boarding point')
def boarding_place(context):
    context.driver.find_element("xpath", '''//div[@class='BoardingDropingBoxstyles__WrapperBox-sc-djxci-0 cUIdyJ']//label[2]''').click()
    time.sleep(2)

@then(u'select dropping point')
def dropping_place(context):
    context.driver.find_element("xpath", '''(//div[@class="BoardingDropingBoxstyles__WrapperBox-sc-djxci-0 cUIdyJ"])[2]//label[2]''').click()
    time.sleep(2)

@then(u'select your seat')
def select_seat(context):
    context.driver.find_element("xpath", '''(//div[@class="SeatWithTooltipstyles__BusSleeper-sc-dkrka-1 cmsovk"])[1]''').click()
    time.sleep(2)

@then(u'click on CONTINUE')
def procced(context):
    context.driver.find_element("xpath", '''//button[text()='CONTINUE']''').click()
    time.sleep(2)

@then(u'apply Insurence')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@class='InsuranceBlockstyles__CheckboxWrap-sc-jgljyo-7 UusRp']//label[2]").click()
    time.sleep(2)

@then(u'enter the passenger name')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@placeholder='Enter Full Name']").send_keys("Rushikesh")
    time.sleep(2)



@then(u'enter the passenger age')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@placeholder='Age']").send_keys("22")
    time.sleep(2)


@then(u'enter the passenger email')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@placeholder='Enter Email Address']").send_keys("rushi12@gmail.com")
    time.sleep(2)


@then(u'enter the passenger mobile')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@placeholder='Enter Mobile Number']").send_keys("7057456772")
    time.sleep(2)


@then(u'click on pay')
def step_impl(context):
    context.driver.find_element("xpath", "//button[@class='ReviewPagestyles__PayButton-sc-fmjc42-13 bYqmLn']").click()
    time.sleep(2)


