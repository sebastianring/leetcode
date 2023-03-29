void rotate(int **matrix, int matrixSize, int *matrixColSize) {
  int halfLength = (matrixSize - 1);
  printf("halfLength is equal to: %i \n", halfLength);
  int basePositions[4][2] = {{0, matrixSize - 1},
                             {*matrixColSize - 1, matrixSize - 1},
                             {*matrixColSize - 1, 0},
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
  }
};
