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

