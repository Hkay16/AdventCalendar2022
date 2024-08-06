import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class day4 {
    public static void main(String[] args) {
        String fileName = "input.txt";
        int overlapCount = 0;
        int containsCount = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                // Delimit by commas
                String[] pairs = line.split(",");

                String firstElf = pairs[0];
                String secondElf = pairs[1];

                // Split each part further to get the ranges
                String[] range1 = firstElf.split("-");
                String[] range2 = secondElf.split("-");

                int start1 = Integer.parseInt(range1[0]);
                int end1 = Integer.parseInt(range1[1]);
                int start2 = Integer.parseInt(range2[0]);
                int end2 = Integer.parseInt(range2[1]);

                // Determine if one range fully contains the other
                boolean contains = (start1 <= start2 && end1 >= end2) || (start2 <= start1 && end2 >= end1);

                // Determine is the ranges overlap
                boolean overlap = (start1 <= end2 && end1 >= start2);

                if (overlap) {
                    overlapCount++;
                }
                
                if (contains) {
                    containsCount++;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Part 1: Number of pairs where one range fully contains the other: " + containsCount);
        System.out.println("Part 2: Number of pairs where the ranges overlap: " + overlapCount);
    }
}
