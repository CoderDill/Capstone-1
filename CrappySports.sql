CREATE TABLE "users" (
  "id" int PRIMARY KEY,
  "username" text,
  "password" text
);

CREATE TABLE "bets" (
  "id" int PRIMARY KEY,
  "team1" text,
  "team2" text,
  "result" text,
  "amt_wagered" int,
  "amt_paid" int,
  "user_id" int
);

ALTER TABLE "bets" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");
