import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'timeConvert' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts INTEGER num as parameter.
     */

    public static String timeConvert(int num) {
    // Write your code here
        
        int m = 0;
        int h = 0;
        
        h = num / 60;
        m = num % 60;
        
        String h_name = "hours";
        String m_name = "minutes";;
        
        if (h==1){
            h_name = "hour";
        }
        
        if (m==1){
            m_name = "minute";
        }
        
        return h + " " + h_name + " " + m + " " + m_name;
        

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int num = Integer.parseInt(bufferedReader.readLine().trim());

        String solution = Result.timeConvert(num);

        bufferedWriter.write(solution);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

