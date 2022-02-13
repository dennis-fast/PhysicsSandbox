# Welcome to PhysicsSandbox
PhysicsSandbox is a project, made in the context of the Advanced Software Engineering course of the Master's
program "Data Science" in the winter semester 2021/22.

The app is a small physical simulation, based on [pymunk](http://www.pymunk.org/) library.

The scene is rendered using [pyglet](https://pyglet.readthedocs.io/).

To run the app, you should simply run the **main.py** file.

The scene consists of a sloped plane, above which three different objects can be spawned by the user:
- **LEFT MOUSE BUTTON** creates a rectangle;
- with the **RIGHT MOUSE BUTTON** a circle can be spawned
- with the **SPACEBAR** a triangle is spawned

In the scene, which have gravity, all objects have physical properties and could interact with each other
and with the plane.

The following tasks were considered in the project and are accompanied by the corresponding links:


### 1. Use and understand **Git!**
GitHub was used as the platform for versioning the project and as the interface between the IDE and the
Build Management System.

GitHub was also used for documentation and as preparation for submission.

To keep the GitHub project up to date, two the most useful commands were:
- git commit --all
- git push

### 2. **UML** at least **3** good diagrams. "good" means you can pump it up artificially as written in DDD. You have 10 million $ from me! Please export the pics. I can not install all tools to view them!
For this project, I created 3 diagrams: Use Case, Class and Activity. The diagrams are created in PlantUML and 
the diagram images are updated using build.py everytime the project is build.

- [Use Case Diagram](docs/uml/use_case_diagram.png) shows the possible actions the user may choose from.
- [Class Diagram](docs/uml/class_diagram.png) shows the Physics Engine classes and interaction between the App
and the classes for the objects from the physics engine.
- [Activity Diagram](docs/uml/activity_diagram.png) shows the sequence of commands in the app, 
including the event handler, which intercepts and processes all possible events. As a proof-of-concept,
the mouse clicks and keystrokes were implemented, which result in the creation of objects at the cursor position.


### 3. **DDD** If your domain is too small, invent other domains around and document these domains (as if you have 10 Mio € from Edlich-Investment!) Develop a clear strategic design with mappings/relationships with 5-0 Domains. It would be nice if these domains are derived from an Event-Storming (but not mandatory).
To model the possible application domains of the PhysicsEngine, I created
[Core Domain Charts](docs/ddd/core_domain_chart.jpg), which should help to visualise the strategic importance
of each (sub)domain or business capability in the architecture allowing you to make business model-aligned
architectural decisions.


### 4. **Metrics** at least two. Sonarcube would be great. Other non trivial metrics are also fine.
In order to check the metrics of the code, I've installed Sonarqube via Docker and created custom project.

Applying Sonarqube on the project, I've got the following results:
[Sonarqube results](docs/metrics/sonarqube_results.png)

As the end, of project has:
- 0 Bugs 
- 0 Vulnerabilities
- 0 Code Security Hotspots
- 2 Code Smells (empty methods, created by PyBuilder)
- 10 min of Technical Debt (due to empty methods)
- 25.5% Duplications on 1.9k Lines, 12 Duplicated Blocks.

[Duplicated Blocks](docs/metrics/sonarqube_duplicated_blocks.png) were created by PyBuilder during the build process.

In the first run, there were 8 Code Smells, which could be instantly improved.


### 5. **Clean Code Development:** at least **5** points you can show me + >>10 points on your **personal cheat sheet**
My personal CCD cheat sheet (can be found [here](docs/clean_code/personal_cheatsheet.pdf)) was based on
[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

The most useful tips were:
- To improve readability, limit lines to 79 characters
- For the operators with different priorities, add whitespace around the operators with the lowest priority(ies),
as for example, there is no whitespace between negative sign as the variable and whitespace around multiplication
and division signs: [example](src/main/python/physics_engine/triangle.py#L39-L43)
- Always surround assignments and comparisons by whitespace: [example](src/main/python/physics_engine/triangle.py#L26)
- Don't use spaces around the = sign when used to indicate a keyword argument, or when used to indicate
a default value for an unannotated function parameter: [example](src/main/python/physics_engine/triangle.py#L26)
- CapWords convention for the classes: [example](src/main/python/physics_engine/triangle.py#L6)
- Function names should be lowercase, with words separated by underscores:
[example](src/main/python/physics_engine/triangle.py#L39)


### 6. **Build Management** with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough). Do e.g. generate Docs, call tests, etc.
Since my project is written in Python, I used PyBuilder as a Build Management Tool.

Using PyBuilder, I was able to generate [UML diagrams](docs/uml) using [PlantUML](https://plantuml.com/),
to call [unittests](src/unittest/python) and to keep the required packages in the state that the project
is properly working (using [requirement file](requirements.txt)).

[Here](docs/build_management_system/pybuilder_successful_build.png) you can see successful build using PyBuilder.


### 7. Integrate some nice **Unit-Tests** in your Code to be integrated into the Build
I've created some unit tests for each physical object to test the correct creation and movement of the objects, 
for example [here](src/unittest/python/circle_tests.py) is a set of unittests for a circle.


### 8. **Continuous Delivery:** show me your pipeline in e.g. Jenkins, Travis-CI, Circle-CI, GitHub Action, GitLab CI, etc.
I've used Jenkins for the Continuous Delivery.

First, I created a workspace on the platform on Built-In Node:
[screenshot](docs/coninuous_delivery/jenkins_workspace.png)

I've installed Jenkins via Docker and linked the workspace to GitHub:
[screenshot](docs/coninuous_delivery/jenkins_github_connection.png)

Since the build and unittests are running on PyBuilder, I only need to call **pyb** to trigger build running and notify
me if the build is unsuccessful via e-mail: [screenshot](docs/coninuous_delivery/jenkins_pipeline.png)

You can see successful build using Jenkins [here](docs/coninuous_delivery/jenkins_successful_build.png).


### 9. Use a good **IDE** and get fluent with it as e.g. IntelliJ. What are your favorite **Key-Shortcuts**?!
  
I've used **PyCharm** for the project, since it has very clean interface and many nice features.

My favorite **Key-Shortcuts** are:
- CTRL + / for block comment
- SHIFT + F10 for running the app
- CTRL + D for line duplication


### 10. **DSL** Create a small DSL Demo example snippet in your code even if it does not contribute to your project
To learn domain-specific language patterns, I created a [small Python script](wiki_links.py), which scrapes internal
links from any given **Wikipedia webpage** itself in the first iteration, as well as all internal links from each Wiki
web page linked to the initial web page in the second iteration. To compile the links in the correct way,
I used regular expression as DSL.


### 11. **Functional Programming** (prove that you have covered all functional aspects in your code.
For this task, I created [another small Python script](func_programming.py), which consists of three parts:
- anonymous function for filtering odd numbers from a given list and squaring them;
- higher-order function for tracing intermediate steps of a recursive function;
- recursive function itself, which calculates x to the power of n.

Hereby, I followed the main rules for functional programming:

- use only final data structures;
- create side effect free functions;
- use of higher-order functions (trace);
- use functions as parameters and return values (in the recursive function);
- use closures / anonymous functions (filter and map).