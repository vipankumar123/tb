
// validations applying on Username
function Username() {
    var user_value = $("#username_id").val()
    var regex_var =/^[ A-Za-z0-9-@&_.]*$/;

    if (user_value){
		if (user_value.match(regex_var)) {

	    	if(user_value.length <= 7 || user_value.length >25){
				$("#username_id").addClass('has-error');
				$("#username_id").removeClass('has-success');
				$("#user_label").text("It must contain minimum 8 characters")
				return false;
			}
			else{
				$("#user_label").text("");
				$("#username_id").removeClass('has-error');
				$("#username_id").addClass('has-success');
				return true;


			}


		}

		else{
			$("#username_id").addClass('has-error');
			$("#username_id").removeClass('has-success');
			$("#user_label").text("Invalid username")
			return false;

		}
	}
	else{

		$("#user_label").text("Please fill out this Field")
		$("#username_id").addClass('has-error');
		$("#username_id").removeClass('has-success');
		}  
	}

// validations applying on username ends here

// validations applying on password_label
function Password_Register() {
    password_value = $("#registerPassword").val();
    var regex_var = /^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,}$/
    if (password_value){
		if (password_value.match(regex_var)) {
				$("#password_label").text("")
				$("#registerPassword").removeClass('has-error');
				$("#registerPassword").addClass('has-success');
				return true;
		}
		else {
			$("#password_label").text("It must contain one lowercase,uppercase,digit and one special character")
			$("#registerPassword").addClass('has-error');
			$("#registerPassword").removeClass('has-success');
			return false;
		    }
		}
    else {
        $("#password_label").text("Please fill out this Field")
        $("#registerPassword").addClass('has-error');
        $("#registerPassword").removeClass('has-success');

        return false;
    }
}

// validations applying on password_label ends here


$(document).on('submit', '#loginform', function(){
	if (Username() && Password_Register() == true){
		return true;
	}
	else{
		Username();
		Password_Register();
		return false;
	}

})


function show() {
    var x = document.getElementById("registerPassword");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}