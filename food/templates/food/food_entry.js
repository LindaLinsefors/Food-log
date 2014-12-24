$(document).ready(function(){

    $("#quantity").change(function(){
        $("#quantity").val( eval( $("#quantity").val() ) );
    }); 

    $(".percent").change(function(){
        $("#unknown").val(
            100
            - $("#fruit").val() 
            - $("#veg").val() 
            - $("#dairy").val() 
            - $("#protein").val() 
            - $("#water").val() 
            - $("#startch").val() 
            - $("#junk").val() 
        );
    });   
    
    $("#get_info").click(function(){
        $.post("{% url 'get_food_stuff_info' %}",
            {
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                food_stuff_name: $("#food_stuff").val()
            },
            function(response, status){
                if (response == "does_not_exist"){
                    alert('"'+$("#food_stuff").val()+'"'
                          + " does not exixt yet");
                }
                else {
                    var food_stuff = JSON.parse(response)[0]["fields"];
                    $("#ingredients").val(food_stuff["ingredients"]);
                    $("#fruit").val(food_stuff["fruit"]);
                    $("#veg").val(food_stuff["veg"]);
                    $("#dairy").val(food_stuff["dairy"]);
                    $("#protein").val(food_stuff["protein"]);
                    $("#water").val(food_stuff["water"]);
                    $("#startch").val(food_stuff["startch"]);
                    $("#junk").val(food_stuff["junk"]);
                    $("#unknown").val(food_stuff["unknown"]);
                }
            }
        );
    }); 
         
});
