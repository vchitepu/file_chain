
import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;
import java.lang.Runtime;
import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Conversion{

	public static String FiletoHex(String file) throws IOException, FileNotFoundException{

		String content = "";
		String command = "xxd " + file + " > tempHexFile.txt";
		Process proc = Runtime.getRuntime().exec(command);
		File f = new File("tempHexFile.txt");
		Scanner s = new Scanner(f);
		int i = 0;
		while(s.hasNext()){
			content += s.next();
			i++;
		}
		return content;
	}

}
