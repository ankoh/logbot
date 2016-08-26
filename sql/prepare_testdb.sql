CREATE DATABASE logbot_testdb;
CREATE USER logbot_test_runner WITH PASSWORD 'thanks_for_all_the_fish';
GRANT ALL PRIVILEGES ON DATABASE logbot_testdb TO logbot_test_runner;