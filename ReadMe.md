# LeetCode 2360. Longest Cycle in a Graph
## 題目
![image](https://user-images.githubusercontent.com/111077328/214656421-c593c9da-0de3-42ce-affb-49391e56323a.png)
### 例子1
![image](https://user-images.githubusercontent.com/111077328/214656699-ef42fd1b-5687-474b-abc2-ec3f87da2ccd.png)
![image](https://user-images.githubusercontent.com/111077328/214656761-a4053fb0-ba85-4960-ae8c-6fb766c82460.png)

## 思路
題目要去找**有向圖**中最長的環，因為是每個點最多指向1個點。當進行DFS走訪時，
如果途中經過已走訪的路徑就代表這是一個環，而走訪過程中記錄經過點當時的步數，如
果重複走到這個點，就將現在的步數減去上次的步數就是環的長度

![image](https://user-images.githubusercontent.com/111077328/214663173-dcda0f02-4d6a-4210-8681-c6c1260ddfce.png)
每次走訪透過passed紀錄當次走訪過的路，travel_step紀錄走訪時的步數，
如果當passed走過時就代表為環，算出步數記錄後跳出，
只有當travel_step為0的點要進行DFS，因為代表這點所連成的區從未走過，而當DFS到travel_step不為0的點就跳出
，因為再走下去也不會影響環的大小
因為資料很大所以不用遞迴走訪，且僅透過一條陣列重複紀錄每次DFS經過的路徑
