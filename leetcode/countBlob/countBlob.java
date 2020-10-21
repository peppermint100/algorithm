package Main;

public class solution {
    public static void main(String[] args) {
        int[][] map = { { 1, 0, 0, 0, 0, 0, 0, 1 }, { 0, 1, 1, 0, 1, 1, 0, 1 }, { 0, 0, 0, 0, 0, 0, 0, 1 },
                { 0, 1, 0, 0, 1, 0, 0, 0 }, { 0, 1, 1, 1, 0, 0, 1, 1 }, { 0, 1, 0, 0, 0, 1, 0, 1 },
                { 0, 0, 0, 1, 0, 0, 0, 1 }, { 0, 1, 1, 1, 0, 1, 0, 0 } };

        Blob blob = new Blob(map);
        System.out.println(blob.countBlob(7, 2));

    }
}

class Blob {
    private int[][] map;
    private final int EMPTY = 0;
    private final int BLOB = 1;
    private final int COUNTED = 2;

    public Blob(int[][] map) {
        this.map = map;
    }

    public int countBlob(int x, int y) {
        // check if it's valid block(overranged blob check)
        if (x < 0 || y < 0 || x >= 8 || y >= 8) {
            return 0;
        }
        // check if it's empty or already counted block
        else if (map[x][y] != BLOB) {
            return 0;
        } else {
            // if its a blob. paint it as counted one
            map[x][y] = COUNTED;
            // check adjacent blocks
            return 1 + countBlob(x, y - 1) + countBlob(x + 1, y - 1) + countBlob(x + 1, y) + countBlob(x + 1, y + 1)
                    + countBlob(x, y + 1) + countBlob(x - 1, y + 1) + countBlob(x - 1, y) + countBlob(x - 1, y - 1);
        }
    }

    public void printMap() {
        int i, j;
        System.out.println(" ");
        for (i = 0; i < 8; i++) {
            System.out.print("\n");
            for (j = 0; j < 8; j++) {
                System.out.print(" " + map[i][j]);
            }
        }
    }

}