# this is the makefile for the fileChain project.
# DO NOT ALTER. If a new ,java file is added add it into the list below.

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