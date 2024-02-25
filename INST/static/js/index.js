function like(){
    $(document).click(function(event){
        let a = $(event.target)
        if (a.attr("class") == "button-like"){
            $.ajax("/", {
                "type": "POST",
                "async": true,
                "dataType": "json",
                "data": {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    "post_id": a.attr("id")
                },
                "success": function(like_img){
                    if(like_img["like_id"]){
                        document.getElementById(a.attr("id")).src = "/static/img/like-1.png"
                    }
                    else{
                        document.getElementById(a.attr("id")).src = "/static/img/like-2.png"
                    }
                    document.getElementById(`${a.attr("id")}-likes`).innerHTML=`<b>Likes: ${like_img["num"]}</b>`
                }
            })
        }
    })
}

function savepost(){
    $(document).click(function(event){
        let b = $(event.target)
        if (b.attr("class") == "button-comment 1"){
            $.ajax("/", {
                "type": "POST",
                "dataType": "json",
                "async": true,
                "data": {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    "save_id": b.data("id")
                },
                "success": function(save){
                    if (save["post_save_id"]){
                        document.getElementById(`${b.data("id")}-save`).src = "/static/img/save-2.png"
                    }
                    else {
                        document.getElementById(`${b.data("id")}-save`).src = "/static/img/save.png"
                    }

                }
            })
        }
    })
}


$(document).ready(function(){
    like();
    savepost();
})