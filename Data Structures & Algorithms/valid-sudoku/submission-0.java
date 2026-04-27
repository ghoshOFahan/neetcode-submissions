class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] squares = new int[9];

        for(int r=0;r<9;r++)
        {
            for(int p=0;p<9;p++)
            {
                if(board[r][p]=='.')
                {
                    continue;
                }
                int val = board[r][p] - '1';
                if((rows[r] & (1<<val))>0 || (cols[p] & (1<<val))>0 ||(squares[(r/3)*3+(p/3)] & (1<<val))>0)
                {
                    return false;
                }
                rows[r] |= (1<<val);
                cols[p] |= (1<<val);
                squares[(r/3)*3+(p/3)] |=(1<<val);
            }
        }
        return true;
    }
}
