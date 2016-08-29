CREATE DATABASE logbot_testdb;
CREATE USER logbot_test_runner WITH PASSWORD 'thanks_for_all_the_fish';
GRANT ALL PRIVILEGES                  ON SCHEMA PUBLIC TO logbot_test_runner;
GRANT ALL PRIVILEGES ON ALL TABLES    IN SCHEMA PUBLIC TO logbot_test_runner;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA PUBLIC TO logbot_test_runner;
