# Create Courses
```
CREATE (:Class {title: 'advdb'}),
       (:Class {title: 'cloud'}),
       (:Class {title: 'devops'});
```

# Create Instructor Node
```
CREATE (:Instructor {first_name: 'Rob', last_name: 'Elliott', email: 'elliot62@purdue.edu'});
```

# Create Relationship Between Instructor and Courses
```
MATCH (i:Instructor {email: 'elliot62@purdue.edu'}),
      (c:Class {title: 'advdb'})
CREATE (i)-[:INSTRUCTOR_FOR]->(c);
```

```
MATCH (i:Instructor {email: 'elliot62@purdue.edu'}),
      (c1:Class {title: 'cloud'}),
      (c2:Class {title: 'devops'})
CREATE (i)-[:INSTRUCTOR_FOR]->(c1),
       (i)-[:INSTRUCTOR_FOR]->(c2);
```