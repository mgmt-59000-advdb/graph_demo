# Create Courses
```
CREATE (:Course {title: 'advdb'}),
       (:Course {title: 'cloud'}),
       (:Course {title: 'devops'});
```

# Create Instructor Node
```
CREATE (:Instructor {first_name: 'Rob', last_name: 'Elliott', email: 'elliot62@purdue.edu'});
```

# Create Relationship Between Instructor and Courses
```
MATCH (i:Instructor {email: 'elliot62@purdue.edu'}),
      (c:Course {title: 'advdb'})
CREATE (i)-[:INSTRUCTOR_FOR]->(c);
```

```
MATCH (i:Instructor {email: 'elliot62@purdue.edu'}),
      (c1:Course {title: 'cloud'}),
      (c2:Course {title: 'devops'})
CREATE (i)-[:INSTRUCTOR_FOR]->(c1),
       (i)-[:INSTRUCTOR_FOR]->(c2);
```

# Create Student Nodes
```
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mgmt-59000-advdb/graph_demo/main/merged_roster.csv' AS row
WITH row WHERE row.Email IS NOT NULL
MERGE (s:Student {email: row.Email})
ON CREATE SET s.first_name = row.`First Name`, s.last_name = row.`Last Name`;
```

# Connect Student Nodes to `advdb` Course
```
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mgmt-59000-advdb/graph_demo/main/merged_roster.csv' AS row
WITH row WHERE row.Course = 'advdb' AND row.Email IS NOT NULL
MATCH (c:Course {title: 'advdb'})
MERGE (s:Student {email: row.Email})
ON CREATE SET s.first_name = row.`First Name`, s.last_name = row.`Last Name`
MERGE (s)-[:ENROLLED_IN]->(c);
```

# Find Student Nodes with No Course Relationships
```
MATCH (s:Student)
WHERE NOT (s)-[:ENROLLED_IN]->(:Class)
RETURN s;
```

# Connect Student Nodes to `cloud` Course
```
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mgmt-59000-advdb/graph_demo/main/merged_roster.csv' AS row
WITH row WHERE row.Course = 'cloud' AND row.Email IS NOT NULL
MATCH (c:Course {title: 'cloud'})
MERGE (s:Student {email: row.Email})
ON CREATE SET s.first_name = row.`First Name`, s.last_name = row.`Last Name`
MERGE (s)-[:ENROLLED_IN]->(c);
```

# Connect Student Nodes to `devops` Course
```
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/mgmt-59000-advdb/graph_demo/main/merged_roster.csv' AS row
WITH row WHERE row.Course = 'devops' AND row.Email IS NOT NULL
MATCH (c:Course {title: 'devops'})
MERGE (s:Student {email: row.Email})
ON CREATE SET s.first_name = row.`First Name`, s.last_name = row.`Last Name`
MERGE (s)-[:ENROLLED_IN]->(c);
```

# View Just the `advdb` Course
```
MATCH (c:Course {title: 'advdb'})
RETURN c;
```

# Find Prof. Elliott's Biggest Fans
```
MATCH (s:Student)-[:ENROLLED_IN]->(c1:Course {title: 'advdb'}),
      (s)-[:ENROLLED_IN]->(c2:Course {title: 'cloud'}),
      (s)-[:ENROLLED_IN]->(c3:Course {title: 'devops'})
RETURN s;
```

# Find Your Own `Student` Node
```
# Write your query here

```

# Add A Second Label to a Node
```
MATCH (s:Student {last_name: 'Bagepalli'})
SET s:TA;
```

# Add a Second Relationship to the TA Node
```
MATCH (ta:Student:TA {last_name: 'Bagepalli'}),
      (c:Course {title: 'cloud'})
CREATE (ta)-[:TA_FOR]->(c);
```


# Clean Up the Database
```
MATCH (n)
WHERE n:Course OR n:Instructor OR n:Student OR n:TA
DETACH DELETE n;
```