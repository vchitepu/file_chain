
import java.security.DigestException;
import java.security.NoSuchAlgorithmException;

public class Miner{

	public static File generateNewFile(FileData data) throws NoSuchAlgorithmException, DigestException{

		File previous_file = FileChain.getLatestFile();
		int index = previous.getIndex() + 1;
		long timestamp = System.currentTimeMillis();
		String previous_hash = previous_file.getHash();
		String hash = ProofOfWork.generateHash(index, previous_hash, timestamp, data);
		return new File(index, timestamp, previous_hash, hash, data);
	}
}