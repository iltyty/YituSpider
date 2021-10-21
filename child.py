class Child:
    BASE_XPATH = '//div[@class="DicomViewer__info--topLeft"]//ul[@class="DicomInfo "]/li'
    NAME_XPATH = BASE_XPATH + '[1]'
    EXAM_ID_XPATH = BASE_XPATH + '[2]'
    GENDER_XPATH = BASE_XPATH + '[3]'
    CHILD_ID_XPATH = BASE_XPATH + '[4]'
    AGE_XPATH = BASE_XPATH + '[5]'

    DATE_XPATH = '//div[@class="DicomViewer__info--topRight"]//ul/li[2]'

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
