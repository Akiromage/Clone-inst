$(function(){
    $("#BTN_POST").click(function(){
        document.getElementById("DIV_ALL").inert=true
        document.getElementById("DIALOG").show();
    })

    $("#BTN_CLOSE").click(function(){
        document.getElementById("DIV_ALL").inert=false
        document.getElementById("DIALOG").close();
    })
})

function request(){
    $("#BTN").click(function(){
    let obj = new FormData()
    obj.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val())
    obj.append('text', $('#INP_TEXT').val())
    obj.append('file', document.getElementById("INP_FILE").files[0])
        $.ajax("/Postcreate/", {
            "async": true,
            "type": "POST",
            "dataType": "json",
            "data": obj,
            "processData": false,
            "contentType": false,
            "success": function(a){
                document.getElementById("DIALOG").close();
                document.getElementById("DIV_ALL").inert=false;
            }
        })
    })
}

$(document).ready(function(){
    document.getElementById("BTN_CLOSE").addEventListener("mouseover", (event)=>{document.getElementById("BTN_CLOSE").src="/static/img/close.png"});
    document.getElementById("BTN_CLOSE").addEventListener("mouseleave", (event)=>{document.getElementById("BTN_CLOSE").src="/static/img/close-bl.png"});
    $("#BTN_FILE").on("click", function(func_a){
        $("#INP_FILE").trigger("click")
    })
    request()
})

