JFLAGS = -g
JC = javac
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES = \
        File.java \
        FileChain.java \
        FileData.java \
        FileUtil.java \
        Hash.java \
        SHA256.java \
        Miner.java \
        ProofOfWork.java 

default: classes

classes: $(CLASSES:.java=.class)

clean:
	$(RM) *.class