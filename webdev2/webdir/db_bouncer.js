var pg = require('pg');
var conString = "postgres://superuser:Cinema4d@localhost:5432/thedb";

const connectionString = process.env.DATABASE_URL || 'postgres://localhost:5432/todo';

var client = new pg.Client(conString);

document.getElementById("create").onclick = function() {addNewUser()};

function addNewUser() {

 client.connect();
   client.query({


        name: 'insert beatle',
        text: "INSERT INTO accounts(username, password) values($1, $2)",
        values: ['George', 'password']
    })

   
} ;

