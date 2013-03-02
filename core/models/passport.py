# -*- coding:utf-8 -*-

import django.db.models as models
from djangosphinx.models import SphinxSearch
from django.utils.encoding import force_unicode

from orphan_list.common.constants import REGISTRATION_CHOICES, \
    FAMILY_STATUSES_CHOICES, PROVISION_OF_EMPLOYMENT_CHOICES, \
    EDUCATION_TYPE_CHOICES, BOOLEAN_CHOICES, DOCUMENT_CHOICES


class Passport(models.Model):
    class Meta:
        app_label = "core"
        verbose_name = "Passport"

    def __unicode__(self):
        return "%s %s %s" % (self.name, self.patronymic, self.surname)

    name = models.CharField("Имя", help_text= "Имя", max_length=255)
    patronymic = models.CharField("Отчество", help_text="Отчество",
        max_length=255)
    surname = models.CharField("Фамилия", help_text="Фамилия",
        max_length=255)
    birthday = models.DateField("Дата рождения", help_text="Дата рождения",
        blank=True, null=True)
    document = models.CharField("Документ удостоверяющий личность", 
        choices=DOCUMENT_CHOICES, 
        help_text = "Документ удостоверяющий личность", max_length=255, 
        blank=True)
    document_number = models.CharField("Серия / номер", 
        help_text="Серия / номер", max_length=255, 
        blank=True)
    document_date = models.DateField("Дата выдачи", 
        help_text="Дата выдачи документа", blank=True, null=True)
    document_issue = models.CharField("Кем выдан", help_text="Кем выдан",
        blank=True, max_length=255)
    date_of_list = models.DateField("Дата включения в список",
        help_text="Дата включения в список", blank=True, null=True)
    registration_type = models.CharField("Тип регистрации",
        choices=REGISTRATION_CHOICES,
        help_text="Тип регистрации по месту жительства", max_length=1024,
        blank=True)
    reqistration_address = models.TextField("Адрес проживания",
        help_text="Адрес проживания", blank=True)
    no_reqistration_reason = models.TextField("Причина отсутсвия "
        "регистрации", help_text="Причина отсутсвия регистрации", blank=True)
    fact_live_address_in_mo = models.TextField("Фактически проживает на "
        "территории МО", help_text="""Фактически проживает на территории
        МО / адрес (соц. гостиница, общежитие, муниципальный фонд,
        у родтсвенников и прочие)""", blank=True)
    fact_live_address_outside_mo = models.TextField("Фактически проживает "
        "за пределами МО / адрес", help_text="Фактически проживает за "

                                             "предлами МО", blank=True)
    place_of_first_find = models.TextField("Место первичного выявления / "
                                           "статус", help_text="""Место
        первичного выявления / статус / правовой статус
        (реквизиты документов)""", blank=True)
    family_status = models.CharField("Семейное положение",
        help_text="Семейное положение", choices=FAMILY_STATUSES_CHOICES,
        max_length=1024, blank=True)
    children = models.IntegerField("Количество детей",
        help_text="Количество детей", default=0, max_length=255)
    has_real_estate = models.CharField("Владеет недвижимостью",
        help_text="Владеет недвижимостью", default=False, choices=BOOLEAN_CHOICES,
        max_length=255)
    real_estate_EGRP = models.TextField("Недвижимое имущество "
                                        "зарег. в ЕГРП",
        help_text="""Недвижимое имущество, право (долевой) собсвенности на
        которое зарегистрировано  в ЕГРП / адрес""", blank=True)
    real_estate_not_EGRP = models.TextField("Недвижимое имущество на "
                                            "ином праве",
        help_text="""Недвжимое имущество, принадлежащее
        на ином праве/адрес""", blank=True)
    form_of_care = models.TextField("Форма устройства",
        help_text="Форма устройство(опека, патронат и пр.", blank=True)
    spokesman_data = models.TextField("Сведения о законном представителе",
        help_text="Сведения о законном представителе (ФИО, степен родства "
                  "и пр.", blank=True)
    provision_of_employment_type = models.CharField("Как трудоустроен",
        help_text="Как трудоустроен", choices=PROVISION_OF_EMPLOYMENT_CHOICES,
        max_length=1024, blank=True)
    employment_place = models.TextField("Место работы",
        help_text="Место работы", blank=True)
    education_type = models.CharField("Тип получаемого образования",
        help_text="Тип получаемого образования",
        choices=EDUCATION_TYPE_CHOICES, max_length=1024, blank=True)
    name_institution_of_education = models.TextField("Наименование учебного "
        "заведения", help_text="Наименование учебного заведения", blank=True)
    vacation = models.TextField("В отпуске по уходу за ребенком",
        help_text="В отпуске по уходу за ребенком / получение пособий, "
                  "денежныъ выплат и пр", blank=True)
    army = models.TextField("В армии", help_text="В Армии", blank=True)
    jail = models.TextField("В местах лишения свободы", help_text="В местах "
        "лишения свободы", blank=True)
    other = models.TextField("Указать иное", help_text="Указать иное",
        blank=True)
    date_of_service_expired = models.DateField("Дата окончания учебы, службы",
            help_text="Дата окончание учебы (службы, пребывания в местах "
            "лишения свободы)", blank=True, null=True)
    annotation = models.TextField("Примечания", help_text="Примечания",
             blank=True)



    # search
    search = SphinxSearch()
