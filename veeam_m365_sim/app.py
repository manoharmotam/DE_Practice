from fastapi import FastAPI
from db import get_db, init_db
import random, datetime
from fastapi.staticfiles import StaticFiles



app = FastAPI()
init_db()
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.post("/create_demo")
def create_demo():
    db = get_db()
    db.execute("INSERT INTO Organizations (OrgName,TenantID) VALUES (?,?)",
               ("DemoOrg","tenant-123"))
    db.execute("INSERT INTO Repositories (Name,Path,CapacityGB,FreeSpaceGB) VALUES (?,?,?,?)",
               ("LocalRepo","/backup",1000,800))
    db.execute("INSERT INTO BackupJobs (JobName,OrgID,RepoID,JobType,Schedule) VALUES (?,?,?,?,?)",
               ("M365-Mailbox-Job",1,1,"Exchange","Daily"))
    for u in ["user1","user2","user3"]:
        db.execute("INSERT INTO JobObjects (JobID,ObjectType,ObjectName,ObjectGUID) VALUES (1,'User',?,?)",
                   (u,f"guid-{u}"))
    db.commit()
    return {"status":"Demo created"}

@app.post("/run_job/{job_id}")
def run_job(job_id:int):
    db = get_db()
    start = datetime.datetime.now()
    objects = db.execute("SELECT ObjectName FROM JobObjects WHERE JobID=?", (job_id,)).fetchall()

    end = datetime.datetime.now()

    failed = 0
    result = "Success"

    db.execute("""INSERT INTO BackupSessions 
        (JobID,StartTime,EndTime,Result,ProcessedObjects,FailedObjects,DataSizeMB)
        VALUES (?,?,?,?,?,?,?)""",
        (job_id,start,end,"Running",len(objects),0,random.randint(50,500)))

    session_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]

    for obj in objects:
        if random.random() < 0.2:
            db.execute("INSERT INTO SessionLogs (SessionID,ObjectName,Severity,Message) VALUES (?,?,?,?)",
                       (session_id,obj[0],"Error","User not found"))
            failed += 1

    result = "Failed" if failed else "Success"

    db.execute("UPDATE BackupSessions SET Result=?, FailedObjects=? WHERE SessionID=?",
               (result,failed,session_id))

    db.commit()
    return {"result":result}


@app.get("/sessions")
def sessions():
    db = get_db()
    return db.execute("SELECT * FROM BackupSessions").fetchall()

@app.get("/logs")
def logs():
    db = get_db()
    return db.execute("SELECT * FROM SessionLogs").fetchall()

@app.get("/jobs")
def jobs():
    db = get_db()
    return db.execute("SELECT * FROM BackupJobs").fetchall()
