class Solution {
public:
    map<pair<int,int>, int> costs_memo;

    int dp(int low, int high) {
        if (low >= high) {
            return 0;
        }

        if (costs_memo.contains({low, high})){
            return costs_memo[{low, high}];
        }
        
        int min_current_step_cost = INT_MAX;
        int current_cost, left_side_cost, right_side_cost;
        for (int i=low; i<=high; i++) {

            left_side_cost = dp(i + 1, high);
            right_side_cost = dp(low, i - 1);
            if (left_side_cost > right_side_cost) {
                current_cost = i + left_side_cost;
            }
            else {
                current_cost = i + right_side_cost;
            }
            if (current_cost < min_current_step_cost) {
                min_current_step_cost = current_cost;
            }
        }

        costs_memo[{low, high}] = min_current_step_cost;
        return min_current_step_cost;
    }


    int getMoneyAmount(int n) {
        // Approach 2, minmax (using dp)

        return dp(1, n);

        // End of Approach 2

        // /*
        // Idea 1: (Update: Doesn't work.)
        // Binary search needed definitely to guess in min tries. 
        // We need to find min amount of money to guaruntee a win, and money is cost on each guess. 
        // SO firstly we can minimize money by doing less amount of guesses.
        // Secondly, the fact we dont know what guesses would be needed,
        // we'll be considering max guess amount on each step to be on safe side, to guarunete a win.
        // This basically means going to right side on each  binary search step.
        // Every time we MOVE, we add the guess of previous step till we cant move.
        // */

        // int money_spent = 0;
        // int low = 1;
        // int high = n;
        // int mid;

        // while (low < high) {
        //     mid = low + ((high - low) / 2);
        //     money_spent += mid;
        //     cout << "Spending $" << mid << endl;
        //     low = mid + 1; 
        // }

        // return money_spent;
    }
};
