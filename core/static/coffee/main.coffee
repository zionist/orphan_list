$(document).ready ->

  # functions
  set_input_masks = () ->
    $(".date").mask("99.99.9999")
    $(".date_time").mask("99.99.9999 99:99")

    # set mask on serial number according type of document
    $("#id_document").click ->
      #$.mask.definitions['~']='.'
      document_type = $("#id_document :selected").val()
      if document_type == "Паспорт"
        $(".document_number").mask("99-99 999999")
      if document_type == "Свидетельство о рождении"
        #$(".document_number").mask("~-~~ 999999")
        $(".document_number").unmask()
      if document_type == "Другой документ"
        $(".document_number").unmask()

  set_active_tab = () ->
    for id in ["list", "create", "login"]
      if (document.URL.match(id))
        $("#" + id).addClass("active")
        break
    if (document.URL.match("select/search"))
      $("#select_search").addClass("active")
    if (document.URL.match("select/xls"))
      $("#select_xls").addClass("active")

  show_hide_registration_other = () ->
    where_live = $("#id_registration_address_where :selected").val()
    if where_live == "Иное жилое помещение"
      $(".registration_other").show()
    else
      $("#id_registration_other").val("")
      $(".registration_other").hide()

  show_hide_living_other = () ->
    where_live = $("#id_living_address_where :selected").val()
    if where_live == "Иное жилое помещение"
      $(".living_other").show()
    else
      # clear form values
      $("#id_living_other").val("")
      $(".living_other").hide()

  show_hide_registration_address = () ->
    live_at_registration = $("#id_registration_live_at_registration_address :selected").val()
    switch live_at_registration
      when "Нет"
        $(".living").show()
      when "Да"
        $(".living").hide()
        $("#id_living_address_region").val($("#id_registration_address_region").val())
        $("#id_living_address_mo").val($("#id_registration_address_mo").val())
        $("#id_living_address_address").val($("#id_registration_address_address").val())
        $("#id_living_address_where").val($("#id_registration_address_where").val())
      when ""
        $(".living").hide()
        $("#id_living_address_region").val("")
        $("#id_living_address_mo").val("")
        $("#id_living_address_address").val("")
        $("#id_living_address_where").val("")

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
      $(".spokesman_data").show()
    else
      $(".spokesman_data").hide()

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

  # set unset all flags on search and search_select pages
  $("a.checkbox-hide-all").click ->
      $('form input[type="checkbox"]').each ->
        $(@).attr('checked', false)
  $("a.checkbox-show-all").click ->
      $('form input[type="checkbox"]').each ->
        $(@).prop("checked", true)

  # calls
  set_active_tab()
  if (document.URL.match('create') or document.URL.match('update'))
    show_hide_registration_other()
    show_hide_living_other()
    show_hide_registration_address()
    set_input_masks()
    show_hide_spokesman_data()
    show_hide_estate()
    show_hide_job()
    show_hide_lodging()

  # form show hide logic
  $("#id_registration_address_where").click ->
    show_hide_registration_other()
  $("#id_living_address_where").click ->
    show_hide_living_other()
  $("#id_registration_live_at_registration_address").change ->
    show_hide_registration_address()

  $("#id_estate_has_estate").click ->
    show_hide_estate()
  $("#id_birthday").focusout ->
    show_hide_spokesman_data()
  $("#id_job_type_of_job").click ->
    show_hide_job()
  $("#id_lodging_accordance").click ->
    show_hide_lodging()


