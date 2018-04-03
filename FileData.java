
//Data that the file stores, used to generate hash
//
//Based off blockchain transaction. Replace with data parser
import java.io.IOException;

public class FileData{

	private String data;
	
	//Data constructor
	public FileData(String filename) throws IOException{
		this.data = Conversion.FiletoHex(filename);
	}
	public String getData(){
		return data;
	}

	public void setData(String data){
		this.data = data;
	}

	@Override
	public String toString(){
		return data;
	}
}