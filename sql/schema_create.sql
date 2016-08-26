-- The SQL schema is based on the Slack RTM API
--
-- Message: https://api.slack.com/events/message

-- profile
CREATE TABLE IF NOT EXISTS profile (
    id INT PRIMARY KEY,
    key VARCHAR(255) NOT NULL
);
CREATE INDEX IF NOT EXISTS profile_key_idx ON profile(key);

-- Channel
CREATE TABLE IF NOT EXISTS channel (
    id INT PRIMARY KEY,
    key VARCHAR(255) NOT NULL
);
CREATE INDEX IF NOT EXISTS channel_key_idx ON channel(key);

-- Channel Messages
CREATE TABLE IF NOT EXISTS channel_message (
    id INT PRIMARY KEY,
    author INT NOT NULL,
    channel INT NOT NULL,
    ts TIMESTAMP NOT NULL,
    content TEXT NOT NULL,

    FOREIGN KEY (channel) REFERENCES channel(ID) ON DELETE CASCADE,
    FOREIGN KEY (author) REFERENCES profile(ID) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS channel_message_channel_idx ON channel_message(channel);
CREATE INDEX IF NOT EXISTS channel_message_author_idx ON channel_message(author);
CREATE INDEX IF NOT EXISTS channel_message_ts_idx ON channel_message(ts);

-- Channel Message Updates
CREATE TABLE IF NOT EXISTS channel_message_update (
    id INT PRIMARY KEY,
    message INT NOT NULL,
    author INT NOT NULL,
    ts TIMESTAMP NOT NULL,
    content TEXT NOT NULL,

    FOREIGN KEY (message) REFERENCES channel_message(id) ON DELETE CASCADE,
    FOREIGN KEY (author) REFERENCES profile(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS channel_message_update_message_idx ON channel_message_update(message);
CREATE INDEX IF NOT EXISTS channel_message_update_author_idx ON channel_message_update(author);
CREATE INDEX IF NOT EXISTS channel_message_update_ts_idx ON channel_message_update(ts);

-- Channel Message Reaction
CREATE TABLE IF NOT EXISTS channel_message_reaction  (
    id INT PRIMARY KEY,
    message INT NOT NULL,
    reaction VARCHAR(50) NOT NULL,
    count INT NOT NULL,

    FOREIGN KEY (message) REFERENCES channel_message(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS channel_message_reaction_message_idx ON channel_message_reaction(message);
CREATE INDEX IF NOT EXISTS channel_message_reaction_reaction_idx ON channel_message_reaction(reaction);
