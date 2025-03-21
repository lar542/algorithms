// https://school.programmers.co.kr/learn/courses/30/lessons/12939
public class Solution1_최댓값과최솟값 {

    public static String solution(String s) {

        String[] words = s.split(" ");

        int max = Integer.parseInt(words[0]);
        int min = max;

        for (String word : words) {
            int num = Integer.parseInt(word);
            if (num > max) max = num;
            if (num < min) min = num;
        }

        return String.format("%d %d", min, max);
    }

    public static void main(String[] args) {
        System.out.println(solution("1 2 3 4"));
        System.out.println(solution("-1 -2 -3 -4"));
        System.out.println(solution("-1 -1"));
    }
}
