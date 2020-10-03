## Problem
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


## Approach
Flood fill 문제와 같은 알고리즘을 사용한다. 스타팅 포인트를 찾고 찾으면 섬이 있다는 뜻이므로 answer에 1을 더해주고 재귀함수로 인접한 1들을
계속 탐색하며 탐색된 1들을 0으로 바꿔준다. 이렇게 하면 다음 1이 새로운 섬의 스타팅 포인트가 된다.

## Complexity
```java

class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[i].length; j++){
                if(grid[i][j] == '1'){
                    count+=1;
                    fill(grid, i, j);
                }
            }
        }
        return count;
    }
    
    public void fill(char[][] grid, int i, int j){
        if(i < 0 || j < 0 || i >= grid.length || j >= grid[i].length || grid[i][j] == '0'){
            return;
        }
        
        grid[i][j] = '0';
        
        fill(grid, i-1, j);
        fill(grid, i+1, j);
        fill(grid, i, j-1);
        fill(grid, i, j+1);
    }
}
```
시간 복잡도는 반복문이 둘이므로 O(ij)가 되고 공간 복잡도 역시 모든 i, j를 탐색하게 되므로 O(ij)가 된다.