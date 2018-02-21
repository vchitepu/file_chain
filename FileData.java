
//Data that the file stores, used to generate hash
//
//Based off blockchain transaction. Replace with data parser.
public class FileData{

	private String name;
	private int age;

	public FileData(String name, int age){
		this.name = name;
		this.age = age;
	}

	public String getName(){
		return name;
	}

	public void setName(String name){
		this.name = name;
	}

	public int getAge(){
		return age;
	}

	public void setAge(int age){
		this.age = age;
	}

	@Override
	public String toString(){
		return name + "n" + age;
	}
}