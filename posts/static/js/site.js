var currPage = 1;

$(document).ready(function(){
    $("#morePosts").click(function() {
        // $.get("localhost:8000/posts/ajax/" + currPage) , function(response) {
        //     //No more posts
        //     console.log(response);
        //     if (response == 400) {
        //         $("#morePosts").css("display", "none");
        //     }
        //     else {
        //         $("#posts").html = $("#posts").html + response;
        //     }
        // }
        $.ajax({
            url: "http://localhost:8000/posts/ajax/" + (currPage + 1)
          }).done(function(response) {
            console.log(response);
            $("#posts").append(response);
            currPage++;
          })
          .fail(function (e) {
              console.log(e);
          })
          ;
    });
});