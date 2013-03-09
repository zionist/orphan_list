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
      $('.registration_no_reqistration_reason').find("textarea, input").each ->
        $(@).val("")

    if reg_type == "не имеет"
      $(".registration_address").hide()
      $(".registration_no_reqistration_reason").show()

      # clear form values
      $('.registration_address').find("textarea, input").each ->
        $(@).val("")

    if reg_type == ""
        # clear form values
        $('.registration_address').find("textarea, input").each ->
          $(@).val("")
        $('.registration_no_reqistration_reason').find("textarea, input").each ->
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
    years_lasted = years_lasted/1000/60/60/24/360
    if years_lasted < required_age
      $("#spokesman_data").show()
    else
      $("#spokesman_data").hide()


  # calls
  set_input_masks()
  set_active_tab()
  show_hide_registration()
  show_hide_spokesman_data()

  # show no_registartion_reason
  $("#id_registration_type").click ->
    show_hide_registration()
  $("#id_birthday").focusout ->
    show_hide_spokesman_data()


