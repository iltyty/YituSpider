class Child:
    BASE_XPATH = '//div[@class="DicomViewer__info--topLeft"]//ul/li'
    NAME_XPATH = BASE_XPATH + '[1]/text()'
    EXAM_ID_XPATH = BASE_XPATH + '[2]/text()'
    GENDER_XPATH = BASE_XPATH + '[3]/text()'
    CHILD_ID_XPATH = BASE_XPATH + '[4]/text()'
    AGE_XPATH = BASE_XPATH + '[5]/text()'

    DATE_XPATH = '//div[@class="DicomViewer__info--topRight"]//ul/li[2]/text()'

    RUS_BONE_XPATH = '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]'
    C_BONE_XPATH = '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]'

    ZH_BTN_XPATH = '//div[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[2]'
    ZH_BTN_SELECTOR = '#root > div > div.DetailLayout__wrapper > div.DetailLayout__right > div > div > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div:nth-child(2)'
    IMG_BTN_XPATH = '//div[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[3]'
    IMG_BTN_SELECTOR = '#root > div > div.DetailLayout__wrapper > div.DetailLayout__right > div > div > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div:nth-child(3)'

    ZH_BONE_XPATH = '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div'
    IMG_BONE_XPATH = '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/div'

    def __init__(self, name: str, exam_id: str, gender: str, child_id: str, age: str,
                 date: str, rus_bone: str, c_bone: str, zh_bone: str, img_bone: str):
        self.name = name
        self.exam_id = exam_id
        self.gender = gender
        self.child_id = child_id
        self.age = age
        self.date = date

        self.rus_bone = rus_bone
        self.c_bone = c_bone
        self.zh_bone = zh_bone
        self.img_bone = img_bone

    def __str__(self) -> str:
        res = '姓名：' + self.name
        res += '\n检查号：' + self.exam_id
        res += '\n性别：' + self.gender
        res += '\n病人号：' + self.child_id
        res += '\n年龄：' + self.age
        res += '\n检查日期：' + self.date
        res += '\nTW3 RUS 骨龄：' + self.rus_bone
        res += '\nTW3 C 骨龄：' + self.c_bone
        res += '\n中华 05 骨龄：' + self.zh_bone
        res += '\n图谱骨龄：' + self.img_bone + '\n'

        return res
