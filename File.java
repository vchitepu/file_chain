// ADT for the actual file
public class File{

	private int index;
	private long timestamp;
	private String previous_hash;
	private String hash;
	private FileData data;


	public File(int index, long timestamp, String previous_hash, String hash, FileData data){
		this.index = index;
		this.timestamp = timestamp;
		this.previous_hash = previous_hash;
		this.hash = hash;
		this.data = data;
	}

	public int getIndex(){
		return index;
	}

	public void setIndex(int index){
		this.index = index;
	}

	public long getTimestamp(){
		return index;
	}

	public void setTimestamp(long timestamp){
		this.timestamp = timestamp;
	}

	public String getPrevious(){
		return previous_hash;
	}

	public void setPrevious(String previous_hash){
		this.previous_hash = previous_hash;
	}

	public String getHash(){
		return hash;
	}

	public void setHash(String hash){
		this.hash = hash;
	}

	public FileData getData(){
		return data;
	}

	public void setData(FileData data){
		this.data = data;
	}

}