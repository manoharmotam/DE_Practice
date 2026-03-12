CREATE TABLE Organizations (
    OrgID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrgName TEXT,
    TenantID TEXT,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Repositories (
    RepoID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Path TEXT,
    CapacityGB INTEGER,
    FreeSpaceGB INTEGER
);

CREATE TABLE BackupJobs (
    JobID INTEGER PRIMARY KEY AUTOINCREMENT,
    JobName TEXT,
    OrgID INTEGER,
    RepoID INTEGER,
    JobType TEXT,
    Schedule TEXT,
    Enabled INTEGER DEFAULT 1
);

CREATE TABLE JobObjects (
    ObjectID INTEGER PRIMARY KEY AUTOINCREMENT,
    JobID INTEGER,
    ObjectType TEXT,
    ObjectName TEXT,
    ObjectGUID TEXT
);

CREATE TABLE BackupSessions (
    SessionID INTEGER PRIMARY KEY AUTOINCREMENT,
    JobID INTEGER,
    StartTime DATETIME,
    EndTime DATETIME,
    Result TEXT,
    ProcessedObjects INTEGER,
    FailedObjects INTEGER,
    DataSizeMB INTEGER
);

CREATE TABLE SessionLogs (
    LogID INTEGER PRIMARY KEY AUTOINCREMENT,
    SessionID INTEGER,
    ObjectName TEXT,
    Severity TEXT,
    Message TEXT,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
