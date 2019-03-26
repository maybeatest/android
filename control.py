from appium.webdriver.common.touch_action import TouchAction
from collections import Mapping
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import *
from Pages import *

class Setup():
    def Boot_page(driver):
        print('10086初始化开始')
        sleep(1)
        Swipes.left(driver)
        Swipes.left(driver)
        Swipes.left(driver)
        Allow_button(driver)
        Allow_button(driver)
        Allow_button(driver)
        print('启动页正常')
        print('10086初始化结束')

class Login():
    def Free_login(driver):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", temp)
        sleep(5)
        print('免登录开始')
        Free_login(driver)
        sleep(3)
        print('登录成功')

    def Password_login(driver):
        sleep(5)
        print('服务密码登录开始')
        Password_login(driver,user_data['username'],user_data['password'])
        sleep(3)
        print('登录成功')

    def Boot_Password_login(driver):
        '''
        引导登录-服务密码
        :param driver:
        :return:
        '''

        try:
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/switch_password'))
            )
            driver.find_element_by_id('com.kingpoint.gmcchh:id/switch_password').click()
            sleep(1)

            try:
                # 非初次登录，有清除按钮
                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/iv_clear'))
                )
                # 点击清除按钮
                driver.find_element_by_id('com.kingpoint.gmcchh:id/iv_clear').click()
                sleep(1)

            except:
                # 初次登录，没有清除按钮
                print('初次登录')

            driver.find_element_by_id('com.kingpoint.gmcchh:id/edit_number').send_keys(user_data['username'])
            driver.find_element_by_id('com.kingpoint.gmcchh:id/edit_service_password').click()
            sleep(1)
            driver.find_element_by_id('com.kingpoint.gmcchh:id/edit_service_password').send_keys(user_data['password'])
            driver.find_element_by_id('com.kingpoint.gmcchh:id/loginBtn').click()
            sleep(1)
            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/loginBtn'))
                )
                driver.find_element_by_id('com.kingpoint.gmcchh:id/loginBtn').click()
            except:
                print('引导登录-服务密码登录成功')
        except:
            print('当前客户端已登录')

class Swipes():
    def up(driver):
        '''
        上划
        :param driver:
        :return:
        '''
        def getSize():
            x = driver.get_window_size()['width']
            y = driver.get_window_size()['height']
            return (x, y)

        l = getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        driver.swipe(x1, y1, x1, y2)

    def down(driver):
        '''
        下拉刷新
        :param driver:
        :return:
        '''
        sleep(6)
        # driver.implicitly_wait(30)
        print('下拉刷新数据')
        def getSize():
            x = driver.get_window_size()['width']
            y = driver.get_window_size()['height']
            return (x, y)

        l = getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        driver.swipe(x1, y1, x1, y2)
        sleep(1)

    def left(driver):
        '''
        向左划
        :param driver:
        :return:
        '''
        def getSize():
            x = driver.get_window_size()['width']
            y = driver.get_window_size()['height']
            return (x, y)

        l = getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        driver.swipe(x1, y1, x2, y1)
        driver.find_element_by_id("com.kingpoint.gmcchh:id/ivHomePageToolbarIcon").click()
        sleep(0.5)

    def right(driver):
        '''
        向右划
        :param driver:
        :return:
        '''
        def getSize():
            x = driver.get_window_size()['width']
            y = driver.get_window_size()['height']
            return (x, y)

        l = getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        driver.swipe(x1, y1, x2, y1)

def Allow_button(driver):
    '''
    允许权限
    :param driver:
    :return:
    '''
    sleep(1)
    driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

def Free_login(driver):
    '''
    免登陆
    :param driver:
    :return:
    '''
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/tv_right'))
        )
        driver.find_element_by_id('com.kingpoint.gmcchh:id/tv_right').click()
        driver.implicitly_wait(30)
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        sleep(1)
        print('登陆成功')

        try:

            paths= "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView"

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, paths))
            )
            driver.find_element_by_xpath(paths).click()
            print('关闭智能短信弹框')
        except:
            print('没有智能短信弹框')

    except:
        print('没有找到免登录框')

def Password_login(driver,user_data,password):
    '''
    服务免密登录
    :param driver:
    :param user_data:
    :param password:
    :return:
    '''
    try:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/rlHomeUnLogin'))
        )
        print('开始登陆')
        driver.find_element_by_id('com.kingpoint.gmcchh:id/rlHomeUnLogin').click()
        driver.find_element_by_id('com.kingpoint.gmcchh:id/switch_password').click()

        try:
            #初次登录
            driver.find_element_by_id('com.kingpoint.gmcchh:id/edit_number').click()
            sleep(1)
            driver.find_element_by_id('com.kingpoint.gmcchh:id/edit_number').send_keys(user_data)
            driver.find_element_by_id('com.kingpoint.gmcchh:id/edit_service_password').click()
            sleep(1)
            driver.find_element_by_id('com.kingpoint.gmcchh:id/edit_service_password').send_keys(password)
            driver.find_element_by_id('com.kingpoint.gmcchh:id/loginBtn').click()
            print('服务免密登录成功')
            sleep(3)
            try:
                #需要获取权限
                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button'))
                )
                Allow_button(driver)
                sleep(3)
            except:
                print('不需要获取权限')
        except:
            #非初次登录
            driver.find_element_by_id('com.kingpoint.gmcchh:id/switch_password').click()
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/iv_clear'))
            )
            driver.find_element_by_id('com.kingpoint.gmcchh:id/iv_clear').click()
            sleep(1)
            driver.find_element_by_id('com.kingpoint.gmcchh:id/edit_number').send_keys(user_data)
            sleep(1)
            driver.find_element_by_id('com.kingpoint.gmcchh:id/edit_service_password').click()
            driver.find_element_by_id('com.kingpoint.gmcchh:id/edit_service_password').send_keys(password)
            sleep(1)
            driver.find_element_by_id('com.kingpoint.gmcchh:id/loginBtn').click()
            try:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/loginBtn'))
                )
                driver.find_element_by_id('com.kingpoint.gmcchh:id/loginBtn').click()
            except:
                print('服务免密登录成功')
    except:
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/rlHomeUnLogin'))
        )
        print('没有登录成功')

def Business_select(driver,name):
    '''
    业务选择
    :param driver:
    :param name:
    :return:
    '''
    try:
        # 业务选择
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/ivBusinessToolbarIcon'))
        )
        driver.find_element_by_id('com.kingpoint.gmcchh:id/ivBusinessToolbarIcon').click()

        # 业务办理中第五个列表：常用业务
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.GridView/android.widget.LinearLayout[5]/android.widget.TextView").click()
        sleep(1)
        Swipes.up(driver)
        Swipes.up(driver)
        sleep(1)

        names = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.TextView[1]").text
        print(names)

        if names == name:

            # 当前列表第3条数据
            driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.TextView[1]").click()
        else:
            print('没有找到:',name)
    except:
        print('没有进入:',name,'详情')

def Business_management(driver):
    '''
    退订、办理
    :param driver:
    :return:
    '''
    try:
        # 点击退订按钮
        WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/tv_cancel'))
        )
        driver.find_element_by_id('com.kingpoint.gmcchh:id/tv_cancel').click()
        try:
            # 退订二次确认
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'android.widget.LinearLayout'))
            )
            driver.implicitly_wait(30)
            # 判断按钮
            if  '确定' == driver.find_element_by_id('com.kingpoint.gmcchh:id/tv_confirm').get_attribute('text') :
                driver.find_element_by_id('com.kingpoint.gmcchh:id/tv_confirm').click()
            else:
                print('没有确定按钮')
            try:
                # 退订成功
                WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'android.widget.LinearLayout'))
                )
                driver.find_element_by_id('com.kingpoint.gmcchh:id/tv_middle').click()
                driver.implicitly_wait(30)
            except:
                print('没有退订成功')
        except:
            print('没有二次弹框')
    except:
        # 点击立即办理按钮
        print('没有退订按钮')
        driver.find_element_by_id('com.kingpoint.gmcchh:id/tv_handles').click()
        try:
            # 办理二次确认
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'android.widget.LinearLayout'))
            )
            driver.implicitly_wait(30)
            # 判断按钮
            if '确定' == driver.find_element_by_id('com.kingpoint.gmcchh:id/tv_confirm').get_attribute('text'):
                driver.find_element_by_id('com.kingpoint.gmcchh:id/tv_confirm').click()
            else:
                print('没有确定按钮')
            try:
                # 退订成功
                WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'android.widget.LinearLayout'))
                )
                driver.find_element_by_id('com.kingpoint.gmcchh:id/tv_middle').click()
                driver.implicitly_wait(30)
            except:
                print('没有退订成功')
        except:
            print('没有办理成功')

def Home_Function_Ergodic(driver):
    '''
    遍历首页宫格内容
    :param driver:
    :return:
    '''

    SuperClassName = driver.find_element_by_id(HomePage_Functions['Id'])
    RelativeLayouts = SuperClassName.find_elements_by_class_name(HomePage_Functions['RelativeLayout'])
    print('首页共有',len(RelativeLayouts),'个RelativeLayout控件。')

    Fun_name = []
    for i in range(0,len(RelativeLayouts)):
        # 遍历首页当前屏幕内宫格内容
        texts = RelativeLayouts[i].find_element_by_class_name('android.widget.TextView').text
        Fun_name.append(texts)
        # print('宫格名称',i+1,':', RelativeLayouts[i].find_element_by_class_name('android.widget.TextView').text)
    print('宫格内容有：',Fun_name)

def Home_Function_Select(driver,Fun_name):
    '''
    遍历并选择功能
    :param driver:
    :param Fun_name:
    :return:
    '''

    SuperClassName = driver.find_element_by_id(HomePage_Functions['Id'])
    print(SuperClassName)
    RelativeLayouts = SuperClassName.find_elements_by_class_name(HomePage_Functions['RelativeLayout'])


    for i in range(0,len(RelativeLayouts)):
        texts = RelativeLayouts[i].find_element_by_class_name('android.widget.TextView').text
        sleep(0.1)
        if texts == Fun_name:
            sleep(0.1)
            RelativeLayouts[i].find_element_by_class_name('android.widget.TextView').click()
            break
        driver.implicitly_wait(30)
    try:
        # 未登录
        Login.Boot_Password_login(driver)
    except:
        # 已登录
        print('当前用户已登录成功，无需引导登录。')

def Package_Allowance_Ergodic(driver):
    '''
    遍历套餐余量内容
    :param driver:
    :return:
    '''
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, Package_Allowance['Id']))
    )
    driver.implicitly_wait(30)
    # 一级标题名
    SuperClassName = driver.find_elements_by_id('com.kingpoint.gmcchh:id/tv_packageGroupTitle')
    # 未办理提示语
    Not_handled = driver.find_elements_by_id('com.kingpoint.gmcchh:id/tv_packageGroupUseNoOrder')
    # 已用提示
    used = driver.find_elements_by_id('com.kingpoint.gmcchh:id/tv_packageGroupUseAndTotal')

    print('一级标题名',len(SuperClassName),'个')
    print('未办理提示语',len(Not_handled),'个')
    print('已用提示',len(used),'个')
    print('--------------------------')

    for i in range(0,len(SuperClassName)):
        print('一级标题名:',SuperClassName[i].text)
    print('--------------------------')
    for i in range(0,len(Not_handled)):
        print('未办理提示语:',Not_handled[i].text)
    print('--------------------------')
    for i in range(0,len(used)):
        print('已用提示:',used[i].text)
    print('--------------------------')

def Package_Allowance_Jump(driver,fun_text):
    '''
    遍历套餐余量内容，并根据fun_text点击跳转
    :param driver:
    :param fun_text:
    :return:
    '''
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, Package_Allowance['Id']))
    )
    driver.implicitly_wait(30)

    Not_handled = driver.find_elements_by_id('com.kingpoint.gmcchh:id/tv_packageGroupUseNoOrder')

    print('--------------------------')
    for i in range(0,len(Not_handled)):
        # print('i =',i)
        print('未办理提示语:',Not_handled[i].text)

        if Not_handled[i].text.find(fun_text) != -1:
            # print(Not_handled[i].text.find(fun_text))
            Not_handled[i].click()
        # else:
        #     print('没有找到包含',fun_text,'的文字信息')
    print('--------------------------')


def Package_Allowance(driver):
    '''
    进入套餐余量，查看并点击短信未办理提示语。
    :return:none
    '''
    sleep(3)
    # Swipes.down(driver)
    Home_Function_Select(driver, '套餐余量')
    Package_Allowance_Jump(driver, '短信')

def Businesstype_Select(driver,Type_name):
    '''
    遍历并选择功能
    :param driver:
    :param Fun_name:
    :return:
    '''

    try:
        # 业务选择
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'com.kingpoint.gmcchh:id/ivBusinessToolbarIcon'))
        )
        driver.find_element_by_id('com.kingpoint.gmcchh:id/ivBusinessToolbarIcon').click()
    except:
        print("未选中业务办理栏目")

    SuperClassName = driver.find_element_by_id(BUsiness_Type['Id'])
    print(SuperClassName)
    RelativeLayouts = SuperClassName.find_elements_by_class_name(BUsiness_Type['LinearLayout'])


    for i in range(0,len(RelativeLayouts)):
        texts = RelativeLayouts[i].find_element_by_class_name(BUsiness_Type['TextView']).text
        sleep(0.1)
        if texts == Type_name:
            sleep(0.1)
            RelativeLayouts[i].find_element_by_class_name(BUsiness_Type['TextView']).click()
            break
        driver.implicitly_wait(30)
    try:
        # 未登录
        Login.Boot_Password_login(driver)
    except:
        # 已登录
        print('当前用户已登录成功，无需引导登录。')


def Business_Select(driver,Business_name,Tab_name):
    '''
    遍历并选择功能
    :param driver:
    :param Fun_name:
    :return:
    '''

    SuperClassName = driver.find_element_by_id(Business_List['Id'])
    print(SuperClassName)

    Sub_Business_Types =SuperClassName.find_element_by_id(Sub_Business_Type['Id'])
    LinearLayouts =Sub_Business_Types.find_elements_by_class_name(Sub_Business_Types['LinearLayout'])

    for i in range(0, len(LinearLayouts)):
        texts = LinearLayouts[i].find_element_by_class_name(Sub_Business_Types['TextView']).text
        sleep(0.1)
        if texts == Tab_name:
            sleep(0.1)
            LinearLayouts[i].find_element_by_class_name(Sub_Business_Types['TextView']).click()
            break
        driver.implicitly_wait(30)


    RelativeLayouts = SuperClassName.find_elements_by_class_name(Business_List['LinearLayout'])

    for i in range(0,len(RelativeLayouts)):
        texts = RelativeLayouts[i].find_element_by_class_name(Business_List['TextView']).text
        sleep(0.1)
        if texts == Business_name:
            sleep(0.1)
            RelativeLayouts[i].find_element_by_class_name(Business_List['TextView']).click()
            break
        driver.implicitly_wait(30)
    try:
        # 未登录
        Login.Boot_Password_login(driver)
    except:
        # 已登录
        print('当前用户已登录成功，无需引导登录。')