const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('articles.db');

// Example of fetching articles
db.serialize(() => {
  db.all("SELECT * FROM articles", (err, rows) => {
    if (err) {
      console.error(err.message);
    }
    console.log(rows);
  });
});

db.close();
