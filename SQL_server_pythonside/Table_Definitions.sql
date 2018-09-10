Create Table Client_Master (
Client_ID int primary key
,Client_First_Name varchar(50)
,Client_Middle_Name varchar(50)
,Client_Last_Name varchar(50)
,Client_Street_Address varchar(100)
,Client_State char(2)
,Client_Zip5 char(5)
,Client_Phone char(10)
,Client_Email nvarchar(100)
,Client_DOB datetime
)
