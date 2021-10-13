<p align="center">

  <h1 align="center">ENG1003_w1_9' s report</h1>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
    <li><a href="#Background-of-Path-Planning-to-Aviation-Engineering">Background of Path Planning to Aviation Engineering</a></li>
    <li><a href="#Theory-of-Path-Planning-Algorithm">Theory of Path Planning Algorithm</a></li>
    <li><a href="#Introduction-of-the-Engineering-Tools">Introduction of the Engineering Tools</a></li>
    <li><a href="#Task-1-Methodology-results-and-Discussion">Task 1:Methodology, results and Discussion</a></li>
    <li><a href="#Task-2-Methodology-results-and-Discussion">Task 2:Methodology, results and Discussion</a></li>
    <li><a href="#task-3-Methodology-results-and-Discussion">task 3:Methodology, results and Discussion</a></li>
    <li><a href="#Reflective-Essay">Reflective Essay </a></li>
    <li><a href="#Reference">Reference </a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
# Background of Path Planning to Aviation Engineering


When travelling by air, we may often think: what is the trajectory of the plane in the sky？ how is the plane's route  planned？
This is a graph of global airline data. Under normal circumstances.You can see that there are approximately 100,000 aircraft movements per day, taking off and landing between 6,000 airports.

![This is an image](https://github.com/KeiraXu03/image/blob/main/228e227c81520ac0d7b7af5427e98cb.png)

Path planning is used in different aspects like aviation, robotics, and computer games. It can let an object move to the destination from the starting point by finding a sequence of valid configurations.

In aviation, it is very common to use path planning, pilot needs to do a path plan before each flight in order to make sure the navigation aid is available. Besides, atc needs to find the best use of the crowded airspace through path planning, it can keep safe and try to lower the probability of delay.

Moreover, path planning can bring safety to the aviation industry. Flight safety is the biggest concern in the aviation industry. There are many flight accidents are involved in weather conditions in recent years. It is very normal to observe bad weather conditions during the flight. Good path planning can enhance the efficiency of air traffic management, also it can help the aircraft avoid bad weather conditions, prohibited areas. In addition, a backup plan can also be planned in path planning in order to cope with an emergency situations. Path planning can also find the path which used the least energy cost so it can help the airline to reduce the operation cost, safety and reduce the workload of the pilot and air traffic controller. 

# Theory of Path Planning Algorithm 
  Path planning technology[[1]](#jump6)[[2]](#jump7) has a wide range of applications in many fields. The applications in the high-tech field include: autonomous robots' collision-free actions; UAVs' obstacle avoidance and penetration flight; cruise missiles to avoid radar searches, anti-rebound attacks, and complete burst explosion missions.Applications in daily life are: GPS navigation; road planning based on GIS system; urban road network planning and navigation. Applications in the field of decision management include: vehicle problems in logistics management (VRP) and similar resource management resource allocation problems. Routing issues in the field of communication technology, etc.Basically, all the planning problems that can be topologically formed as a point-line network can be solved by the method of path planning.  
  The core of path planning is the design of algorithms. Path planning algorithms [[3]](#jump8) have received widespread attention. From traditional algorithms to later algorithms developed in combination with bionics, intelligent algorithms have made tremendous progress.Different intelligent algorithms have different characteristics, and their scope and fields are also. Therefore, studying the path planning intelligent algorithm from the characteristics of the algorithm itself and its application is of great significance to the development of path planning technology.  
General steps of path planning
  General path planning problems in the continuous domain, such as dynamic path planning problems of robots and aircraft, etc. The general steps include environment modeling, path search, and path smoothing[[4]](#jump9)[[5]](#jump).  
  **Common path planning algorithms**  
  **（1）Traditional algorithm**  
  Traditional path planning algorithms include: simulated annealing algorithm, artificial potential field method, fuzzy logic algorithm, tabu search algorithm and so on.  
  **（2）Graphics algorithm**  
  Traditional algorithms often have difficult modeling problems when solving practical problems. Graphics methods provide basic modeling methods. However, graphics methods generally have insufficient search capabilities, and they often need to be combined with specialized search algorithms. Graphics methods include: C-space method, grid method, free space method, voronoi diagram method, etc.  
  **（3）Intelligent Bionics Algorithm**  
  When dealing with path planning problems in the context of complex and dynamic environmental information, inspiration from nature can often play a very good role. Intelligent bionics algorithm is the algorithm people discover through bionics research. Commonly used are: ant colony algorithm, neural network algorithm, particle swarm algorithm, genetic algorithm, etc  
  **（4）Other algorithms**  
  There are also some artificially invented algorithms that are widely used because of their excellent characteristics. These algorithms generally have strong path search capabilities and can play a good role in discrete path topology networks.These algorithms include: A* algorithm, Dijkstra algorithm, fallback algorithm, Floyd algorithm, etc.
# Introduction of the Engineering Tools 

## a.Python

### Introduction
Python was founded by Guido van Rossum, who was working at the Dutch Mathematical and Computer Science Research Institute in Amsterdam, and during Christmas 1989, Guido van Rossum, in order to pass the time, decided to develop a new interpretive scripting language as a successor to the ABC language, as an alternative to using the Unix shell and C for system administration, and to take on the responsibility of interacting with the Amoeba operating system and handling exceptions. Interaction and exception handling with the Amoeba operating system [[6]](#jump1)
![python](https://github.com/KeiraXu03/image/blob/main/python.png)
Python reached version 1.0 in January 1994. The main new feature of this release is to include the functional programming tools lambda, map, filter and reduce provided by Amrit Prem[[7]](#jump2)
### What python can do?
* *Python can be used on a server to create web applications.*   
* *Python can be used alongside software to create workflows.*   
* *Python can connect to database systems. It can also read and modify files.*   
* *Python can be used to handle big data and perform complex mathematics.*  
* *Python can be used for rapid prototyping, or for production-ready software development.*  

## b.Github
<img width="400" height="250" src="https://github.com/KeiraXu03/image/blob/main/github2.png"/>
  
### What is Github?
* *A social network and platform for software developers*  
* *A place where people can share code*    
* *Over 65 million users*  
* *Many big companies are using it*  
* *A place to Share, Communicate, Collaborate with others, especially programmers*  

### How GitHubThe GitHub developed？
* *The GitHub platform began development on October 1, 2007.*[[8]](#jump3)  
* *On April 10, 2008, GitHub was officially launched.*  
* *On January 23, 2014, co-founder Tom Preston-Werner took over the position of president from another co-founder, Chris Wanstrath. The latter will also take over the CEO position left by Preston Werner.*  
* *On the evening of June 4, 2018, American technology company Microsoft announced the acquisition of GitHub for $7.5 billion in stocks[[9]](#jump4),[[10]](#jump5).On October 29th, Microsoft's vice president of developer services, Nat Friedman (Nat Friedman) will become the new CEO of GitHub.*  
* *On March 17, 2020, Github announced the acquisition of npm. GitHub has now guaranteed that npm will always be free to use.*
# Task 1 Methodology results and Discussion
## Methodology:
### First,we should find the code which needs to be changed.
**Start and Finish Point:**  
![1](https://github.com/KeiraXu03/image/blob/main/08bc4b5b246daf9f1ddbfa83321f580.png)
****
**Set obstacle positions:**     
![2](https://github.com/KeiraXu03/image/blob/main/b371647410ce3d465af05395a40fb69.png)
****
**Set fuel consuming area and time consuming area:**
![3](https://github.com/KeiraXu03/image/blob/main/6a1f1753efd2a5eb662ab240d4283bb.png)
### Secondly,according to our goal,we change the code:
```python
# start and goal position
    sx = 0.0  # [m]
    sy = 0.0  # [m]
    gx = 50.0  # [m]
    gy = 50.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]
```
****
```python
    # set obstacle positions for group 9
    for i in range(-10, 20): # draw the free border
        ox.append(20.0)
        oy.append(i)

    for i in range(40, 50):
        ox.append(i)
        oy.append(140-2*i)
```
****
```python
# set fuel consuming area
    fc_x, fc_y = [], []
    for i in range(30, 35):
        for j in range(0, 40):
            fc_x.append(i)
            fc_y.append(j)
    
    # set time consuming area
    tc_x, tc_y = [], []
    for i in range(0, 20):
        for j in range(20, 40):
            tc_x.append(i)
            tc_y.append(j)
```
## Result:
<img width="570" height="450" src="https://github.com/KeiraXu03/image/blob/main/task1.gif"/>  

****
**We tried all the data and found that the model PolyU-A380 achieved minimum cost.**

![5](https://github.com/KeiraXu03/image/blob/main/e24b1eae634324769b137ecdd37282e.png)
# Task 2 Methodology results and Discussion
## Methodology:
### First,we use C++ to help us find the possible values of the variables.
<details>
<summary>C++ Code</summary>
```C++
#include<iostream>
using namespace std;
int main()
{
    
    for(int cf=0;cf<=60;cf++)
    {
        for(int ct=0;ct<=60;ct++)
        {
            if(ct-cf<=30&&2*ct-cf>=20&&-4*ct-cf>=-220&&-0.5*ct-cf<=-30)
            cout<<cf<<" "<<ct<<endl;
        }
    }
    return 0; 
}
```
</details>
<details>
  <summary>Operation data</summary>
  <pre><code> 
     10 40
11 38
11 39
11 40
11 41
12 36
12 37
12 38
12 39
12 40
12 41
12 42
13 34
13 35
13 36
13 37
13 38
13 39
13 40
13 41
13 42
13 43
14 32
14 33
14 34
14 35
14 36
14 37
14 38
14 39
14 40
14 41
14 42
14 43
14 44
15 30
15 31
15 32
15 33
15 34
15 35
15 36
15 37
15 38
15 39
15 40
15 41
15 42
15 43
15 44
15 45
16 28
16 29
16 30
16 31
16 32
16 33
16 34
16 35
16 36
16 37
16 38
16 39
16 40
16 41
16 42
16 43
16 44
16 45
16 46
17 26
17 27
17 28
17 29
17 30
17 31
17 32
17 33
17 34
17 35
17 36
17 37
17 38
17 39
17 40
17 41
17 42
17 43
17 44
17 45
17 46
17 47
18 24
18 25
18 26
18 27
18 28
18 29
18 30
18 31
18 32
18 33
18 34
18 35
18 36
18 37
18 38
18 39
18 40
18 41
18 42
18 43
18 44
18 45
18 46
18 47
18 48
19 22
19 23
19 24
19 25
19 26
19 27
19 28
19 29
19 30
19 31
19 32
19 33
19 34
19 35
19 36
19 37
19 38
19 39
19 40
19 41
19 42
19 43
19 44
19 45
19 46
19 47
19 48
19 49
20 20
20 21
20 22
20 23
20 24
20 25
20 26
20 27
20 28
20 29
20 30
20 31
20 32
20 33
20 34
20 35
20 36
20 37
20 38
20 39
20 40
20 41
20 42
20 43
20 44
20 45
20 46
20 47
20 48
20 49
20 50
21 21
21 22
21 23
21 24
21 25
21 26
21 27
21 28
21 29
21 30
21 31
21 32
21 33
21 34
21 35
21 36
21 37
21 38
21 39
21 40
21 41
21 42
21 43
21 44
21 45
21 46
21 47
21 48
21 49
22 21
22 22
22 23
22 24
22 25
22 26
22 27
22 28
22 29
22 30
22 31
22 32
22 33
22 34
22 35
22 36
22 37
22 38
22 39
22 40
22 41
22 42
22 43
22 44
22 45
22 46
22 47
22 48
22 49
23 22
23 23
23 24
23 25
23 26
23 27
23 28
23 29
23 30
23 31
23 32
23 33
23 34
23 35
23 36
23 37
23 38
23 39
23 40
23 41
23 42
23 43
23 44
23 45
23 46
23 47
23 48
23 49
24 22
24 23
24 24
24 25
24 26
24 27
24 28
24 29
24 30
24 31
24 32
24 33
24 34
24 35
24 36
24 37
24 38
24 39
24 40
24 41
24 42
24 43
24 44
24 45
24 46
24 47
24 48
24 49
25 23
25 24
25 25
25 26
25 27
25 28
25 29
25 30
25 31
25 32
25 33
25 34
25 35
25 36
25 37
25 38
25 39
25 40
25 41
25 42
25 43
25 44
25 45
25 46
25 47
25 48
26 23
26 24
26 25
26 26
26 27
26 28
26 29
26 30
26 31
26 32
26 33
26 34
26 35
26 36
26 37
26 38
26 39
26 40
26 41
26 42
26 43
26 44
26 45
26 46
26 47
26 48
27 24
27 25
27 26
27 27
27 28
27 29
27 30
27 31
27 32
27 33
27 34
27 35
27 36
27 37
27 38
27 39
27 40
27 41
27 42
27 43
27 44
27 45
27 46
27 47
27 48
28 24
28 25
28 26
28 27
28 28
28 29
28 30
28 31
28 32
28 33
28 34
28 35
28 36
28 37
28 38
28 39
28 40
28 41
28 42
28 43
28 44
28 45
28 46
28 47
28 48
29 25
29 26
29 27
29 28
29 29
29 30
29 31
29 32
29 33
29 34
29 35
29 36
29 37
29 38
29 39
29 40
29 41
29 42
29 43
29 44
29 45
29 46
29 47
30 25
30 26
30 27
30 28
30 29
30 30
30 31
30 32
30 33
30 34
30 35
30 36
30 37
30 38
30 39
30 40
30 41
30 42
30 43
30 44
30 45
30 46
30 47
31 26
31 27
31 28
31 29
31 30
31 31
31 32
31 33
31 34
31 35
31 36
31 37
31 38
31 39
31 40
31 41
31 42
31 43
31 44
31 45
31 46
31 47
32 26
32 27
32 28
32 29
32 30
32 31
32 32
32 33
32 34
32 35
32 36
32 37
32 38
32 39
32 40
32 41
32 42
32 43
32 44
32 45
32 46
32 47
33 27
33 28
33 29
33 30
33 31
33 32
33 33
33 34
33 35
33 36
33 37
33 38
33 39
33 40
33 41
33 42
33 43
33 44
33 45
33 46
34 27
34 28
34 29
34 30
34 31
34 32
34 33
34 34
34 35
34 36
34 37
34 38
34 39
34 40
34 41
34 42
34 43
34 44
34 45
34 46
35 28
35 29
35 30
35 31
35 32
35 33
35 34
35 35
35 36
35 37
35 38
35 39
35 40
35 41
35 42
35 43
35 44
35 45
35 46
36 28
36 29
36 30
36 31
36 32
36 33
36 34
36 35
36 36
36 37
36 38
36 39
36 40
36 41
36 42
36 43
36 44
36 45
36 46
37 29
37 30
37 31
37 32
37 33
37 34
37 35
37 36
37 37
37 38
37 39
37 40
37 41
37 42
37 43
37 44
37 45
38 29
38 30
38 31
38 32
38 33
38 34
38 35
38 36
38 37
38 38
38 39
38 40
38 41
38 42
38 43
38 44
38 45
39 30
39 31
39 32
39 33
39 34
39 35
39 36
39 37
39 38
39 39
39 40
39 41
39 42
39 43
39 44
39 45
40 30
40 31
40 32
40 33
40 34
40 35
40 36
40 37
40 38
40 39
40 40
40 41
40 42
40 43
40 44
40 45
41 31
41 32
41 33
41 34
41 35
41 36
41 37
41 38
41 39
41 40
41 41
41 42
41 43
41 44
42 31
42 32
42 33
42 34
42 35
42 36
42 37
42 38
42 39
42 40
42 41
42 42
42 43
42 44
43 32
43 33
43 34
43 35
43 36
43 37
43 38
43 39
43 40
43 41
43 42
43 43
43 44
44 32
44 33
44 34
44 35
44 36
44 37
44 38
44 39
44 40
44 41
44 42
44 43
44 44
45 33
45 34
45 35
45 36
45 37
45 38
45 39
45 40
45 41
45 42
45 43
46 33
46 34
46 35
46 36
46 37
46 38
46 39
46 40
46 41
46 42
46 43
47 34
47 35
47 36
47 37
47 38
47 39
47 40
47 41
47 42
47 43
48 34
48 35
48 36
48 37
48 38
48 39
48 40
48 41
48 42
48 43
49 35
49 36
49 37
49 38
49 39
49 40
49 41
49 42
50 35
50 36
50 37
50 38
50 39
50 40
50 41
50 42
51 36
51 37
51 38
51 39
51 40
51 41
51 42
52 36
52 37
52 38
52 39
52 40
52 41
52 42
53 37
53 38
53 39
53 40
53 41
54 37
54 38
54 39
54 40
54 41
55 38
55 39
55 40
55 41
56 38
56 39
56 40
56 41
57 39
57 40
58 39
58 40
59 40
60 40
  </code></pre>
</details>

# task 3 Methodology results and Discussion
## Methodology:
### First,we should find the code which needs to be changed:
* We need to calculate the cost.
* We need to create a minus cost area
### Secondly,according to our goal,we change the code:
**Calculate the cost:** 
```python
# add minus cost in minus cost area
                if self.calc_grid_position(node.x, self.min_x) in self.pc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.pc_y:
                        # print("fuel consuming area!!")
                        node.cost = node.cost + self.Delta_P* self.C_P* self.motion[i][2]
```
****
**Set minus cost area:**
```python
# set minus cost area
    tc_x, tc_y = [], []
    for i in range(0, 20):
        for j in range(20, 40):
            tc_x.append(i)
            tc_y.append(j)
```
## Result:
<img width="570" height="450" src="https://github.com/KeiraXu03/image/blob/main/task3.gif"/>

****
**We found that the cost is under our expectation:**

![5](https://github.com/KeiraXu03/image/blob/main/e24b1eae634324769b137ecdd37282e.png)

# Reflective Essay

# Reference
<span id="jump6">[1]</span> *Cong Yanfeng. Research on path planning method based on rolling optimization principle [D]. Jilin: Jilin University, 2007.*  
<span id="jump7">[2]</span> *Peter Stiles, Ira Glickstein.RoutePlanning[C].IEEE,1991:420-425.*  
<span id="jump8">[3]</span> *Zhang Yongfang, Zhang An, Zhang Zhiyu, et al. Tactical flight path planning algorithm[J]. Journal of Traffic and Transportation Engineering, 20
06 (12) :84-87*  
<span id="jump9">[4]</span> *Xu Peipei. Research on global path planning algorithm of mobile robot in complex dynamic environment. [D]. Beijing: Beijing University of Posts and Telecommunications, 2009*  
<span id="jump10">[5]</span> *Wang Tao.Robot path planning and simulation system based on ant colony algorithm[D]. Xi'an: Xi'an University of Science and Technology, 2009.*
<span id="jump1">[6]</span> *Why was Python created in the first place?. Python FAQ. [2007-03-22].*     
<span id="jump2">[7]</span> *van Rossum, Guido. The fate of reduce() in Python 3000. Artima Developer. [2007-03-22].*    
<span id="jump3">[8]</span> *Weis, Kristina. GitHub CEO and Co-Founder Chris Wanstrath Keynoting Esri’s DevSummit!. 2014-02-10 [2015-07-02].*  
<span id="jump4">[9]</span> *Lee. Microsoft buys Github code-sharing site for $7.5bn. BBC News. 2018-06-04 [2018-06-06].*       
<span id="jump5">[10]</span> *defunkt. A bright future for GitHub. The GitHub Blog. 2018-06-04 [2018-06-06].*  

