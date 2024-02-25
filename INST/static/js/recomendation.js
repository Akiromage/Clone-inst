function rec(){
            $.ajax("/Rec/", {
                "dataType": "json",
                "type": "POST",
                "async": true,
                "data": {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                },
                "success": function(scb){
                    document.getElementById("DIV_R").innerHTML=scb;
                }
            })
}

$(document).ready(function(){
    rec();
})