var pg = require('pg');
var conString = "postgres://superuser:Cinema4d@localhost:5432/thedb";

var client = new pg.Client(conString);
client.connect();

client.query({
    name: 'insert beatle',
    text: "INSERT INTO accounts(username, password) values($1, $2)",
    values: ['George', 'password']
});