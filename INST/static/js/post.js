function comment(){
    $("#BTN_COMMENT").click(function(){
        $.ajax($("#BTN_COMMENT").data("url"), {
            "type": "POST",
            "async": true,
            "dataType": "json",
            "data": {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                "text_c": $("#INP_COMMENT").val()
            },
            "success": function(posts_d){
                document.getElementById("DIV_COMMENTS").innerHTML+=posts_d
            }
        })
    })
}

function like(){
    $("#BTN_LIKE").click(function(){
        $.ajax($("#BTN_LIKE").data("url_l"), {
            "type": "POST",
            "async": true,
            "dataType": "json",
            "data": {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                "likes_t": true
            },
            "success": function(post_like){
                if(post_like["ection"] == "dislike"){
                    document.getElementById("BTN_LIKE").src = "/static/img/like-1.png"
                }
                else{
                    document.getElementById("BTN_LIKE").src = "/static/img/like-2.png"
                }

                document.getElementById("P_INT").innerHTML=`<b>Likes: ${post_like["int"]}</b>`;
            }
        })
    })
}

$(document).ready(function(){
    document.getElementById("BTN_COMMENT").addEventListener("mouseover", (event)=>{document.getElementById("BTN_COMMENT").src="/static/img/send.png"});
    document.getElementById("BTN_COMMENT").addEventListener("mouseleave", (event)=>{document.getElementById("BTN_COMMENT").src="/static/img/send-bl.png"});
    comment();
    like();
})