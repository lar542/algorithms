import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

// https://school.programmers.co.kr/learn/courses/30/lessons/42584
public class Solution2_주식가격 {

    public static int[] solution(int[] prices) {

        int[] answer = new int[prices.length];

        for (int i = 0; i < prices.length; i++) {
            for (int j = i + 1; j < prices.length; j++) {
                answer[i]++;
                if (prices[i] > prices[j]) break;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] answer = solution(new int[]{1, 2, 3, 2, 3}); // 4, 3, 1, 1, 0
        for (int i = 0; i < answer.length; i++) {
            System.out.print(answer[i] + " ");
        }
    }
}
