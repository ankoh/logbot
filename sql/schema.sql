-- The SQL schema is based on the Slack RTM API
--
-- Message: https://api.slack.com/events/message

-- User
CREATE TABLE IF NOT EXISTS User (
    ID INT PRIMARY KEY,
    Key VARCHAR(255) NOT NULL
);
CREATE INDEX IF NOT EXISTS User_Key_Idx ON User(Key);

-- Channel
CREATE TABLE IF NOT EXISTS Channel (
    ID INT PRIMARY KEY,
    Key VARCHAR(255) NOT NULL
);
CREATE INDEX IF NOT EXISTS Channel_Key_Idx ON Channel(Key);

-- Channel Messages
CREATE TABLE IF NOT EXISTS ChannelMessage (
    ID INT PRIMARY KEY,
    Author INT NOT NULL,
    Channel INT NOT NULL,
    When TIMESTAMP NOT NULL,
    Content TEXT NOT NULL,

    FOREIGN KEY (Channel) REFERENCES Channel(ID) ON DELETE CASCADE,
    FOREIGN KEY (Author) REFERENCES User(ID) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS ChannelMessage_Channel_Idx ON ChannelMessage(Channel);
CREATE INDEX IF NOT EXISTS ChannelMessage_Author_Idx ON ChannelMessage(Author);
CREATE INDEX IF NOT EXISTS ChannelMessage_When_Idx ON ChannelMessage(When);

-- Channel Message Updates
CREATE TABLE IF NOT EXISTS ChannelMessageUpdate (
    ID INT PRIMARY KEY,
    Message INT NOT NULL,
    Author INT NOT NULL,
    When TIMESTAMP NOT NULL,
    Content TEXT NOT NULL,

    FOREIGN KEY (Message) REFERENCES ChannelMessage(ID) ON DELETE CASCADE,
    FOREIGN KEY (Author) REFERENCES User(ID) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS ChannelMessageUpdate_Message_Idx ON ChannelMessageUpdate(Message);
CREATE INDEX IF NOT EXISTS ChannelMessageUpdate_Author_Idx ON ChannelMessageUpdate(Author);
CREATE INDEX IF NOT EXISTS ChannelMessageUpdate_When_Idx ON ChannelMessageUpdate(When);

-- Channel Message Reaction
CREATE TABLE IF NOT EXISTS ChannelMessageReaction  (
    ID INT PRIMARY KEY,
    Message INT NOT NULL,
    Reaction VARCHAR(50) NOT NULL,
    Count INT NOT NULL,

    FOREIGN KEY (Message) REFERENCES ChannelMessage(ID) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS ChannelMessageReaction_Message_Idx ON ChannelMessageReaction(Message);
CREATE INDEX IF NOT EXISTS ChannelMessageReaction_Reaction_Idx ON ChannelMessageReaction(Reaction);
