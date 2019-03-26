caps = {
    "platformName":"Android",
    "deviceName":"Nexus_5X",
    # "deviceName": "d24a88e9",
    "platformVersion":"7.0",
    # "platformVersion":"9",
    "unicodeKeyboard":True,
    "resetKeyboard":True,
    "appPackage":"com.kingpoint.gmcchh",
    'appActivity':'.newui.main.skeleton.view.SkeletonActivity',
    "app":"/Users/hanxin/Desktop/Gmcchh-debug.apk",
}

temp = {
    "platformName":"Android",
    "deviceName":"Nexus_5X",
    # "deviceName": "d24a88e9",
    "platformVersion":"7.0",
    # "platformVersion": "9",
    "unicodeKeyboard":True,
    "resetKeyboard":True,
    "appPackage":"com.kingpoint.gmcchh",
    'appActivity':'.newui.main.skeleton.view.SkeletonActivity',
    # "app":"/Users/hanxin/Desktop/Gmcchh-debug.apk",
    "noReset":True,
}

machine = {
    "platformName":"Android",
    "deviceName":"d24a88e9",
    "platformVersion":"9",
    "unicodeKeyboard":True,
    "resetKeyboard":True,
    "appPackage":"com.kingpoint.gmcchh",
    'appActivity':'.newui.main.skeleton.view.SkeletonActivity',
    "app":"/Users/hanxin/Desktop/Gmcchh-debug.apk",
    "noReset":True,
}

desired_caps = {
                #测试包路径
                # 'app': apk_path + '\\app\\Gmcchh_test',
                'platformName': 'Android',
                #p9
                # 'deviceName': 'KWG5T16516005851',
                # 'platformVersion': '7.0',

                #荣耀8
                # 'deviceName': 'SQRNW17722011218',
                # 'platformVersion': '8.0',

                # 小米note3
                # 'deviceName': 'bd4bc802',
                # 'platformVersion': '7.1.1',
                #模拟器
                'deviceName': '127.0.0.1:52001',
                'platformVersion': '4.4.2',
                # 不需要每次都安装apk
                'noReset': True,
                # apk包名
                # 'appPackage': 'com.taobao.taobao',
                'appPackage':'com.kingpoint.gmcchh',
                # apk的launcherActivity
                # 'appActivity': 'com.taobao.tao.welcome.Welcome'
                'appActivity': 'com.kingpoint.gmcchh.newui.main.skeleton.view.SkeletonActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                # 'automationName': 'uiautomator2'
                }

user_data={
    'username':'136 0032 1834',
    'password':'112233',
}

