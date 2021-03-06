
<p align="center">

  <h1 align="center">ENG1003_w1_9' s report</h1>
  
# Presentation Link:
 https://www.youtube.com/watch?v=Rl_fJXkXYFs
 
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
    <li><a href="#Background-of-Path-Planning-to-Aviation-Engineering">Background of Path Planning to Aviation Engineering</a></li>
    <li><a href="#Theory-of-Path-Planning-Algorithm">Theory of Path Planning Algorithm</a></li>
    <li><a href="#Introduction-of-the-Engineering-Tools">Introduction of the Engineering Tools</a></li>
    <li><a href="#Task-1-Methodology-results-and-Discussion">Task 1:Methodology, results and Discussion</a></li>
    <li><a href="#Task-2-Methodology-results-and-Discussion">Task 2:Methodology, results and Discussion</a></li>
    <li><a href="#task-3-Methodology-results-and-Discussion">task 3:Methodology, results and Discussion</a></li>
    <li><a href="#Additional-Task-1">Additional Task 1</a></li>
    <li><a href="#Additional-Task-2">Additional Task 2</a></li>
    <li><a href="#Reflective-Essay">Reflective Essay </a></li>
    <li><a href="#Reference">Reference </a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
# Background of Path Planning to Aviation Engineering[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)
When travelling by air, we may often think: what is the trajectory of the plane in the sky？ how is the plane's route  planned？
This is a graph of global airline data. Under normal circumstances.You can see that there are approximately 100,000 aircraft movements per day, taking off and landing between 6,000 airports.

![This is an image](https://github.com/KeiraXu03/image/blob/main/228e227c81520ac0d7b7af5427e98cb.png)


Path planning is used in different aspects like aviation, robotics, and computer games. It can let an object move to the destination from the starting point by finding a sequence of valid configurations.

Path planning is common in aviation, pilots carry out path planning before each flight to ensure safety, fuel efficiency according to the airport standard departing/arriving procedures (STAR/SID) in the aeronautical information publication. With a proper path plan with a highly efficient air traffic control the airspace of the Flight information region could be utilized allowing higher traffic volume and more available slots with safety as its top priority.

Froma airline perspective ,with navigation technology advancing different new procedures are included in path planning to reduced separation,shorter and direct pathing to achieve higher efficency.One example of these procedures is the required navigation performance authorization required approach (RNP AR APCH) which allows aircraft operations on their desired flight path with position determined continuously on its own rather than tracked by ground navigational aids like DME/VOR.With RNAV together with GNSS aircraft positioning is significantly increased the accuracy up to 95% ,with this the flight path could be shortened and directed increasing fuel efficiency and traffic capacity.

On the other hand from ATC perspective, path planning is crucial in maintaining efficient use of airspace with balance public interest as aircraft operations produces noise to the surrounding community.Therefore when constructing flight path (SID/STAR) in AIP noise mitigations measures are taken into account following ICAO guidelines. Take Hong Kong as example ,aircraft operations between 11pm to 7am departing east are required to deviate south to the southern district to avoid noise disturbance to the populated areas in both sides of the victoria harbour.

Moreover, path planning can bring safety to the aviation industry. Flight safety is the biggest concern in the aviation industry. There have been many flight accidents involving weather in recent years. It is very normal to observe bad weather conditions during the flight. Good path planning can enhance the efficiency of air traffic management, also it can help the aircraft avoid bad weather conditions, prohibited areas. In addition, a backup plan can also be planned in path planning in order to cope with an emergency situation. Path planning can also find the path which uses the least energy cost so it can help the airline to reduce the operation cost, safety and reduce the workload of the pilot and air traffic controller. 

# Theory of Path Planning Algorithm [![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)

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
  
# Introduction of the Engineering Tools [![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)

## a.Python

### Introduction
Python was founded by Guido van Rossum, who was working at the Dutch Mathematical and Computer Science Research Institute in Amsterdam, and during Christmas 1989, Guido van Rossum, in order to pass the time, decided to develop a new interpretive scripting language as a successor to the ABC language, as an alternative to using the Unix shell and C for system administration, and to take on the responsibility of interacting with the Amoeba operating system and handling exceptions. Interaction and exception handling with the Amoeba operating system [[6]](#jump1)

It is a high-level programming language that is easy to learn and read. One of the main ideas of python is “simple”. This main idea can lower the maintenance cost of the program. The most important thing is python is free of charge to all major platforms.
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

# Task 1 Methodology results and Discussion[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)
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
| Aircraft Model   |CF      | Delta F | CT     |Delta T |Cc       |Fa      |Ta      | Total cost|
| :-----:          | :----: | :-----: | :----: | :----: | :-----: | :----: | :----: |  :----:   |
| PolyU-A380   | 1 | 1 | 2   | 5 | 10 |0.2  | 0.2 | 1626.62 |
| PolyU-A381   | 1 | 1.5 |3   | 5 | 10 |0.3   | 0.4 | 2053.09 |
| PolyU-A382   | 1 | 2.0 |4   | 5 | 10 |0.4   | 0.5 | 2479.41 | 
| PolyU-A383   | 1 | 2.5|5   | 5 | 10 |0.5   | 0.1 |  2866.33|
****
**We tried all the data and found that the model PolyU-A380 achieved minimum cost.**

![5](https://github.com/KeiraXu03/image/blob/main/e24b1eae634324769b137ecdd37282e.png)
****
# Task 2 Methodology results and Discussion [![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)
## Methodology:
### First,we use C++ to help us find the possible values of the variables.
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
**Running results:**
![111](https://github.com/KeiraXu03/image/blob/main/8b27c4d9add61ab4ca111a08374b472.png)
****
**Then we add the resulting data to the code**
```python
# you could modify the setup here for different aircraft models (based on the lecture slide) #
        self.C_F = 20
        self.Delta_F = 5
        self.C_T = 20
        self.Delta_T = 5
        self.C_C = 10
        
        self.Delta_F_A = 5 # additional fuel
        self.Delta_T_A = 5 # additional time 
```
****
**_By trying we found that when both variables are taken as 20, the total cost is the least_**
![222](https://github.com/KeiraXu03/image/blob/main/cc33451acef9a2f1845fe5a9ff757d2.png)
****

# task 3 Methodology results and Discussion[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)
## Methodology:
### First,we should find the code which needs to be changed:
* We need to calculate the cost.
* We need to create a minus cost area
### Secondly,according to our goal,we change the code:
**Add variables**
```python
       self.Delta_F_A = 0.2 # additional fuel
        self.Delta_T_A = 0.2 # additional time 
```
****
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
        pc_x, pc_y = [], []
    for i in range(0, 16):
            pc_x.append(i)
            pc_y.append(i)
```
## Result:
<img width="570" height="450" src="https://github.com/KeiraXu03/image/blob/main/task3.gif"/>

****
**We found that the cost is under our expectation:**

![5](https://github.com/KeiraXu03/image/blob/main/e24b1eae634324769b137ecdd37282e.png)
****
# Additional Task 1
## Methodology:
**Addition task is more difficult than any other task,so we need to figure out what is the order in which the program runs**
****
**conduct the main function**
```python
if __name__ == '__main__':
    main()
```
****
**The next step is to set obstacles and color the points, which is omitted here.**
****
**The most important part:use class:AStarPlanner
```python
a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)
```
****
**And finally, the graph function**
```python
    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-r") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.show() # show the plot
```
**What we should do is only to change the main function
```python
def main():
    print(__file__ + " start the A star algorithm demo !!") # print simple notes

    # start and goal position
    sx = 0.0  # [m]
    sy = 0.0  # [m]
    gx = 10.0  # [m]
    gy = 30.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]
    ox, oy = [], []
    for i in range(-10, 60): # draw the button border 
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 60): # draw the right border
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60): # draw the top border
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60): # draw the left border
        ox.append(-10.0)
        oy.append(i)

    for i in range(-10, 20): # draw the free border
        ox.append(20.0)
        oy.append(i)

    for i in range(40, 50):
        ox.append(i)
        oy.append(140-2*i)
    
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

    if show_animation:  # pragma: no cover
        plt.plot(fc_x, fc_y, "oy") # plot the fuel consuming area
        plt.plot(tc_x, tc_y, "or") # plot the time consuming area
        plt.plot(ox, oy, ".k") # plot the obstacle
        plt.plot(0, 0, "or") # plot the start position 
        plt.plot(10,30, "oy") # plot the end position
        plt.plot(32,20, "og")
        plt.plot(50,50, "xb")
        plt.grid(True) # plot the grid to the plot panel
        plt.axis("equal") # set the same resolution for x and y axis 

    a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)
    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-b") # show the route 
        plt.pause(0.001)
        plt.plot(0, 0, "or") # plot the start position 
        plt.plot(10,30, "oy") # plot the end position
        plt.plot(32,20, "og")
        plt.plot(50,50, "xb")# pause 0.001 seconds
       ## plt.show() # show the plot
    sx = 10.0  # [m]
    sy = 30.0  # [m]
    gx = 32.0  # [m]
    gy = 20.0  # [m]
    rx, ry = a_star.planning(sx, sy, gx, gy)
    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-b") # show the route 
        plt.pause(0.001) 
        plt.plot(0, 0, "or") # plot the start position 
        plt.plot(10,30, "oy") # plot the end position
        plt.plot(32,20, "og")
        plt.plot(50,50, "xb")# pause 0.001 seconds
    sx = 32.0  # [m]
    sy = 20.0  # [m]
    gx = 50.0  # [m]
    gy = 50.0  # [m
    rx, ry = a_star.planning(sx, sy, gx, gy)
    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-b") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.plot(0, 0, "or") # plot the start position 
        plt.plot(10,30, "oy") # plot the end position
        plt.plot(32,20, "og")
        plt.plot(50,50, "xb")# pause 0.001 seconds
        plt.show() # show the plot
```
## result
<img width="570" height="450" src="https://github.com/KeiraXu03/image/blob/main/task4.gif"/> 

# Additional Task 2
## Methodology:
### Modify the code so that:
* **Only the fuel-consuming area remains and generate it randomly with a fixed area (30x30)**  
**solution:**
```python
fc_x, fc_y = [], []
    r_fc_x = random.randrange(-9, 31)
    r_fc_y = random.randrange(-9, 31)
    for i in range(r_fc_x, r_fc_x+30):
        for j in range(r_fc_y, r_fc_y+30):
            fc_x.append(i)
            fc_y.append(j)
```
****
* **Diagonal movement is disabled, change parameter(s) so that the object could travel within one grid size**  
**solution:**
travel within one grid size:
```python
    grid_size = 1  
    robot_radius = 0  
```
**Diagonal movements are disabled:**
```python
@staticmethod
    def get_motion_model(): 
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1]]
```
****
* **Obstacles are generated randomly with reasonable density**
**solution:**
```python
for i in range(0,1200):#Based on several attempts, we found that the density is appropriate when the number of obstacles is 1200
        g1=random.randrange(-9, 60)
        g2=random.randrange(-9, 60)
        if((abs(g1-sx)<=3 and abs(g2-sy)<=3 ) or (abs(g1-gx)<=3 and abs(g2-gy)<=3)):
            continue
        ox.append(g1)
        oy.append(g2)
```
****
* **Destination and starting points are generated randomly with at least a 50-unit distance in-between**
**solution:**
```python
while True:
        sx = random.randrange(-10, 59)  # [m]
        sy = random.randrange(-10, 59)  # [m]
        gx = random.randrange(-10, 59)  # [m]
        gy = random.randrange(-10, 59)  # [m]
        if (gx-sx) >= 50 or (sx-gx) >= 50 or (gy-sy) >= 50 or (sy-gy) >= 50:
            break
```
* **Plotting of the fuel-consuming area would not cover the obstacles, and obstacles should not generateat/near the start and end poin**
**solution:**
```python
for i in range(0,1200):
        g1=random.randrange(-9, 60)
        g2=random.randrange(-9, 60)
        if((abs(g1-sx)<=3 and abs(g2-sy)<=3 ) or (abs(g1-gx)<=3 and abs(g2-gy)<=3)):##obstacles should not generateat/near the start and end poin
            continue
        ox.append(g1)
        oy.append(g2)
```
****
# result:
**Since maps and paths are generated randomly, we only include three representative maps here**  
**FIG. 1**

<img width="570" height="450" src="https://github.com/KeiraXu03/image/blob/main/task5-1.gif"/> 

**FIG. 2**

<img width="570" height="450" src="https://github.com/KeiraXu03/image/blob/main/task5-2.gif"/> 

**FIG. 3**

<img width="570" height="450" src="https://github.com/KeiraXu03/image/blob/main/task5-3.gif"/> 

# Reflective Essay[![111](https://img.shields.io/badge/Back-readme1.0.0-cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)
### 1 (XU,Zhuoning 21101256d)
In this project, I served as the group leader, mainly responsible for the assignment of work within the group and the integration of students' codes.    
This class made me realize the importance of path planning for aerospace. It is hard to imagine what our lives would be like without path planning. In fact, with the development of transportation, to increase the capacity and transportation efficiency, proper path planning is the key. This can improve the efficiency of transportation and reduce the occurrence of accidents at the same time
Additional task is the section I am mainly responsible for. The teacher's explanation made me understand that when we meet a new problem, we don't need to write the code from scratch. Instead, we can download the relevant code from GitHub and modify it to get the program we want.In the first additional task due to the wrong idea, I spent a week or so on this think nothing, and then by chance it occurred to me that I only need to modify the main function.This incident made me realize that when we facing some problems that can't be solved,we can change our thoughts and maybe we will find the answer to the question.
Another challenge we meet is the Additional task 2.This task requires more code changes than any other task, and the task requirements are complex.One of the codes for the random starting end point and the fuel consumption area was written by my group members.His code gave me ideas, and the random number setting part of it I think is very well written.Based on his idea, I designed the code to set random obstacles.
As the leader of our group, I also try to learn how to communicate with my group members. I didn't do all the work by myself but distributed the tasks to the group members and gave everyone a chance to practice.



### 2 (Hui Kwan To 21055999d)
In this project, I am mainly responsible for the short essay part of the assignment, some previous python assignments and provide opinions and support to the group leaders. 

For the background searching work in the short essay, I have to search many academic references and sources and I need to make sure the data is correct and trustable. Also, I need to avoid plagiarism in the short essay. It is not difficult to work for me in this part but for me, python is the hardest part as I am not good at computing knowledge. Everything needs to study again. I usually watch YouTube and my group leader to seek help if I have any difficulties during the assignment.

AAE freshman project is the first project that I had in my university school life. Therefore, I have many things need to learn during the project such as how to work with my groupmate, how to commutate with them, etc. Luckily, my groupmates are very nice to me, willing to share their experience and help each other. For an ae student, I am fortunate for doing the AAE freshman project, because this project is something related to aviation which I will be interest in it. Path planning is one of the interesting topics to me, as I wanted to become an air traffic controller in the future. Studying path planning can also study the distribution of the airspace and navigation system.

During this project, I understand that engineer is not just about components and work. We have to learn python and 3D CAD as well which are used to design an aircraft. Besides, I know the GitHub software through this project. Before this project, I don’t know GitHub and python can be used in flight control software for UAVs, aviation services engineering, logistics, and facility management, machine learning for data analysis, aeronautical engineering, aircraft maintenance, and navigation and positioning.

### 3 (HU Yuxin 21102506d)
AAE project provides us a chance to work with the group and let me meet many excellent groupmates.It enlighten me on path planning and programming.I have learned a lot during the project and enjoy this very much.  
My work are searching related information and makeing suggestions to the group leader.Due to the problem of my computer,l had not do programming work and it is really a pity.I got information bilibili and academic paper website.Our group leader is hardworking and do the main work.I think the he took on most of the challenges so that i think i did't meet challenge during the project.Although my work assigned to me is easy, l still learned something.Github let me learn how can people work together from all over the world.Everyone benefits from sharing of sources.Through the teacher's explanation and   operation，i realize the role of path in saving time and improving safety in transportation Besides,l learned how to work together with the group.Because of everyone’s communication, we got a lot of useful information.  
This project let me recognize the charm of programming. it is the beginning of my learning programming and i will learn more in the future to solve more problems with it.Finally,thanks to everyone' efforts to make our work better and lookiing forward to to future cooperation。

### 4 (Chau Chun Pong Mat,21031576D )

This AAE freshman project is very interesting for me, with no previous python or any coding experiences for me in my secondary times,AAE project introduces me to this new world of coding. I have learned a lot about python and how it works.
My main task in this is responsible for some short essays and doing research on flight path planning and supporting the group leader.

For searching on the topic over path planning ,I found out that pilot does not fly the aircraft blindly or freely in the skies but they have to strictly following the navigational aids on the ground and fly accordingly to the standard instrument arrival procedures/standard instrument departure procedures  (STAR/SID) to allow an efficient use of airspace, slot and most importantly ensuring safety and efficiency. I now know that with advances in technology the guidance of flight safety is behind such as the GNSS . Moreover, I learnt more on the work of air traffic control on the working principle behind such as the sequencing method, the standard and on how to increase the capacity while ensuring safety. Furthemore, I learnt that different methods of aircraft planning are used to mitigate noise to the surrounding environments such as the noise mitigating SID/STAR procedures apply to aircraft arriving and departing in Hong Kong. The project enables me to not learn about python but more on the ATC procedures, deepening my understanding and curiosity over the work of ATC and inspiring me to work as air traffic controller in the future.

The main challenges I face is language barrier with my group mates since my mandarin is not good,but they are still willing to communicate and continue to teach me accordingly . They are very helpful and nice in sharing their understanding of python with me even though I still don't understand how it works  sometimes.

All in all , I truly enjoy this freshman project and I learnt a lot both on path planning and on python. Thanks to my groupmate once again and I am looking forward to discovering more on python in my studies.


### 5 (Arshad Asaad 21102596d)
The AAE freshman project for me was a very knowledgeable project. Before coming to university, I had learned a bit of python from IT class. But I never actually learned anything, I only memorized the words that would be used in tests and examinations. The AAE freshman project teacher gave us tasks and freedom to do our tasks however we wanted. The teachers would help us with any problems we had. The tasks given to me by the team leader were not too difficult. I did not know how to complete the programming, so I had to self-learn from online guides just as the teacher had told us. I found self-learning to be very helpful. It made the knowledge I learned stick in my brain and I have not forgotten it. I think this opportunity to self-learn has been the most valuable thing I have learned from the AAE freshman project. I now know the benefits of self-learning, which I find will be very useful in my future. 
Github is very interesting, in the fact that it allows people across the world to remotely work together. I think it is very useful, and I am glad to have learned of it. The path planning programme I had to do was very fun to do. I found that it was challenging but I had fun facing the challenge. 
One part I think I can improve upon is cooperation, I was not very involved with the group. I did finish the parts I was given, but I think I could have done more. The group leader was very good at his role.
I will continue to learn programming, and absorb more knowledge. I hope there will be challenging yet fun programming tasks in the future for me to complete.

****
# Reference[![Join the chat at https://gitter.im/guodongxiaren/README](https://img.shields.io/badge/Back-readme1.0.0-cyan.svg)](https://github.com/KeiraXu03/ENG1003_w1_9/blob/main/README.md)
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

