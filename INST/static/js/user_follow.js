function user_follow(){
    $(function(){
        $("#BTN_USER").click(function(){
            $.ajax($("#BTN_USER").data("url"), {
                "type": "POST",
                "async": true,
                "dataType": "json",
                "data": {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                "success": function(user_profils){
                    document.getElementById("U_FOLLOWERS").innerHTML=`<b>Followers:</b> ${user_profils["followers"]} <b style="margin-left: 10px;">Follow:</b> ${user_profils["follow"]}`


                    if (user_profils["my_subscribe"] == true){
                        document.getElementById("BTN_USER").innerHTML="Unfollow"
                        document.getElementById("BTN_USER").className="btn btn-outline-light btn-block"
                    }
                    else {
                        document.getElementById("BTN_USER").innerHTML="Follow"
                        document.getElementById("BTN_USER").className="btn btn-primary btn-block"
                    }
                }
            })
        })
    })
}


$(document).ready(function(){
    user_follow()
})