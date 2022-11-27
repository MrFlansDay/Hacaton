const { count } = require("console");
const mysql = require("mysql")

// function sss1() {
// const data = [[], [], []]

const connection = mysql.createConnection({
   host: "localhost",
   user: "root",
   database: "work",
   password: "12345"
});

const sql = `SELECT * FROM rating`;

connection.query(sql, function (err, results) {
   {
      if (err) console.log(err);
      // console.log(results[i]);
   }
   // for (let index = 0; index < results.length; index++) {
   //    data[index].push(results[index].position);
   //    data[index].push(results[index].fio);
   //    data[index].push(results[index].score);
   // }
   console.log(results[0].fio);
   // console.log(data)
});

connection.end();
// return data;
// }
// const data = sss1()
// console.log("data")
