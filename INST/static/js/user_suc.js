$(function(){
    $("#INP_SUC").keyup(function(){
        $.ajax("/Suc/", {
            "async": true,
            "type": "POST",
            "dataType": "json",
            "data": {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                "inp_text": $("#INP_SUC").val()
            },
            "success": function(user_suc){
                document.getElementById("U_LIST").innerHTML=user_suc
            }
        })
    })
})