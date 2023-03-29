#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void rotate(int **matrix, int matrixSize, int *matrixColSize) {
  for (int i = 0; i < matrixSize; i++) {
    for (int j = 0; j < *matrixColSize; j++) {
      printf("Array val: %i at %i %i \n", matrix[i][j], i, j);
    }
  }
  for (int ctr1 = 0; ctr1 < matrixSize; ctr1++) {
    for (int ctr2 = 0; ctr2 < *matrixColSize; ctr2++) {
      printf("[%i]", matrix[ctr1][ctr2]);
    }
    printf("\n");
  }

  int length = (matrixSize - 1);
  int levels = (matrixSize / 2);
  printf("halfLength is equal to: %i \n", length);
  int basePositions[4][2] = {{0, matrixSize - 1},
                             {*matrixColSize - 1, matrixSize - 1},
                             {*matrixColSize - 1, 0},
                             {0, 0}};
  int targetCarry;
  int nextx;
  int nexty;

  for (int level = 0; level < levels; level++) {
    for (int i = level; i < length - level; i++) {
      int sourceCarry = matrix[level][i];
      for (int j = 0; j < 4; j++) {
        switch (j) {
        case 0:
          nexty = basePositions[j][0] + i;
          nextx = basePositions[j][1] - level;
          break;
        case 1:
          nexty = basePositions[j][0] - level;
          nextx = basePositions[j][1] - i;
          break;
        case 2:
          nexty = basePositions[j][0] - i;
          nextx = basePositions[j][1] + level;
          break;
        case 3:
          nexty = basePositions[j][0] + level;
          nextx = basePositions[j][1] + i;
          break;
        }

        targetCarry = matrix[nexty][nextx];
        printf("I want to move val: %i to %i, %i where value: %i sits ----- i: "
               "%i j: %i, level: %i \n",
               sourceCarry, nexty, nextx, targetCarry, i, j, level);
        matrix[nexty][nextx] = sourceCarry;
        sourceCarry = targetCarry;
      }
    }
  }

  for (int ctr1 = 0; ctr1 < matrixSize; ctr1++) {
    for (int ctr2 = 0; ctr2 < *matrixColSize; ctr2++) {
      printf("[%i]", matrix[ctr1][ctr2]);
    }
    printf("\n");
  }
}

struct matrix {
  int matrixSize;
  int matrixColSize;
  int **matrix;
  int values;
};

int **allocateMemory(int *matrixSize, int *matrixColSize) {
  int **matrix = (int **)malloc(*matrixSize * sizeof(int *));

  for (int i = 0; i < *matrixSize; i++) {
    matrix[i] = (int *)malloc(*matrixColSize * sizeof(int *));
  }

  return matrix;
};

void populateMatrix(int **matrix, int *matrixSize, int *matrixColSize,
                    int *values) {
  for (int i = 0; i < *matrixSize; i++) {
    for (int j = 0; j < *matrixColSize; j++) {
      matrix[i][j] = *(values + i * *matrixColSize + j);
    }
  }
}

int main() {
  /* ------- data #1 ------------- */
  struct matrix myMatrix1 = {.matrixSize = 3, .matrixColSize = 3};
  int myMatrix1Values[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};

  myMatrix1.matrix =
      allocateMemory(&myMatrix1.matrixSize, &myMatrix1.matrixColSize);
  populateMatrix(myMatrix1.matrix, &myMatrix1.matrixSize,
                 &myMatrix1.matrixColSize, myMatrix1Values);

  /* ------- data #2 ------------- */
  struct matrix myMatrix2 = {.matrixSize = 4, .matrixColSize = 4};
  int myMatrix2Values[] = {15, 13, 2, 5, 14, 4, 8,  1,
                           12, 3,  6, 9, 16, 7, 10, 11};

  myMatrix2.matrix =
      allocateMemory(&myMatrix2.matrixSize, &myMatrix2.matrixColSize);
  populateMatrix(myMatrix2.matrix, &myMatrix2.matrixSize,
                 &myMatrix2.matrixColSize, myMatrix2Values);

  /* ------- end of data---------- */

  struct matrix *tests[2] = {&myMatrix1, &myMatrix2};
  int testResult[2] = {1, 1};

  const int testsLength = sizeof(tests) / sizeof(tests[0]);

  for (int i = 0; i < testsLength; i++) {
    rotate(tests[i]->matrix, tests[i]->matrixSize, &tests[i]->matrixColSize);
  }

  for (int i = 0; i < myMatrix1.matrixColSize; i++) {
    free(myMatrix1.matrix[i]);
  }
  free(myMatrix1.matrix);
  return 0;
}
