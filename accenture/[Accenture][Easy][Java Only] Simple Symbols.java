import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'simpleSymbols' function below.
     *
     * The function is expected to return a BOOLEAN.
     * The function accepts STRING str as parameter.
     */

    public static boolean simpleSymbols(String str) {
        String s_trimmed = str.trim();

        // if alphabet is first or last item, return false
        if(Character.isLetter(s_trimmed.charAt(0)) || Character.isLetter(s_trimmed.charAt(s_trimmed.length()-1)))
            return false;

        // if front/back of an alphabet not '+', return false
        for (int i = 1 ; i <str.length()-1; i++) 
            if (Character.isLetter(s_trimmed.charAt(i)) && (s_trimmed.charAt(i-1)!='+' || s_trimmed.charAt(i+1)!='+'))
                return false;

  return true;


    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String str = bufferedReader.readLine();

        boolean solution = Result.simpleSymbols(str);

        bufferedWriter.write(String.valueOf(solution ? 1 : 0));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}