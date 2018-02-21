
//Proof of Work for chain
import java.security.DigestException;
import java.security.NoSuchAlgorithmException;

public class ProofOfWork{

	private static final int NUM_BITS = 16;

	public static String generateHash(int index, String previous_hash, long timestamp, FileData data) throws NoSuchAlgorithmException, DigestException{
		String source = FileUtil.wrapFileContent(index, timestamp, previous_hash, data);
		return Hash.generateStamp(NUM_BITS, source);
	}

	public static boolean validate(String hash) throws NoSuchAlgorithmException, DigestException{
		return Hash.valid(NUM_BITS, hash);
	}

}