/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int low = 1;
        int high = n;
        int current_guess, guess_res;

        while (5) {
            current_guess = low + (high - low) / 2;
            guess_res = guess(current_guess);
            if (guess_res == 0) {
                break;
            }

            if (guess_res == -1) {
                high = current_guess - 1;
            } 
            else {
                low = current_guess + 1;
            }
        }
        return current_guess;
    }

};
