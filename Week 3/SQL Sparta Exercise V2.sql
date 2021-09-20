DROP TABLE IF EXISTS CSTrainers;
DROP TABLE IF EXISTS CSAttendees;
DROP TABLE IF EXISTS CourseSchedule;
DROP TABLE IF EXISTS Rooms;
DROP TABLE IF EXISTS Academies
DROP TABLE IF EXISTS CourseCatalog;
DROP TABLE IF EXISTS Employees;



CREATE TABLE Academies(
    AcademyID INT NOT NULL IDENTITY PRIMARY KEY,
    AcademyName VARCHAR(20)
)

CREATE TABLE Rooms(
    RoomID INT NOT NULL IDENTITY PRIMARY KEY,
    AcademyID INT FOREIGN KEY REFERENCES Academies(AcademyID),
    RoomName VARCHAR(20),
    Description VARCHAR(MAX),
    Capacity INT CHECK (Capacity <= 25)
)

CREATE TABLE CourseCatalog(
    CourseTypeID INT NOT NULL IDENTITY PRIMARY KEY,
    CourseName VARCHAR(20),
    Duration INT
)

CREATE TABLE Employees(
    EmployeeID INT NOT NULL IDENTITY PRIMARY KEY,
    FirstName VARCHAR(20),
    LastName VARCHAR(20),
    EmployeeType CHAR CHECK (EmployeeType = 'T' OR EmployeeType = 'S'),
    StartDate DATE
)

CREATE TABLE CourseSchedule(
    CourseScheduleID INT NOT NULL IDENTITY PRIMARY KEY,
    AcademyID INT FOREIGN KEY REFERENCES Academies(AcademyID),
    RoomID INT FOREIGN KEY REFERENCES Rooms(RoomID),
    CourseTypeID INT FOREIGN KEY REFERENCES CourseCatalog(CourseTypeID),
    StartDate DATE,
    EndDate DATE
)
CREATE TABLE CSTrainers(
    TrainerID INT,
    CourseScheduleID INT,
    EmployeeType CHAR,
    CONSTRAINT CSTrainersID PRIMARY KEY (TrainerID, CourseScheduleID),
    FOREIGN KEY (TrainerID) REFERENCES Employees (EmployeeID),
    FOREIGN KEY (CourseScheduleID) REFERENCES CourseSchedule(CourseScheduleID)
)
CREATE TABLE CSAttendees(
    AttendeeID INT,
    CourseScheduleID INT,
    CONSTRAINT CSAttendeeID PRIMARY KEY (AttendeeID, CourseScheduleID),
    FOREIGN KEY (AttendeeID) REFERENCES Employees (EmployeeID),
    FOREIGN KEY (CourseScheduleID) REFERENCES CourseSchedule(CourseScheduleID)
)


INSERT INTO [Academies]
           ([AcademyName])
     VALUES
           ('Richmond')
;


INSERT INTO [Academies]
           ([AcademyName])
     VALUES
           ('Birmingham')
;

INSERT INTO [Academies]
           ([AcademyName])
     VALUES
           ('Leeds')
;

INSERT INTO [Rooms]
           ([AcademyID]
           ,[RoomName]
           ,[Description]
           ,[Capacity])
     VALUES
           (1
           ,'Room 1'
           ,'Next to the new Lo; sign'
           ,12)
;

INSERT INTO [Rooms]
           ([AcademyID]
           ,[RoomName]
           ,[Description]
           ,[Capacity])
     VALUES
           (1
           ,'Room 2'
           ,'Behind the new Sparta sign'
           ,18)
;
INSERT INTO [Rooms]
           ([AcademyID]
           ,[RoomName]
           ,[Description]
           ,[Capacity])
     VALUES
           (1
           ,'Room 3'
           ,'No air-con'
           ,18)
;

INSERT INTO [Rooms]
           ([AcademyID]
           ,[RoomName]
           ,[Description]
           ,[Capacity])
     VALUES
           (1
           ,'Room 4'
           ,'Has second door with number lock'
           ,10)
;

INSERT INTO [Rooms]
           ([AcademyID]
           ,[RoomName]
           ,[Description]
           ,[Capacity])
     VALUES
           (1
           ,'Boardroom'
           ,'Use as last resort'
           ,14)
;

INSERT INTO [CourseCatalog]
           ([CourseName]
           ,[Duration])
     VALUES
           ('BA-Test',
           7)
;
INSERT INTO [CourseCatalog]
           ([CourseName]
           ,[Duration])
     VALUES
           ('Engineering',
           12)
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           ,[StartDate]
           )
     VALUES
	 		     ('Tim','Cawte','T','07/14/2017')
				 ;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           ,[StartDate]
           )
     VALUES
	 		     ('Richard','Gurney','T','07/01/2017')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           )
     VALUES
	 		     ('Adam','Smith','S')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('John','Williams','S')
;
INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Nick','Willis','S')
;
INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Jenny','Jones','S')
;
INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Katie','Prince','S')
;
INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Peter','Brown','S')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Mo','Khan','S')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Juan','Carlos','S')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Jan','Miller','S')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Kyle','Carpenter','S')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Alvarao','Carlos','S')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Margaret','Baker','S')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Oti','Mwase','S')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Joe','Mann','S')
;

INSERT INTO [Employees]
           ([FirstName]
           ,[LastName]
           ,[EmployeeType]
           
           )
     VALUES
	 		     ('Steve','Harris','S')
;

INSERT INTO [CourseSchedule]
           ([AcademyID]
           ,[RoomID]
           ,[CourseTypeID]
           ,[StartDate]
           ,[EndDate])
     VALUES
           (1
           ,1
           ,1
           ,'01/15/2018'
           ,'03/02/2018'
		  )
;

INSERT INTO [CourseSchedule]
           ([AcademyID]
           ,[RoomID]
           ,[CourseTypeID]
           ,[StartDate]
           ,[EndDate])
     VALUES
           (1
           ,3
           ,2
           ,'01/22/2018'
           ,'03/03/2018'
		  )
;
INSERT INTO [CSTrainers]
           ([CourseScheduleID]
           ,[TrainerID])
     VALUES
           (1
           ,1)
;
INSERT INTO [CSTrainers]
           ([CourseScheduleID]
           ,[TrainerID])
     VALUES
           (2
           ,2)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (1
           ,3)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (1
           ,4)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (1
           ,5)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (1
           ,6)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (1
           ,7)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (1
           ,8)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (2
           ,9)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (2
           ,10)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (2
           ,11)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (2
           ,12)
;

INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (2
           ,13)
;


INSERT INTO [CSAttendees]
           ([CourseScheduleID]
           ,[AttendeeID])
     VALUES
           (2
           ,15)
;
INSERT INTO Rooms(
    AcademyID, RoomName, [Description], Capacity
)
VALUES(
    2, 'Room 1', 'Main room, new computers', 20
)
INSERT INTO CourseCatalog(
    CourseName, Duration
)
VALUES(
    'Data_Engineering', 12
)
INSERT INTO CourseSchedule(
    AcademyID,  RoomID, CourseTypeID, StartDate, EndDate
)
VALUES(
    2, 6, 3, '2021-08-23', '2021-11-05'
)

INSERT INTO Employees
         ([FirstName]
         ,[LastName]
         ,[EmployeeType])
 VALUES
        ('Danny', 'Jew','T'),
        ('Matt','Lyons','S'),
        ('Suleman','Mahmood','S'),
        ('Robert','Fabijan','S'),
        ('Matthew','Reddy','S'),
        ('Sreeniti','Sudhakar','S'),
        ('Marcel','Krzyzanowski','S'),
        ('Ahmedali','Reman','S'),
        ('Gavinder','Hayer','S'),
        ('Leon','Seeamber','S'),
        ('Tia','Edmead','S');

    INSERT INTO CSTrainers(
        TrainerID, CourseScheduleID)
    VALUES(
        18,3
    )

    INSERT INTO CSAttendees(
        AttendeeID, CourseScheduleID
    )
    VALUES
        (19,3),
        (20,3),
        (21,3),
        (22,3),
        (23,3),
        (24,3),
        (25,3),
        (26,3),
        (27,3),
        (28,3);


SELECT * FROM Employees;

SELECT CC.CourseName, CS.StartDate, CS.EndDate,  
CASE 
WHEN CC.CourseName = 'BA-Test' THEN DATEADD(D, 56, CS.EndDate) 
ELSE DATEADD(D,84, CS.EndDate)
END AS 'Check Date',
A.AcademyName, R.RoomName, T.FirstName + ' ' + T.LastName AS 'Trainer', E.FirstName + ' ' + E.LastName AS 'Spartan' FROM CourseSchedule CS
--SELECT * FROM CourseSchedule CS
LEFT JOIN Academies A ON CS.AcademyID = A.AcademyID
LEFT JOIN Rooms R ON R.RoomID = CS.RoomID
LEFT JOIN CourseCatalog CC ON CS.CourseTypeID = CC.CourseTypeID

LEFT JOIN CSAttendees CSA ON CS.CourseScheduleID = CSA.CourseScheduleID
LEFT JOIN Employees E ON  CSA.AttendeeID = E.EmployeeID

LEFT JOIN CSTrainers CST ON CS.CourseScheduleID = CST.CourseScheduleID
LEFT JOIN Employees T ON CST.TrainerID = T.EmployeeID;

-- SELECT CC.CourseName, CS.StartDate, CS.EndDate, 
-- CASE 
-- WHEN CC.CourseName = 'BA-Test' THEN DATEADD(D, 56, CS.EndDate) 
-- ELSE DATEADD(D,84, CS.EndDate)
-- END AS 'Check Date',
-- A.AcademyName, R.RoomName, T.FirstName + ' ' + T.LastName AS 'Trainer', LEFT(E.FirstName,1) + ' ' + LEFT(E.LastName,1) AS 'Spartan Initials' FROM CourseSchedule CS
-- --SELECT * FROM CourseSchedule CS
-- LEFT JOIN Academies A ON CS.AcademyID = A.AcademyID
-- LEFT JOIN Rooms R ON R.RoomID = CS.RoomID
-- LEFT JOIN CourseCatalog CC ON CS.CourseTypeID = CC.CourseTypeID

-- LEFT JOIN CSAttendees CSA ON CS.CourseScheduleID = CSA.CourseScheduleID
-- LEFT JOIN Employees E ON  CSA.AttendeeID = E.EmployeeID

-- LEFT JOIN CSTrainers CST ON CS.CourseScheduleID = CST.CourseScheduleID
-- LEFT JOIN Employees T ON CST.TrainerID = T.EmployeeID
-- ;
