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
