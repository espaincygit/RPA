# must run in the current month
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

projectName = "研发(10月-3月)"
worktimeURL = "http://xx.xxx.xx.xx/kkk&WORK_DATE=%s"
browser = webdriver.Ie()
browser.get('http://xxx.xxx.xxx.xxx/sdldls')
try:
    # login start
    elemID = browser.find_element_by_id("txtID")
    elemPW = browser.find_element_by_id("txtlPSWORD")
    elemLogin = browser.find_element_by_id("btnLOGIN")
    elemID.send_keys('cccc')
    elemPW.send_keys('cccc')
    elemLogin.click()
    time.sleep(3)
    # login end

    # switch to tree menu
    browser.switch_to.frame("navigationTree")
    treeNodeStr = "var q=document.getElementById('UltraWebTree1_1_1').children[3].click()"
    browser.execute_script(treeNodeStr)
    time.sleep(1)

    # switch to edit menu
    browser.switch_to.default_content()
    browser.switch_to.frame("main")

    list = []
    for num in range(2, 6): #34

        elemLine = browser.find_element_by_xpath(".//*[@id='wgList']/tbody/*[%s]" % (num))
        # collect all work days
        if elemLine is not None:
            attr = elemLine.get_attribute('style')
            if attr.find('lightgray') == -1:
                elemTime = browser.find_element_by_xpath(".//*[@id='wgList']/tbody/*[%s]/td" % (num))
                print('Found value <%s> in element !' % (elemTime.get_attribute("innerText")))
                list.append(elemTime.get_attribute("innerText"))

    # delete last total line
    del (list[-1])

    # fill work time start
    for dayNum in list:
        # open work time window
        addWorkUrl = worktimeURL % (dayNum)
        browser.get(addWorkUrl)

        # input 8 hours
        elemInput = browser.find_element_by_xpath(".//*[@id='wgList']/tbody/*[2]/*[3]/input")
        elemInput.clear()
        elemInput.send_keys("8")

        # open search window
        elemButton = browser.find_element_by_xpath(".//*[@id='wgList']/tbody/*[2]/*[2]/*[2]") #submit
        elemButton.click()
        time.sleep(1)

        # switch to new dialog
        alert = browser.switch_to.alert
        time.sleep(1)
        hd = browser.window_handles
        print(hd)
        browser.switch_to.window(hd[1])
        print(browser.title)
        time.sleep(1)
        # input project name
        elemInput = browser.find_element_by_xpath(".//*[@id='txtName']")
        elemInput.send_keys(projectName)
        # do search
        elemInput = browser.find_element_by_xpath(".//*[@id='btnSch']")
        elemInput.click()
        time.sleep(2)

        # select the project
        elemButton = browser.find_element_by_xpath(".//*[@id='wgList']/tbody/*[2]") #submit
        elemButton.click()

        # click the close button
        elemInput = browser.find_element_by_xpath(".//*[@id='btnSel']")
        elemInput.click()
        time.sleep(2)

        # switch to original window
        hd = browser.window_handles
        browser.switch_to.window(hd[0])

        # click save button
        elemButton = browser.find_element_by_xpath(".//*[@id='btnInput']") #submit
        elemButton.click()
        time.sleep(1)
        alert = browser.switch_to.alert
        alert.dismiss()


    print("End!")

except:
    print('Exception happened.')
