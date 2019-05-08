# must run in the current month
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Ie()
browser.get('http://XXXXXXX/ccccc/pppp/0000/00100.ccc')
try:
    # login start
    elemID = browser.find_element_by_id("txtID")
    elemPW = browser.find_element_by_id("txtlPSWORD")
    elemLogin = browser.find_element_by_id("btnLOGIN")
    elemID.send_keys('ccccc')
    elemPW.send_keys('ccccc')
    elemLogin.click()
    time.sleep(3)
    # login end

    # switch to tree menu
    browser.switch_to.frame("navigationTree")
    treeNode = "var q=document.getElementById('UltraWebTree1_1_1').children[3].click()"
    browser.execute_script(treeNode)
    time.sleep(1)

    # switch to edit menu
    browser.switch_to.default_content()
    browser.switch_to.frame("main")

    list = []
    for num in range(2, 6): # 33
        elemLine = browser.find_element_by_xpath(".//*[@id='wgList']/tbody/*[%s]" % (num))

        if elemLine is not None:
            attr = elemLine.get_attribute('style')
            if attr.find('lightgray') == -1:
                elemTime = browser.find_element_by_xpath(".//*[@id='wgList']/tbody/*[%s]/td" % (num))
                print('Found value <%s> in element !' % (elemTime.get_attribute("innerText")))
                list.append(elemTime.get_attribute("innerText"))

    # delete total
    del (list[-1])

    for dayNum in list:

        addWorkUrl = "http://XXXXXXX/ccccc/pppp/0000/00100.ccc?YM=201905&STAFFID=180703&WORK_DATE=%s" % (dayNum)

        browser.get(addWorkUrl)

        strID = "document.getElementById('SEL_CASE_ID').value = '201810-0501-003'"
        browser.execute_script(strID)
        strNM = "document.getElementById('SEL_CASE_NAME').value = '项目名称'"
        browser.execute_script(strNM)

        elemInput = browser.find_element_by_xpath(".//*[@id='wgList']/tbody/*[2]/*[3]/input")
        elemInput.clear()
        elemInput.send_keys("8")

        elemButton = browser.find_element_by_xpath(".//*[@id='btnInput']") #submit

        elemButton.send_keys(Keys.ENTER)
        time.sleep(2)
        alert = browser.switch_to.alert

        alert.dismiss()

    print("End!")

except:
    print('Was not able to find an element with that name.')
