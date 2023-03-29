#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char *s) {
  int length = strlen(s);
  int currentSeqLength = 0;
  int recordSeqLength;
  int latestRepetition = 0;

  if (length > 0) {
    recordSeqLength = 1;
  } else {
    recordSeqLength = 0;
  }

  for (int i = 0; i < length; i++) {
    int j = latestRepetition;
    while (j < i) {
      printf("I: %i, J: %i, currentSeqLength %i \n", i, j, currentSeqLength);
      if (s[i] == s[j]) {
        currentSeqLength = i - j - 1;
        latestRepetition = j + 1;
        printf("LATEST REP SET TO: %i \n", j);
        break;
      }
      j++;
    }

    currentSeqLength += 1;
    printf("I: %i, J: %i, currentSeqLength %i \n", i, j, currentSeqLength);
    if (j + 1 == length && length > 1) {
      /* currentSeqLength += 1; */
    }

    if (currentSeqLength > recordSeqLength) {
      recordSeqLength = currentSeqLength;
    }
  }

  return recordSeqLength;
}

int main() {
  int myint = 0;

  char *tests[7] = {"abcabcbb", "pwwkew", "", "dvdf", " ", "au", "cdd"};
  int testResult[7] = {3, 3, 0, 3, 1, 2, 2};

  const int testsLength = sizeof(tests) / sizeof(tests[0]);

  for (int i = 0; i < testsLength; i++) {
    printf("ITERATION #%i ------------- \n", i);
    int result = lengthOfLongestSubstring(tests[i]);
    printf("Result of test #%i , %s, was %i and the expected was: %i \n", i + 1,
           tests[i], result, testResult[i]);
  }

  return 0;
}
