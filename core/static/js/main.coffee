$(document).ready ->
    $(".date").mask("99.99.9999")

    # set mask on serial number according type of document
    $(".document_type").click ->
        document_type = $(".document_type :selected").val()
        if document_type == "Паспорт"
            $(".document_number").mask("серия: 99-99  номер: 999999")
        if document_type == "Свидетельство о рождении"
            $(".document_number").mask("серия: *-**  номер: 999999")
        if document_type == "Другой документ"
            $(".document_number").unmask()
    
    # set active tab
    for id in ["list", "create", "login"]
        if (document.URL.match(id))
            $("#" + id).addClass("active")
            break


    # ajax login form upload
    #log = () ->
    #    $("#test").show()
    #    $("#myModal").modal("show")
    #    alert("1")

    #$("#login").click ->
    #    $("#login_form").load("/core/login/")
    #    $("#myModal").modal("show")
        
