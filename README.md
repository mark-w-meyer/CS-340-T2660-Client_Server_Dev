# CS-340-T2660-Client_Server_Dev
 This repository contains a project involving a Jupyter Dash front-end dashboard with a MongoDB and Python backend.

---------------------------------------------------------
How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

In order to write programs that are maintainable, readable, and adaptable, it is imperative to modularize the program such that the simplest of processes are extracted from the bigger picture into their own functions or classes. This can be implemented using classes, constructors, methods, interfaces or abstractions, encapsulation, polymorphism, and other Object-Oriented principles. For example, when working on the CRUD Python module, the script with all the MongoDB queries were contained within a .py file and housed all the necessary CRUD functions, the database file itself, and authentications to the server. The dashboard was then implemented in its own .ipynb file which imported the script to connect the dashboard to the server housing the database. The advantages of working this way are to provide easy maintenance, bug fixes for the queries, and authentication; furthermore, modularity provides convenient reusability so that these queries can be applied to a different server and a different dashboard without rewriting the entire file. With that said, this is precisely how I could use this CRUD Python module in the future: importing a different spreadsheet, accessing it through a different server, and creating a completely different dashboard that meets the user needs of a different client.

---------------------------------------------------------
How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

Approaching a problem as a computer scientist means looking at the objective, and the overall expected process, pinpointing where you currently reside in that process, and then extracting and implementing the designs, tools, and resources needed to get from that point to the ultimate solution. My approach to this project did not differ much from previous assignments in other courses because the same software development and object-oriented principles still apply. The primary differences were within what tools were used (programming languages, frameworks, data structures) and what designs were implemented, but overall, the objective is still breaking down the big problem into smaller manageable problems to meet user needs. I would use these same techniques and strategies in the future to create databases to meet other client requests being especially sensitive to the nature of the business or industry, the target users/audience, the practicality of the implementation, and the cost and resources involved in that process.

---------------------------------------------------------
What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists engineer and innovate at the speed of the imagination in an industry that consistently stimulates the need to attain the next level. This matters because computer scientists enable technology beyond its original purpose, push the bounds of both hardware and software, and inspire the users who benefit from these products to complete the feedback loop for further innovation. My work on this type of project would help a company, like Grazioso Salvare, do their work better by making their jobs easier and freeing up their time to do things more efficiently which, in turn, provides opportunities to work towards additional user needs. This is the epitome of the cycle that continuously feeds the engineering and innovation of a computer scientist.

---------------------------------------------------------
