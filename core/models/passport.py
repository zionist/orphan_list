# -*- coding:utf-8 -*-

import django.db.models as models
from djangosphinx.models import SphinxSearch

from orphan_list.common.constants import REGISTRAION_WHERE_CHOICES, FAMILY_STATUS_CHOICES, JOB_TYPE_CHOICES, \
    BOOLEAN_CHOICES, DOCUMENT_CHOICES, LOWFUL_STATUSES, EDUCATION_TYPE_CHOICES, HIRING_TYPE_CHOICES, LODGING_CHOICES, \
    LODGING_HOUSE_OR_FLAT_CHOICES, REGION_CHOICES, MO_CHOICES, SPOKESNAM_TYPE_CHOICES


class Passport(models.Model):
    class Meta:
        app_label = "core"
        verbose_name = "Passport"

    def __unicode__(self):
        return "%s %s %s" % (self.surname, self.surname, self.patronymic)

    # name 
    surname = models.CharField("Фамилия", help_text="Фамилия",
                               max_length=255)
    name = models.CharField("Имя", help_text= "Имя", max_length=255)
    patronymic = models.CharField("Отчество", help_text="Отчество",
        max_length=255)
    birthday = models.DateField("Дата рождения", help_text="Дата рождения",
        blank=True, null=True)

    # orders and dates
    order_number = models.CharField("Номер приказа о внесении в список",
                                    help_text="Номер приказа", max_length=255,
                                    blank=True)
    order_allegation_date_and_time = models.DateTimeField("Дата и время подачи"
        " заявления", help_text = "Дата и время подачи заявления",
        blank=True, null=True)
    order_number_of_queue = models.CharField("Номер очередности",
         help_text = "Номер очередности", blank=True, max_length=1024)
    order_UMSO_conclusion_date = models.DateField("Дата заключения УОМС",
        help_text="Дата заключения УОМС", blank=True, null=True)
    order_date = models.DateField("Дата внесения в список",
        help_text="Дата внесения  в список", blank=True, null=True)

    # person document
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

    # registration
    registration_address_region = models.CharField("Адрес регистрации (регион)",
        help_text="Адрес регистрации (регион)", blank=True, max_length=2048,
        choices=REGION_CHOICES)
    registration_address_mo = models.CharField("Адрес регистрации (МО)",
        help_text="Адрес регистрации (МО)", blank=True, max_length=2048,
        choices=MO_CHOICES)
    registration_address_address = models.CharField("Арес регистрации (ул, № дома)",
        help_text="Арес регистрации (Ул, № дома)", blank=True, max_length=10000)
    registration_address_where = models.CharField("Вид жилого помещения по адресу регистрации",
        help_text="Вид жилого помещения по адресу регистрации", blank=True, max_length=2048,
        choices=REGISTRAION_WHERE_CHOICES)
    registration_other = models.CharField("Вид жилого помещения иной",
        help_text="Вид жилого помещения иной", blank=True, max_length=10000)

    registration_live_at_registration_address = \
        models.CharField("Сведения о совпадении регистрации и фактического проживания",
        help_text="Сведения о совпадении регистрации и фактического проживания", blank=True, max_length=10000,
            choices=BOOLEAN_CHOICES)

    living_address_region = models.CharField("Фактический адрес проживания (регион)",
        help_text="Фактический адрес проживания (регион)", blank=True, max_length=2048,
        choices=REGION_CHOICES)
    living_address_mo = models.CharField("Фактический адрес проживания (МО)",
        help_text="Фактический адрес проживания (МО)", blank=True, max_length=2048, choices=MO_CHOICES)
    living_address_address = models.CharField("Фактический адрес проживания (ул. № дома)",
        help_text="Фактический адрес проживания (ул. № дома)", blank=True, max_length=10000)
    living_address_where = models.CharField("Вид жилого помещения по адресу фактического проживания",
        help_text="Вид жилого помещения по адресу фактического проживания", blank=True, max_length=2048,
        choices=REGISTRAION_WHERE_CHOICES)
    living_other = models.CharField("Вид жилого помещения по адресу фактического проживания иной",
        help_text="Вид жилого помещения по адресу фактического проживания иной", blank=True,
        max_length=10000)

    # lowful status
    lowful_status = models.CharField("Правовой статус",
        help_text="Правовой статус", choices=LOWFUL_STATUSES, blank=True,
        max_length=255)
    lowful_status_date = models.DateField("Дата установления правового статуса",
        help_text="Дата установления правового статуса",
        null=True, blank=True)
    lowful_status_number = models.CharField("Номер документа правового статуса",
        help_text="Номер документа по которому установлен правовой статус",
        blank=True, max_length=255)
    lowful_status_invalidity = models.CharField("Инвалидность",
        help_text="Инвалидность", blank=True, choices=BOOLEAN_CHOICES,
        max_length=255)

    # spokesman data
    form_of_care_spokesman_data = models.CharField("Сведения о "
        "законном представителе",
        help_text="Сведения о законном представителе (ФИО, степен родства "
        "и пр.", blank=True, max_length=10000)
    form_of_care_spokesman_type = models.CharField("Кто представляет",
        help_text="Кто представляет", blank=True, max_length=1024,
        choices=SPOKESNAM_TYPE_CHOICES)

    # family status
    family_status = models.CharField("Семейное положение",
        help_text="Семейное положение", choices=FAMILY_STATUS_CHOICES,
        max_length=1024, blank=True)
    family_status_children = models.CharField("Количество детей",
        help_text="Количество детей", max_length=255, blank=True)

    # estate
    estate_has_estate = models.CharField("Обстоятельства, препятствующие"
        " проживанию в ранее занимаемых помещениях",
        help_text="Обстоятельства, препятствующие проживанию в ранее занимаемых помещениях", choices=BOOLEAN_CHOICES,
        max_length=255, blank=True)
    estate_cant_live_date_of_order  = models.DateField("Дата правового акта "
        "о невозможности проживания",
        help_text="Дата правового акта о невозможности проживания", null=True,
        blank=True)
    estate_cant_live_order_number  = models.CharField("Номер правового акта о "
        "невозможности проживания",
        help_text="Номер правового акта о невозможности проживания", blank=True,
        max_length=255)

    # job and education
    job_type_of_job = models.CharField("Форма занятости",
        help_text="Форма занятости",
        choices=JOB_TYPE_CHOICES, max_length=255, blank=True)
    job_how_hired = models.CharField("Как трудоустроен",
        help_text="Как трудоустроен", choices=HIRING_TYPE_CHOICES,
        max_length=255, blank=True)
    job_job_place = models.CharField("Где трудоустроен",
        help_text="Где трудоустроен", max_length=10000, blank=True)
    job_eduction_type = models.CharField("Тип учебного заведения",
                                         help_text="Тип учебного заведения",
        max_length=255,  choices=EDUCATION_TYPE_CHOICES, blank=True)
    job_education_house = models.CharField("Учебное заведение",
        help_text="Учебное заведение",  max_length=10000, blank=True)
    job_other = models.CharField("Форма занятости иное",
        help_text="Форма занятости иное", blank=True,
        max_length=10000)
    job_started = models.DateField("Дата начала",
        help_text="Дата начала формы занятости", blank=True, null=True)
    job_finished = models.DateField("Дата окончания",
        help_text="Дата окончания формы занятости", blank=True, null=True)

    # lodging
    lodging_accordance = models.CharField("Предоставлено жилье",
        help_text="Предоставлено жилье", choices=BOOLEAN_CHOICES,
        max_length=255, blank=True)
    lodging_how_gained = models.CharField("Как предоставлено",
        help_text="Как предоставлено", choices=LODGING_CHOICES, max_length=255,
        blank=True)
    lodging_house_or_flat = models.CharField("Дом / квартира",
        help_text="Дом / квартира", choices=LODGING_HOUSE_OR_FLAT_CHOICES,
        max_length=255, blank=True)
    lodging_square = models.CharField("Общая площадь",
        help_text="Общая площадь", max_length=2048, blank=True)

    # order_of hiring_date order_of_hiring_number movied to lodging
    order_of_hiring_date = models.DateField("Дата заключения договора найма",
        help_text="Дата заключения договора найма", blank=True, null=True)
    order_of_hiring_number = models.CharField("Номер договора найма",
        help_text="Номер договора найма", max_length=255, blank=True)
