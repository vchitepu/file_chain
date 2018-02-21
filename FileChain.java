//Chain of files using implemented with a stack
import java.util.Stack;

public class FileChain{

	private static Stack<File> filechain;

	static{
		initFileChain();
	}

	public static File getLatestFile(){
		return filechain.peek();
	}

	public static void pushNewFile(File new_file){
		filechain.push(new_file);
	}

	public static void initFileChain(){
		filechain = new Stack<File>();
		filechain.push(FileUtil.generateGenesisFile());
	}
}