#include <stddef.h>
#include <stdio.h>
#include <string.h>

int rotate(int matrixSize, int matrixColSize,
           int matrix[matrixSize][matrixColSize]) {
  for (int ctr1 = 0; ctr1 < matrixSize; ctr1++) {
    for (int ctr2 = 0; ctr2 < matrixColSize; ctr2++) {
      printf("[%i]", matrix[ctr1][ctr2]);
    }
    printf("\n");
  }

  int halfLength = (matrixSize - 1);
  printf("halfLength is equal to: %i \n", halfLength);
  int basePositions[4][2] = {{0, matrixSize - 1},
                             {matrixColSize - 1, matrixSize - 1},
                             {matrixColSize - 1, 0},
                             {0, 0}};
  int targetCarry;
  int nextx;
  int nexty;

  for (int i = 0; i < halfLength; i++) {
    int sourceCarry = matrix[0][i];
    for (int j = 0; j < 4; j++) {
      switch (j) {
      case 0:
        nexty = basePositions[j][0] + i;
        nextx = basePositions[j][1];
        break;
      case 1:
        nexty = basePositions[j][0];
        nextx = basePositions[j][1] - i;
        break;
      case 2:
        nexty = basePositions[j][0] - i;
        nextx = basePositions[j][1];
        break;
      case 3:
        nexty = basePositions[j][0];
        nextx = basePositions[j][1] + i;
        break;
      }

      targetCarry = matrix[nexty][nextx];
      printf("I want to move val: %i to %i, %i where value: %i sits ----- i: "
             "%i j: %i\n",
             sourceCarry, nexty, nextx, targetCarry, i, j);
      matrix[nexty][nextx] = sourceCarry;
      sourceCarry = targetCarry;
    }

    /* add last value to first */
  }

  for (int ctr1 = 0; ctr1 < matrixSize; ctr1++) {
    for (int ctr2 = 0; ctr2 < matrixColSize; ctr2++) {
      printf("[%i]", matrix[ctr1][ctr2]);
    }
    printf("\n");
  }

  return 0;
}

struct matrix {
  int matrixSize;
  int matrixColSize;
  int matrix[3][3];
  int *matrixPtr[3][3];
};

int main() {
  struct matrix myMatrix1 = {.matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},
                             .matrixSize = 3,
                             .matrixColSize = 3};

  int result = rotate(3, 3, myMatrix1.matrix);

  int myMatrix2[4][4] = {
      {5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}};

  int result2 = rotate(4, 4, myMatrix2);

  return 0;
}
