/* Welcome to the SQL mini project. You will carry out this project partly in
the PHPMyAdmin interface, and partly in Jupyter via a Python connection.

This is Tier 2 of the case study, which means that there'll be less guidance for you about how to setup
your local SQLite connection in PART 2 of the case study. This will make the case study more challenging for you: 
you might need to do some digging, aand revise the Working with Relational Databases in Python chapter in the previous resource.

Otherwise, the questions in the case study are exactly the same as with Tier 1. 

PART 1: PHPMyAdmin
You will complete questions 1-9 below in the PHPMyAdmin interface. 
Log in by pasting the following URL into your browser, and
using the following Username and Password:

URL: https://sql.springboard.com/
Username: student
Password: learn_sql@springboard

The data you need is in the "country_club" database. This database
contains 3 tables:
    i) the "Bookings" table,
    ii) the "Facilities" table, and
    iii) the "Members" table.

In this case study, you'll be asked a series of questions. You can
solve them using the platform, but for the final deliverable,
paste the code for each solution into this script, and upload it
to your GitHub.

Before starting with the questions, feel free to take your time,
exploring the data, and getting acquainted with the 3 tables. */


/* QUESTIONS 
/* Q1: Some of the facilities charge a fee to members, but some do not.
Write a SQL query to produce a list of the names of the facilities that do. */
name 	
Tennis Court 1
Tennis Court 2
Massage Room 1
Massage Room 2
Squash Court

SELECT name
FROM Facilities
WHERE membercost <> 0

/* Q2: How many facilities do not charge a fee to members? */
4

SELECT name
FROM Facilities
WHERE membercost = 0

/* Q3: Write an SQL query to show a list of facilities that charge a fee to members,
where the fee is less than 20% of the facility's monthly maintenance cost.
Return the facid, facility name, member cost, and monthly maintenance of the
facilities in question. */
facid 	name 	membercost 	monthlymaintenance 	
0 	Tennis Court 1 		5.0 	200
1 	Tennis Court 2 		5.0 	200
2 	Badminton Court 	0.0 	50
3 	Table Tennis 		0.0 	10
4 	Massage Room 1 		9.9 	3000
5 	Massage Room 2 		9.9 	3000
6 	Squash Court 		3.5 	80
7 	Snooker Table 		0.0 	15
8 	Pool Table 		0.0 	15

SELECT facid, name, membercost, monthlymaintenance
FROM Facilities
WHERE membercost < .2 * monthlymaintenance

/* Q4: Write an SQL query to retrieve the details of facilities with ID 1 and 5.
Try writing the query without using the OR operator. */
acid 	name 		membercost 	guestcost 	initialoutlay 	monthlymaintenance 	
1 	Tennis Court 2 	5.0 		25.0 		8000 		200
5 	Massage Room 2 	9.9 		80.0 		4000 		3000

SELECT *
FROM Facilities
WHERE facid IN (1,5);

/* Q5: Produce a list of facilities, with each labelled as
'cheap' or 'expensive', depending on if their monthly maintenance cost is
more than $100. Return the name and monthly maintenance of the facilities
in question. */

name 		monthlymaintenance 	monthlymaintenanceText 	
Tennis Court 1 	200 			expensive
Tennis Court 2 	200 			expensive
Badminton Court 50 			cheap
Table Tennis 	10 			cheap
Massage Room 1 	3000 			expensive
Massage Room 2 	3000 			expensive
Squash Court 	80 			cheap
Snooker Table 	15 			cheap
Pool Table 	15 			cheap

SELECT name, monthlymaintenance
FROM Facilities
CASE WHEN monthlymaintenance > 100 THEN 'expensive'
ELSE 'cheap' END AS monthlymaintenanceText


/* Q6: You'd like to get the first and last name of the last member(s)
who signed up. Try not to use the LIMIT clause for your solution. */

Darren 	Smith

SELECT firstname, surname
FROM Members
WHERE memid <> 0
HAVING MAX(joindate)

/* Q7: Produce a list of all members who have used a tennis court.
Include in your output the name of the court, and the name of the member
formatted as a single column. Ensure no duplicate data, and order by
the member name. */
name 		CourtName
Anne Baker 	Tennis Court 1
Anne Baker 	Tennis Court 2
Burton Tracy 	Tennis Court 2
Burton Tracy 	Tennis Court 1
Charles Owen 	Tennis Court 1
Charles Owen 	Tennis Court 2
Darren Smith 	Tennis Court 2
David Farrell 	Tennis Court 1
David Farrell 	Tennis Court 2
David Jones 	Tennis Court 2

SELECT DISTINCT CONCAT(m.firstname,' ', m.surname) AS name, f.name AS CourtName 
FROM Members AS m 
INNER JOIN Bookings AS b 
INNER JOIN Facilities AS f 
ON b.facid = f.facid 
WHERE m.memid != 0 AND f.name LIKE 'Tennis Court%' 
ORDER by name

/* Q8: Produce a list of bookings on the day of 2012-09-14 which
will cost the member (or guest) more than $30. Remember that guests have
different costs to members (the listed costs are per half-hour 'slot'), and
the guest user's ID is always 0. Include in your output the name of the
facility, the name of the member formatted as a single column, and the cost.
Order by descending cost, and do not use any subqueries. */

member_name 	facility_name 	Cost
GUEST GUEST 	Massage Room 2 	320.0
GUEST GUEST 	Massage Room 1 	160.0
GUEST GUEST 	Massage Room 1 	160.0
GUEST GUEST 	Massage Room 1 	160.0
GUEST GUEST 	Tennis Court 2 	150.0
GUEST GUEST 	Tennis Court 1 	75.0
GUEST GUEST 	Tennis Court 1 	75.0
GUEST GUEST 	Tennis Court 2 	75.0
GUEST GUEST 	Squash Court 	70.0
Jemima Farrell 	Massage Room 1 	39.6

SELECT CONCAT(m.firstname,' ', m.surname) AS member_name, f.name AS facility_name 
CASE WHEN b.memid != 0 THEN b.slots * f.membercost 
ELSE f.guestcost * b.slots END AS 'Cost' 
FROM Facilities as f 
INNER JOIN Bookings as b 
ON f.facid = b.facid 
INNER JOIN Members AS m
ON b.memid = m.memid
WHERE Cost > 30 AND b.starttime LIKE '2012-09-14%' 
ORDER BY Cost DESC

/* Q9: This time, produce the same result as in Q8, but using a subquery. */
I cannot figure this out.


/* PART 2: SQLite

Export the country club data from PHPMyAdmin, and connect to a local SQLite instance from Jupyter notebook 
for the following questions.  

QUESTIONS:
/* Q10: Produce a list of facilities with a total revenue less than 1000.
The output of facility name and total revenue, sorted by revenue. Remember
that there's a different cost for guests and members! */
name 	total_revenue
0 	Pool Table 	70.0
1 	Squash Court 	266.0
2 	Tennis Court 1 	345.0
3 	Squash Court 	644.0

SELECT f.name, (guestcost * SUM(k.slots) + membercost * SUM(b.slots)) AS total_revenue 
FROM Facilities AS f 
INNER JOIN Bookings AS b 
ON f.facid = b.facid AND b.memid != 0 
INNER JOIN Bookings AS k ON b.facid = k.facid and k.memid = 0    
GROUP BY k.slots, b.slots 
HAVING total_revenue < 1000 
Order by total_revenue LIMIT 10

/* Q11: Produce a report of members and who recommended them in alphabetic surname,firstname order */

surname 	firstname 	Recommender
0 	Bader 	Florence 	Sarwin Ramnaresh
1 	Baker 	Anne 	None
2 	Baker 	Timothy 	Coplin Joan
3 	Boothe 	Tim 	None
4 	Butters 	Gerald 	Genting Matthew
5 	Coplin 	Joan 	None
6 	Crumpet 	Erica 	None
7 	Dare 	Nancy 	None
8 	Farrell 	David 	None
9 	Farrell 	Jemima 	Baker Timothy
10 	Farrell 	Jemima 	Pinker David
11 	GUEST 	GUEST 	None
12 	Genting 	Matthew 	Rumney Henrietta
13 	Hunt 	John 	None
14 	Jones 	David 	Jones Douglas
15 	Jones 	Douglas 	None
16 	Joplette 	Janice 	Dare Nancy
17 	Joplette 	Janice 	Jones David
18 	Mackenzie 	Anna 	None
19 	Owen 	Charles 	None
20 	Pinker 	David 	None
21 	Purview 	Millicent 	Hunt John
22 	Rownam 	Tim 	Boothe Tim
23 	Rumney 	Henrietta 	None
24 	Sarwin 	Ramnaresh 	None
25 	Smith 	Darren 	Joplette Janice
26 	Smith 	Darren 	Butters Gerald
27 	Smith 	Darren 	Owen Charles
28 	Smith 	Darren 	Smith Jack
29 	Smith 	Darren 	Mackenzie Anna
30 	Smith 	Darren 	None
31 	Smith 	Jack 	None
32 	Smith 	Tracy 	Worthington-Smyth Henry
33 	Smith 	Tracy 	Purview Millicent
34 	Smith 	Tracy 	Crumpet Erica
35 	Stibbons 	Ponder 	Baker Anne
36 	Stibbons 	Ponder 	Bader Florence
37 	Tracy 	Burton 	Stibbons Ponder
38 	Tupperware 	Hyacinth 	None
39 	Worthington-Smyth 	Henry 	None

rs2 = pd.read_sql_query("SELECT m.surname, m.firstname, r.surname||' ' ||r.firstname AS Recommender FROM Members AS m LEFT JOIN Members AS r ON m.memid = r.recommendedby ORDEr BY m.surname, m.firstname", conn)

/* Q12: Find the facilities with their usage by member, but not guests */
facility_name 	member_name 	Usage
0 	Table Tennis 	Darren Smith 	2
1 	Massage Room 1 	Darren Smith 	2
2 	Snooker Table 	Darren Smith 	2
3 	Pool Table 	Darren Smith 	1
4 	Pool Table 	Darren Smith 	1
5 	Tennis Court 1 	Tracy Smith 	3
6 	Tennis Court 1 	Tracy Smith 	3
7 	Massage Room 1 	Tim Rownam 	2
8 	Squash Court 	Darren Smith 	2
9 	Snooker Table 	Tracy Smith 	2

SELECT f.name AS facility_name, m.firstname||' '||m.surname AS member_name, b.slots AS Usage FROM Facilities AS f INNER JOIN Bookings AS b Using(facid) INNER JOIN Members AS m Using(memid) WHERE memid != 0 LIMIT 10

/* Q13: Find the facilities usage by month, but not guests */

name 	month 	Usage
0 	Badminton Court 07 	344
1 	Massage Room 1 	07 	421
2 	Massage Room 2 	07 	27
3 	Pool Table 	07 	783
4 	Snooker Table 	07 	421
5 	Squash Court 	07 	195
6 	Table Tennis 	07 	385
7 	Tennis Court 1 	07 	308
8 	Tennis Court 2 	07 	276

SELECT name, strftime('%m', starttime) AS month, COUNT(b.slots) AS Usage FROM Facilities INNER JOIN Bookings AS b USING(facid) WHERE b.memid <> 0 GROUP BY name
