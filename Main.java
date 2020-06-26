import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) {
//		processBuilder.command("bash", "-c", "java", "-jar", "processing-py.jar", "app.py");

    	try {
    		Process process = Runtime.getRuntime().exec("java -jar processing-py.jar app.py");

	 		BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

		    String line = "";

	    	while ((line = reader.readLine()) != null) {
	        	System.out.println(line);
	    	}
		
    	} 

    	catch (Exception e) {
    		System.out.println("error");
    	}
		


    }

}