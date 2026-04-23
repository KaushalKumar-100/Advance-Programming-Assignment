import java.util.*;
import java.util.stream.*;

class Student {

    int id;
    String name;
    List<String> courses;
    Map<String,Integer> scores;

    Student(int id,String name){
        this.id=id;
        this.name=name;
        courses=new ArrayList<>();
        scores=new HashMap<>();
    }

    double getAverageScore(){
        return scores.values()
                .stream()
                .mapToInt(Integer::intValue)
                .average()
                .orElse(0);
    }
}

public class Student_performance {

   
    public static List<Student> getTopNStudents(List<Student> students,int n){

        return students.stream()
                .sorted(Comparator.comparingDouble(Student::getAverageScore).reversed())
                .limit(n)
                .collect(Collectors.toList());
    }



    public static Map<String,Double> getAverageScorePerCourse(List<Student> students){

        Map<String,List<Integer>> courseScores = new HashMap<>();

        for(Student s:students){
            for(String course:s.courses){

                int marks = s.scores.getOrDefault(course,0);

                courseScores
                        .computeIfAbsent(course,k->new ArrayList<>())
                        .add(marks);
            }
        }

        Map<String,Double> avgMap = new HashMap<>();

        for(String course:courseScores.keySet()){

            List<Integer> marks = courseScores.get(course);

            double avg = marks.stream()
                    .mapToInt(Integer::intValue)
                    .average()
                    .orElse(0);

            avgMap.put(course,avg);
        }

        return avgMap;
    }


    public static Set<String> getAllUniqueCourses(List<Student> students){

        return students.stream()
                .flatMap(s -> s.courses.stream())
                .collect(Collectors.toSet());
    }


    public static void main(String[] args){

        List<Student> students = new ArrayList<>();


        // Student 1
        Student s1 = new Student(24012,"Anil");
        s1.courses.addAll(Arrays.asList("DS","AP","CAO","TOC"));
        s1.scores.put("DS",42);
        s1.scores.put("AP",38);
        s1.scores.put("CAO",35);
        s1.scores.put("TOC",40);
        students.add(s1);


        // Student 2
        Student s2 = new Student(24013,"Sahil");
        s2.courses.addAll(Arrays.asList("DS","AP","CAO","TOC"));
        s2.scores.put("DS",30);
        s2.scores.put("AP",44);
        s2.scores.put("CAO",36);
        s2.scores.put("TOC",41);
        students.add(s2);


        // Student 3
        Student s3 = new Student(24014,"Aryan");
        s3.courses.addAll(Arrays.asList("DS","AP","CAO","TOC"));
        s3.scores.put("DS",33);
        s3.scores.put("AP",28);
        s3.scores.put("CAO",39);
        s3.scores.put("TOC",45);
        students.add(s3);


        // Student 4
        Student s4 = new Student(24015,"Aditya");
        s4.courses.addAll(Arrays.asList("DS","AP","CAO","TOC"));
        s4.scores.put("DS",37);
        s4.scores.put("AP",40);
        s4.scores.put("CAO",29);
        s4.scores.put("TOC",48);
        students.add(s4);


        // Student 5
        Student s5 = new Student(24016,"Kaushal");
        s5.courses.addAll(Arrays.asList("DS","AP","CAO","TOC"));
        s5.scores.put("DS",41);
        s5.scores.put("AP",43);
        s5.scores.put("CAO",34);
        s5.scores.put("TOC",39);
        students.add(s5);


        // Top 3 students
        List<Student> topStudents = getTopNStudents(students,5);

        System.out.println("Top Students:");
        for(Student s:topStudents){
            System.out.println(s.name+" Avg:"+s.getAverageScore());
        }


        // Course averages
        System.out.println("\nAverage per Course:");
        System.out.println(getAverageScorePerCourse(students));


        // Unique courses
        System.out.println("\nAll Courses:");
        System.out.println(getAllUniqueCourses(students));
    }
}