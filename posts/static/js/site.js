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
            if (response["more_posts"] || !response["no_posts"]){
                $("#posts").append(response["html"]);
                var moreposts = document.getElementById('morePosts');
                moreposts.parentNode.appendChild(moreposts);
                currPage++;
            }
            
            if (!response["more_posts"]) {
                $("#morePosts").css("display", "none");
            }

          })
          .fail(function (e) {
              console.log(e);
          })
          ;
    });
});