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
// New Client

var userDataRef = firebase.database().ref("Umugenzi").orderByKey();
userDataRef.once("value").then(function(snapshot) {
    snapshot.forEach(function(childSnapshot) {
        var key = childSnapshot.key;
        var childData = childSnapshot.val();          
        $("#client").append("<p>" + childData + "</p>");
    });
});
});