
//General utilities and file procedures
import java.security.NoSuchAlgorithmException;
import java.lang.Runtime;
import java.util.*;


public class FileUtil {
	//genesis file 
	public static File generateGenesisFile() {
		int index = 0;
		long timestamp = System.currentTimeMillis();
		String previous_hash = "0";
		String hash = "0";
		FileData data = new FileData("The_Initial_File");

		return new File(index, timestamp, previous_hash, hash, data);
	}
	//put all file attributes through SHA256 hash algorithm
	public static String wrapFileContent(int index, long timestamp, String previous_hash, FileData data)
		throws NoSuchAlgorithmException {

		String content = index + previous_hash + timestamp + data.toString();
		return SHA256.toSha256(content);
	}
}