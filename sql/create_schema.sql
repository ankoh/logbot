-- The SQL schema is based on the Slack RTM API
--
-- Message: https://api.slack.com/events/message

-- Profile
CREATE TABLE IF NOT EXISTS profile (
    id SERIAL PRIMARY KEY,
    key VARCHAR(255) UNIQUE NOT NULL
);
CREATE INDEX IF NOT EXISTS profile_key_idx ON profile(key);

-- Channel
CREATE TABLE IF NOT EXISTS channel (
    id SERIAL PRIMARY KEY,
    key VARCHAR(255) UNIQUE NOT NULL
);
CREATE INDEX IF NOT EXISTS channel_key_idx ON channel(key);

-- Messages
CREATE TABLE IF NOT EXISTS message (
    id SERIAL PRIMARY KEY,
    author INT NOT NULL,
    channel INT NOT NULL,
    received TIMESTAMP NOT NULL,
    clock VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,

    FOREIGN KEY (channel) REFERENCES channel(ID) ON DELETE CASCADE,
    FOREIGN KEY (author) REFERENCES profile(ID) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS message_channel_idx ON message(channel);
CREATE INDEX IF NOT EXISTS message_author_idx ON message(author);
CREATE INDEX IF NOT EXISTS message_received_idx ON message(received);
CREATE INDEX IF NOT EXISTS message_clock_idx ON message(clock);
