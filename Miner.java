
//generating and validating new file objects
import java.security.DigestException;
import java.security.NoSuchAlgorithmException;

public class Miner{

	public static File generateNewFile(FileData data) throws NoSuchAlgorithmException, DigestException{

		File previous_file = FileChain.getLatestFile();
		int index = previous_file.getIndex() + 1;
		long timestamp = System.currentTimeMillis();
		String previous_hash = previous_file.getHash();
		String hash = ProofOfWork.generateHash(index, previous_hash, timestamp, data);
		return new File(index, timestamp, previous_hash, hash, data);
	}

	public static boolean isNewFile(File new_file) throws NoSuchAlgorithmException, DigestException{
		boolean valid = true;
		File previous_file = FileChain.getLatestFile();

		if(previous_file.getIndex() != new_file.getIndex() -1){
			valid = false;
		}
		else if(!previous_file.getHash().equals(new_file.getPrevious())){
			valid = false;
		}
		else{
			valid = ProofOfWork.validate(new_file.getHash());
		}
		return valid;
	}
}