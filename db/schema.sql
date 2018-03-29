-- A basic little schema for the blog. Just one little table.
CREATE TABLE post (
  id          INTEGER       PRIMARY KEY,
  author      VARCHAR(75),
  title       TEXT,
  posted_on   DATETIME,
  body        TEXT
);