$(document).ready ->

  # functions
  set_input_masks = () ->
    $(".date").mask("99.99.9999")
    $(".date_time").mask("99.99.9999 99:99")

    # set mask on serial number according type of document
    $("#id_document").click ->
      document_type = $("#id_document :selected").val()
      if document_type == "Паспорт"
        $(".document_number").mask("99-99 999999")
      if document_type == "Свидетельство о рождении"
        $(".document_number").mask("*-** 999999")
      if document_type == "Другой документ"
        $(".document_number").unmask()

  set_active_tab = () ->
    for id in ["list", "create", "login"]
      if (document.URL.match(id))
        $("#" + id).addClass("active")
        break

  show_hide_registration = () ->
    reg_type = $("#id_registration_type :selected").val()
    if reg_type == "по месту проживания" or reg_type == "по месту жительства"
      $(".registration_no_reqistration_reason").hide()
      $(".registration_address").show()

      # clear form values
      $('input.registration_no_reqistration_reason').each ->
        $(@).val("")

    if reg_type == "не имеет"
      $(".registration_address").hide()
      $(".registration_no_reqistration_reason").show()

      # clear form values
      $('input.registration_address').each ->
        $(@).val("")

    if reg_type == ""
      $(".registration_address").hide()
      $(".registration_no_reqistration_reason").hide()
      # clear form values
      $('input.registration_address').each ->
        $(@).val("")
      $('input.registration_no_reqistration_reason').each ->
        $(@).val("")

  # if age of person > 18 show spokesman data
  show_hide_spokesman_data = () ->
    vals = $("#id_birthday").val().split(".")
    day = vals[0]
    mounth = vals[1]
    year = vals[2]
    birhday = new Date(year, mounth, day)
    required_age = 18
    years_lasted = new Date() - birhday
    # get years from ms
    years_lasted = years_lasted/1000/60/60/24/360
    if years_lasted < required_age
      $("#spokesman_data").show()
    else
      $("#spokesman_data").hide()

  show_hide_estate = () ->
    estate_status = $("#id_estate_has_estate :selected").val()
    if estate_status == "Да"
      $(".has_estate").show()
    else
      $(".has_estate").hide()
      $("#id_estate_cant_live_date_of_order").val("")
      $("#id_estate_cant_live_order_number").val("")

  show_hide_job = () ->
    type_of_job = $("#id_job_type_of_job :selected").val()
    switch type_of_job
      when "Работает"
        $(".job_has_education").hide()
        $(".job_has_other").hide()
        $(".job_has_job").show()
        $("#id_job_eduction_type").val("")
        $("#id_job_education_house").val("")
        $("#id_job_other").val("")
      when "Обучается"
        $("#id_job_how_hired").val("")
        $("#id_job_job_place").val("")
        $("#id_job_other").val("")
        $(".job_has_other").hide()
        $(".job_has_job").hide()
        $(".job_has_education").show()
      when "Иное"
        $("#id_job_how_hired").val("")
        $("#id_job_job_place").val("")
        $("#id_job_how_hired").val("")
        $("#id_job_eduction_type").val("")
        $("#id_job_education_house").val("")
        $(".job_has_job").hide()
        $(".job_has_education").hide()
        $(".job_has_other").show()
      else
        $("#id_job_how_hired").val("")
        $("#id_job_job_place").val("")
        $("#id_job_how_hired").val("")
        $("#id_job_eduction_type").val("")
        $("#id_job_education_house").val("")
        $("#id_job_other").val("")
        $(".job_has_job").hide()
        $(".job_has_education").hide()
        $(".job_has_other").hide()

    if type_of_job == ""
      $("#id_job_started").val("")
      $("#id_job_finished").val("")
      $(".job_period").hide()
    else
      $(".job_period").show()

  show_hide_lodging = () ->
    lodging = $("#id_lodging_accordance :selected").val()
    if lodging == "Да"
      $(".lodging").show()
    else
      $('.lodging').each ->
        $(@).val("")
      $(".lodging").hide()

  # calls
  set_input_masks()
  set_active_tab()
  show_hide_registration()
  show_hide_spokesman_data()
  show_hide_estate()
  show_hide_job()
  show_hide_lodging()

  # form show hide logic
  $("#id_registration_type").click ->
    show_hide_registration()
  $("#id_estate_has_estate").click ->
    show_hide_estate()
  $("#id_birthday").focusout ->
    show_hide_spokesman_data()
  $("#id_job_type_of_job").click ->
    show_hide_job()
  $("#id_lodging_accordance").click ->
    show_hide_lodging()


