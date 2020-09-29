## Recursive

재귀 함수의 조건

1. 재귀 함수의 순환을 멈추게 하는 조건이 존재 해야 한다.(Base code)
2. Base Code로 가기 위한 장치가 존재해서 결국 재귀 함수의 순환을 멈추도록 해야 한다.

## 미로 찾기 알고리즘 아이디어

먼저 길은 0, 벽은 1로 하여 이차원 배열로 미로를 그린다. 그 후 재귀 함수로 길을 찾는다.

미로 찾기 재귀 함수의 Base Code는 자기 자신의 위치가 목적지인지 확인하는 것이다.

그리고 자기 자신의 좌표 중심 상하좌우가 벽인지 방문 했던 좌표면 false를 리턴하고 갈 수 있는 길(0)이면 true를 리턴하여 순환 함수를 돌린다.

```java
public class Main {
    public static void main(String[] args) {
        Maze maze = new Maze();
        maze.printMaze();
        maze.findMaze(0, 0);
        maze.printMaze();
    }
}

class Maze {
    int N = 8;
    int[][] maze = { { 0, 0, 0, 0, 0, 0, 0, 1 }, { 0, 1, 1, 0, 1, 1, 0, 1 }, { 0, 0, 0, 1, 0, 0, 0, 1 },
            { 0, 1, 0, 0, 1, 1, 0, 0 }, { 0, 1, 1, 1, 0, 0, 1, 1 }, { 0, 1, 0, 0, 0, 1, 0, 1 },
            { 0, 0, 0, 1, 0, 0, 0, 1 }, { 0, 1, 1, 1, 0, 1, 0, 0 } };
    int PATHWAY = 0;
    int WALL = 1;
    int BLOCKED = 2;
    int PATH = 3;

    public boolean findMaze(int x, int y) {
        // maze out of range
        if (x < 0 || y < 0 || x >= N || y >= N) {
            return false;
        }
        // maze goal check
        else if (x == N - 1 && y == N - 1) {
            maze[x][y] = PATH;
            return true;
        }
        // maze wall or visited check
        else if (maze[x][y] != PATHWAY) {
            return false;
        }
        // maze pathway check NESW
        else {
            maze[x][y] = PATH;
            if (findMaze(x, y - 1) || findMaze(x + 1, y) || findMaze(x, y + 1) || findMaze(x - 1, y)) {
                return true;
            }
            maze[x][y] = BLOCKED;
            return false;
        }
    }

    public void printMaze() {
        int i, j;
        System.out.println(" ");
        for (i = 0; i < N; i++) {
            System.out.print("\n");
            for (j = 0; j < N; j++) {
                System.out.print(" " + maze[i][j]);
            }
        }
    }
}
```
