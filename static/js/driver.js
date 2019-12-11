$(document).ready(function(){
    var firebaseConfig = {
            apiKey: "AIzaSyAd4ZfpGHCefyg2YWrgI-q5vJfps_18zFY",
            authDomain: "trips-93fd2.firebaseapp.com",
            databaseURL: "https://trips-93fd2.firebaseio.com",
            projectId: "trips-93fd2",
            storageBucket: "trips-93fd2.appspot.com",
            messagingSenderId: "199100272502",
            appId: "1:199100272502:web:c2d8bd8abc68e91841f457"
          };
          // Initialize Firebase
          firebase.initializeApp(firebaseConfig);
    
    //New driver
    var userDataRef = firebase.database().ref("Umushoferi").orderByKey();

    userDataRef.once("value").then(function(snapshot) {
        snapshot.forEach(function(childSnapshot) {
            var key = childSnapshot.key;
            var childData = childSnapshot.val();       
            var lname = childSnapshot.val().lname
            var fname = childSnapshot.val().fname
            var email = childSnapshot.val().email
            var gender = childSnapshot.val().gender
            var password = childSnapshot.val().password
            var phone = childSnapshot.val().phone

            $("#name").append("<p>" + lname + "</p>");
            $("#age").append("<p>" + fname + "</p>");
            $("#permit").append("<p>" + email + "</p>");
            $("#plate").append("<p>" + gender + "</p>");
            $("#pass").append("<p>" + password + "</p>");
            $("#tel").append("<p>" + phone + "</p>");
        });
    });
// Clients
    var userDataRef = firebase.database().ref("Umugenzi").orderByKey();
    userDataRef.once("value").then(function(snapshot) {
        snapshot.forEach(function(childSnapshot) {
            var key = childSnapshot.key;
            var childData = childSnapshot.val();       
            var lname = childSnapshot.val().lname
            var fname = childSnapshot.val().fname
            var email = childSnapshot.val().email
            var gender = childSnapshot.val().gender
            var password = childSnapshot.val().password
            var phone = childSnapshot.val().phone

            $("#name1").append("<p>" + lname + "</p>");
            $("#age1").append("<p>" + fname + "</p>");
            $("#permit1").append("<p>" + email + "</p>");
            $("#plate1").append("<p>" + gender + "</p>");
            $("#pass1").append("<p>" + password + "</p>");
            $("#tel1").append("<p>" + phone + "</p>");
    });
});

    });
