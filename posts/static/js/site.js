var currPage = 1;
var showMenu = false;
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
            url: "http://localhost:8000/ajax/" + (currPage + 1)
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
    $("#toggle-night").click(function() {
        $.ajax({
            url: "http://localhost:8000/ajax-toggle-night"
          }).done(function(response) {
            console.log(response);
            location.reload(true);
            //alert('test1');
          })
          .fail(function (e) {
            console.log(e);
            //alert('test2');
          })
          ;
    });
    $("#small-menu-button").click(function() {
        showMenu = !showMenu;
        if (showMenu) {
            $("#small-menu").css("display", "block");
        }
        else {
            $("#small-menu").css("display", "none");
        }
        
    });
});