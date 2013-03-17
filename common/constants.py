# -*- coding:utf-8 -*-

REGISTRAION_WHERE_CHOICES = (
    (u"Жилой дом", u"Жилой дом"),
    (u"Квартира", u"Квартира"),
    (u"Общежитие", u"Общежитие"),
    (u"Гостиница-приют", u"Гостиница-приют"),
    (u"Дом маневренного фонда", u"Дом маневренного фонда"),
    (u"Специальный дом для одиноких престарелых", u"Специальный дом для одиноких престарелых"),
    (u"Дом-интернат для инвалидов", u"Дом-интернат для инвалидов"),
    (u"Иное жилое помещение", u"Иное жилое помещение"),
)

FAMILY_STATUS_CHOICES = (
    (u"не состоит в браке", u"не состоит в браке"),
    (u"состоит  в браке", u"состоит в браке"),
)

JOB_TYPE_CHOICES = (
    (u"Работает", u"Работает"),
    (u"Обучается", u"Обучаетcя"),
    (u"В отпуске по уходу за ребенком", u"В отпуске по уходу за ребенком"),
    (u"В вооруженных силах", u"В вооруженных силах"),
    (u"В местах лишения свободы", u"В местах лишения свободы"),
    (u"В розыске", u"В розыске"),
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
    (u"ребенок-сирота", u"ребенок-сирота"),
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

DEFAULT_SEARCH_TRUE_VALUES = {
    u'surname': u'Фамилия',
    u'name': u'Имя',
    u'year': u'Год рождения',
    }

DEFAULT_XLS_TRUE_VALUES = {
    u'surname': u'Фамилия',
    u'name': u'Имя',
    u'birthday': u'Дата рождения',
    }

EXTRA_SEARCH_FIELDS = {
    u'from_year': u'С года рождения',
    u'to_year': u'До года рождения',
    u'year': u'Год рождения',
    }

SPOKESNAM_TYPE_CHOICES = (
    (u"Гос. учереждение", u"Гос. учереждение"),
    (u"Приемная семья", u"Приемная семья"),
    (u"Опека", u"Опека"),
    (u"Патронатное воспитание", u"Патронатное воспитание"),
    (u"Иное", u"Иное"),
)

REGION_CHOICES = (
    (u"Краснодарский край", u"Краснодарский край"),
    (u"Алтайский край", u"Алтайский край"),
    (u"Амурская область", u"Амурская область"),
    (u"Архангельская область", u"Архангельская область"),
    (u"Астраханская область", u"Астраханская область"),
    (u"Белгородская область", u"Белгородская область"),
    (u"Брянская область", u"Брянская область"),
    (u"Владимирская область", u"Владимирская область"),
    (u"Волгоградская область", u"Волгоградская область"),
    (u"Вологодская область", u"Вологодская область"),
    (u"Воронежская область", u"Воронежская область"),
    (u"Еврейская автономная область", u"Еврейская автономная область"),
    (u"Забайкальский край", u"Забайкальский край"),
    (u"Ивановская область", u"Ивановская область"),
    (u"Иркутская область", u"Иркутская область"),
    (u"Калининградская область", u"Калининградская область"),
    (u"Калужская область", u"Калужская область"),
    (u"Камчатский край", u"Камчатский край"),
    (u"Кемеровская область", u"Кемеровская область"),
    (u"Кировская область", u"Кировская область"),
    (u"Костромская область", u"Костромская область"),
    (u"Красноярский край", u"Красноярский край"),
    (u"Курганская область", u"Курганская область"),
    (u"Курская область", u"Курская область"),
    (u"Ленинградская область", u"Ленинградская область"),
    (u"Липецкая область", u"Липецкая область"),
    (u"Магаданская область", u"Магаданская область"),
    (u"Москва", u"Москва"),
    (u"Московская область", u"Московская область"),
    (u"Мурманская область", u"Мурманская область"),
    (u"Ненецкий автономный округ", u"Ненецкий автономный округ"),
    (u"Нижегородская область", u"Нижегородская область"),
    (u"Новгородская область", u"Новгородская область"),
    (u"Новосибирская область", u"Новосибирская область"),
    (u"Омская область", u"Омская область"),
    (u"Оренбургская область", u"Оренбургская область"),
    (u"Орловская область", u"Орловская область"),
    (u"Пензенская область", u"Пензенская область"),
    (u"Пермский край", u"Пермский край"),
    (u"Приморский край", u"Приморский край"),
    (u"Псковская область", u"Псковская область"),
    (u"Республика Адыгея", u"Республика Адыгея"),
    (u"Республика Алтай", u"Республика Алтай"),
    (u"Республика Башкортостан", u"Республика Башкортостан"),
    (u"Республика Бурятия", u"Республика Бурятия"),
    (u"Республика Дагестан", u"Республика Дагестан"),
    (u"Республика Ингушетия", u"Республика Ингушетия"),
    (u"Республика Кабардино-Балкария", u"Республика Кабардино-Балкария"),
    (u"Республика Калмыкия", u"Республика Калмыкия"),
    (u"Республика Карачаево-Черкессия", u"Республика Карачаево-Черкессия"),
    (u"Республика Карелия", u"Республика Карелия"),
    (u"Республика Коми", u"Республика Коми"),
    (u"Республика Марий Эл", u"Республика Марий Эл"),
    (u"Республика Мордовия", u"Республика Мордовия"),
    (u"Республика Саха Якутия", u"Республика Саха Якутия"),
    (u"Республика Северная Осетия - Алания", u"Республика Северная Осетия - Алания"),
    (u"Республика Татарстан", u"Республика Татарстан"),
    (u"Республика Тыва", u"Республика Тыва"),
    (u"Республика Удмуртия", u"Республика Удмуртия"),
    (u"Республика Хакасия", u"Республика Хакасия"),
    (u"Республика Чувашия", u"Республика Чувашия"),
    (u"Ростовская область", u"Ростовская область"),
    (u"Рязанская область", u"Рязанская область"),
    (u"Самарская область", u"Самарская область"),
    (u"Санкт-Петербург", u"Санкт-Петербург"),
    (u"Саратовская область", u"Саратовская область"),
    (u"Сахалинская область", u"Сахалинская область"),
    (u"Свердловская область", u"Свердловская область"),
    (u"Смоленская область", u"Смоленская область"),
    (u"Ставропольский край", u"Ставропольский край"),
    (u"Тамбовская область", u"Тамбовская область"),
    (u"Тверская область", u"Тверская область"),
    (u"Томская область", u"Томская область"),
    (u"Тульская область", u"Тульская область"),
    (u"Тюменская область,", u"Тюменская область,"),
    (u"Тюменская область", u"Тюменская область"),
    (u"Ульяновская область", u"Ульяновская область"),
    (u"Хабаровский край", u"Хабаровский край"),
    (u"Ханты-Мансийский автономный округ - Югра", u"Ханты-Мансийский автономный округ - Югра"),
    (u"Челябинская область", u"Челябинская область"),
    (u"Чеченская республика", u"Чеченская республика"),
    (u"Чукотский автономный округ", u"Чукотский автономный округ"),
    (u"Ямало-Ненецкий автономный округ", u"Ямало-Ненецкий автономный округ"),
    (u"Ярославская область", u"Ярославская область"),
)

MO_CHOICES = (
    (u"Город Краснодар", u"Город Краснодар"),
    (u"Город-курорт Анапа", u"Город-курорт Анапа"),
    (u"Город Армавир", u"Город Армавир"),
    (u"Город-курорт Геленджик", u"Город-курорт Геленджик"),
    (u"Город Горячий Ключ", u"Город Горячий Ключ"),
    (u"Город Кропоткин", u"Город Кропоткин"),
    (u"Город-герой Новороссийск", u"Город-герой Новороссийск"),
    (u"Город-курорт Сочи", u"Город-курорт Сочи"),
    (u"Абинский район", u"Абинский район"),
    (u"Апшеронский район", u"Апшеронский район"),
    (u"Белоглинский район", u"Белоглинский район"),
    (u"Белореченский район", u"Белореченский район"),
    (u"Брюховецкий район", u"Брюховецкий район"),
    (u"Выселковский район", u"Выселковский район"),
    (u"Гулькевичский район", u"Гулькевичский район"),
    (u"Динской район", u"Динской район"),
    (u"Ейский район", u"Ейский район"),
    (u"Кавказский район", u"Кавказский район"),
    (u"Калининский район", u"Калининский район"),
    (u"Каневский район", u"Каневский район"),
    (u"Кореновский район", u"Кореновский район"),
    (u"Красноармейский район", u"Красноармейский район"),
    (u"Крыловский район", u"Крыловский район"),
    (u"Крымский район", u"Крымский район"),
    (u"Курганинский район", u"Курганинский район"),
    (u"Кущевский район", u"Кущевский район"),
    (u"Лабинский район", u"Лабинский район"),
    (u"Ленинградский район", u"Ленинградский район"),
    (u"Мостовский район", u"Мостовский район"),
    (u"Новокубанский район", u"Новокубанский район"),
    (u"Новопокровский район", u"Новопокровский район"),
    (u"Павловский район", u"Павловский район"),
    (u"Приморско-Ахтарский район", u"Приморско-Ахтарский район"),
    (u"Славянский район", u"Славянский район"),
    (u"Староминский район", u"Староминский район"),
    (u"Тбилисский район", u"Тбилисский район"),
    (u"Темрюкский район", u"Темрюкский район"),
    (u"Тимашевский район", u"Тимашевский район"),
    (u"Тихорецкий район", u"Тихорецкий район"),
    (u"Туапсинский район", u"Туапсинский район"),
    (u"Успенский район", u"Успенский район"),
    (u"Усть-Лабинский район", u"Усть-Лабинский район"),
    (u"Щербиновский район", u"Щербиновский район"),
)
