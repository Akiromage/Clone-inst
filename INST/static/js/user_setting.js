function user_setting(){
        $("#BTN_C").click(function(){
        let img = new FormData()
        img.append('csrfmiddlewaretoken', $('input[name="csrfmiddlewaretoken"]').val())
        img.append("name", $("#name").val())
        img.append("status", $("#status").val())
        img.append("my_web", $("#my_web").val())
        img.append("avatar", document.getElementById("INP_FILES").files[0])
            $.ajax("/Usersett/", {
                "type": "POST",
                "dataType": "json",
                "async": true,
                "data": img,
                "processData": false,
                "contentType": false,
                "success": function(user_s){
                    if(user_s["status"]){
                        document.getElementById("status").value=user_s["status"]
                        }
                    if(user_s["name"]){
                        document.getElementById("name").value=user_s["name"]
                        }
                    if(user_s["my_web"]){
                        document.getElementById("my_web").value=user_s["my_web"]
                        }
                    if(user_s["avatar"]){
                        document.getElementById("avatar").src=user_s["avatar"]
                        }
                }
            })
        })
}

function user_psw(){
    $("#BTN_CO").click(function(){
        $.ajax("/Users/", {
            "dataType": "json",
            "type": "POST",
            "async": true,
            "data": {"psw_1": $("#password1").val(),
                    "psw_2": $("#password2").val(),
                     'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                     },
            "success": function(u_psw){
                document.getElementById("P_NUM").innerHTML=u_psw
                }
            })
        })
}

function user_mod(){
    $("#BTN_COM").click(function(){
        $.ajax("/Modifikations/", {
            "type": "POST",
            "dataType": "json",
            "async": true,
            "data": {"email": $("#email").val(),
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()},
            "success": function(u_email){
                document.getElementById("P_EMAIL").innerHTML=u_email
            }
        })
    })
}

function user_personal(){
    $("#BTN_COMP").click(function(){
        $.ajax("/Personal/", {
            "type": "POST",
            "dataType": "json",
            "async": true,
            "data": {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                "last_name": $("#last_name").val(),
                "first_name": $("#first_name").val()
            },
            "success": function(u_pers){
                 document.getElementById("P_PERS").innerHTML=u_pers
            }
        })
    })
}

$(document).ready(function(){
    $("#BTN_FILES").click(function(func_a){
        console.log("Completed")
        $("#INP_FILES").trigger("click")
    })
    user_setting()
    user_psw()
    user_mod()
    user_personal()
})