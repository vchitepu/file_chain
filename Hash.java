
import java.security.DigestException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import java.text.SimpleDateFormat;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.TimeZone;
import java.util.Scanner;

public class Hash{

	private static final byte[] hashBuffer = new byte[20];
	private static MessageDigest md = null;
	private static int MAX_BITS = hashBuffer.length * Byte.SIZE;

	private static Map<Character, String> charBinStringMap = new HashMap<Character, String>();
	static{
		charBinStringMap.put('0', "0000");
		charBinStringMap.put('1', "0001");
		charBinStringMap.put('2', "0010");
		charBinStringMap.put('3', "0011");
		charBinStringMap.put('4', "0100");
		charBinStringMap.put('5', "0101");
		charBinStringMap.put('6', "0110");
		charBinStringMap.put('7', "0111");
		charBinStringMap.put('8', "1000");
		charBinStringMap.put('9', "1001");
		charBinStringMap.put('A', "1010");
		charBinStringMap.put('B', "1011");
		charBinStringMap.put('C', "1100");
		charBinStringMap.put('D', "1101");
		charBinStringMap.put('E', "1110");
		charBinStringMap.put('F', "1111");

	}

	private static char[] randomChar = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
			's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
			'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', '/',
			'+'};


	//STAMP VALIDATION (DOUBLE CHECK AND STUDY)
	public static boolean valid(int numBits, String stamp) throws NoSuchAlgorithmException, DigestException{

		if(numBits > MAX_BITS){
			throw new IllegalArgumentException(String.format("Parameter numBits has max size of %d", MAX_BITS));
		}

		boolean result = false;
		if(md == null){
			md = MessageDigest.getInstance("SHA1");
		}
		md.reset();
		md.update(stamp.getBytes());
		md.digest(hashBuffer, 0, hashBuffer.length);

		if(numBits < Integer.SIZE){
			int mask = 0xFFFFFFFF >>> numBits;
			int value = hashBuffer[0] << 24 | hashBuffer[1] << 16 | hashBuffer[2] << 8 | hashBuffer[3];
			if((mask | ~value) == 0xFFFFFFFF){
				result = true;
			}
		}
		else{
			boolean nonZeroCharFound = false;
			char [] characters = toBinString(hashBuffer).toCharArray();

			for(int i = 0; i < numBits; i++){
				if(characters[i] != '0'){
					nonZeroCharFound = true;
					break;
				}
			}
			result = !nonZeroCharFound;
		}
		return result;
	}

	public static String generateStamp(int numBits, String resourceStr) throws NoSuchAlgorithmException, DigestException{

		if (numBits > MAX_BITS)
			throw new IllegalArgumentException(String.format("Parameter numBits has a maximum size of %d", MAX_BITS));

			String result = null;
			Date currDate = new Date(System.currentTimeMillis());

			int version = 1;
			String dateStr = null;
			{
				SimpleDateFormat fmt = new SimpleDateFormat("yyyyMMddhhmmss");
				fmt.setTimeZone(TimeZone.getTimeZone("ETC"));
				dateStr = fmt.format(currDate);
			}

			String ext = "";
			String randStr = genRandStr();
			int counter = 1;

			while(result == null){
				String stamp = String.format("%s:%s:%s:%s:%s:%s:%s", version, numBits, dateStr, resourceStr, ext, randStr, counter);
				if(valid(numBits, stamp)){
					result = stamp;
					break;
				}
				counter++;
			}
			return result;
	}

	private static String genRandStr(){
		StringBuilder builder = new StringBuilder();
		Random random = new Random();

		for(int i = 0; i < 10; i++){
			builder.append(randomChar[random.nextInt(randomChar.length)]);
		}
		return builder.toString();
	}

	private static String toHexStr(byte[] buffer){
		StringBuilder tmp = new StringBuilder();
		for(byte b : buffer)
			tmp.append(String.format("%02X", b));

		return tmp.toString();
	}

	private static String toBinString(byte[] buff) {
		StringBuilder tmp = new StringBuilder();
		for (char c : toHexStr(buff).toCharArray())
			tmp.append(charBinStringMap.get(c));

		return tmp.toString();
	}
}