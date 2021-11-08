/** https://www.youtube.com/watch?v=In0nB0ABaUk */
const fullName = document.getElementById("fullname");

const emailAddress = document.getElementById("emailaddress");

const form = document.getElementById("form");

const errorElement = document.getElementById("error-msg");

const message = document.getElementById("message");

form.addEventListener("submit", (e) => {

    e.preventDefault();
    let error = [];
    if (fullName.value === "" || fullName.value == null) {
        error.push("Your Full Name is required");
    } else  {
        for (let i = 0; i < error.length; i++) {
            if (error[i] === "Your Full Name is required") {
                error.splice[i, 1];
            }
        }
    }

    if (message.value === "" || message.value == null) {
        error.push("Your message is required");
    } else  {
        for (let i = 0; i < error.length; i++) {
            if (error[i] === "Your message is required") {
                error.splice[i, 1];
            }
        }
    }
    if ( error.length === 0){
      alert("Thank you for your email. We will get back to you as soon as we can.");
      location.href =  '/home' ;
    } else {
      error.push("Please fill in the form correctly");
    }
});