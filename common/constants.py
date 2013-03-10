# -*- coding:utf-8 -*-

REGISTRATION_CHOICES = (
    (u"по месту проживания", u"по месту проживания"),
    (u"по месту жительства", u"по месту жительства"),
    (u"не имеет", u"не имеет"),
)

FAMILY_STATUS_CHOICES = (
    (u"холост", u"холост"),
    (u"женат", u"замужем"),
)

JOB_TYPE_CHOICES = (
    (u"Работает", u"Работает"),
    (u"Обучается", u"Обучаетcя"),
    (u"В отпуске по уходу за ребенком", u"В отпуске по уходу за ребенком"),
    (u"В вооруженных силах", u"В вооруженных силах"),
    (u"В местах лишения свободы", u"В местах лишения свободы"),
    (u"Иное", u"Иное"),
)

EDUCATION_TYPE_CHOICES = (
    (u"Обучается в НПО", u"Обучаетcя в НПО"),
    (u"Обучается в СУЗе", u"Обучаетcя в СУЗе"),
    (u"Обучается в ВУЗе", u"Обучаетcя в ВУЗе"),
    (u"Получает второе высшее", u"Получает второе высшее"),
)

BOOLEAN_CHOICES = (
    (u"Да", u"Да"),
    (u"Нет", u"Нет"),
)

HIRING_TYPE_CHOICES = (
    (u"Через ЦЗН", u"Через ЦЗН"),
    (u"Самостоятельно", u"Самостоятельно"),
)

DOCUMENT_CHOICES = (
    (u"Паспорт", u"Паспорт"),
    (u"Свидетельство о рождении", u"Свидетельство о рождении"),
    (u"Другой документ", u"Другой документ"),
)

LOWFUL_STATUSES = (
    (u"Ребенок сирота", u"Ребенок сирота"),
    (u"Ребенок оставщийся без попечения родителей", u"Ребенок оставщийся без попечения родителей"),
)

LODGING_CHOICES = (
    (u"Куплено", u"Куплено"),
    (u"Построено", u"Построено"),
)

LODGING_HOUSE_OR_FLAT_CHOICES = (
    (u"Дом", u"Дом"),
    (u"Квартира", u"Квартира"),
)

DEFAULT_SEARCH_TRUE_VALUES = ['surname', 'name', 'birthday']

