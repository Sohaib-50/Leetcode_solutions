class Solution {
public:
    int countTriples(int n) {
        int count = 0, c_squared, potential_c;

        for (int a = 1; a <= n; a++) {
            for (int b = a; b <= n; b++) {
                c_squared = (a * a) + (b * b);
                
                potential_c = std::sqrt(c_squared);

                if (((potential_c * potential_c) == c_squared) && (potential_c <= n)) {
                    count += 2;
                }
            }
        }

        return count;
    }
};
