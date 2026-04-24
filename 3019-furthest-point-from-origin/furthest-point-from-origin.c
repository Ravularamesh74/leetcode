int furthestDistanceFromOrigin(char* moves) {
    int L = 0, R = 0, U = 0;

   for (int i = 0; moves[i] != '\0'; i++) {
        if (moves[i] == 'L')L++;
        else if (moves[i]== 'R')R++;
        else U++;

    }
    return abs( R - L) + U;
}