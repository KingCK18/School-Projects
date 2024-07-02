public class LinkStrand implements IDnaStrand {
    
    private Node myFirst, myLast;
    private long mySize;
    private int myAppends;
    private int myIndex;
    private Node myCurrent;
    private int myLocalIndex;

    private class Node{
        String myInfo;
        Node myNext;
        Node prev;

        public Node(String s){
            myInfo = s;
            myNext = null;
            prev = null;
        }
    }

    public LinkStrand(){
        this("");
    }

    public LinkStrand(String s){
        initialize(s);
    }

    @Override
    public long size() {
        // TODO Auto-generated method stub
        return mySize;
    }

    @Override
    public void initialize(String source) {
        // TODO Auto-generated method stub
        Node newNode = new Node(source);
        myFirst = newNode;
        myLast = newNode;
        mySize = source.length();
        myAppends = 0;
        myIndex = 0;
        myCurrent = myFirst;
        myLocalIndex = 0;
    }

    @Override
    public IDnaStrand getInstance(String source) {
        // TODO Auto-generated method stub
        return new LinkStrand(source);
    }

    @Override
    public IDnaStrand append(String dna) {
        // TODO Auto-generated method stub
        Node newNode = new Node(dna);
        if (myLast != null){
            myLast.myNext = newNode;
        }
        else{
            myFirst = newNode;
        }
        
        newNode.prev = myLast;
        myLast = newNode;
        mySize = mySize + dna.length();
        myAppends++;

        return this;
    }

    @Override
    public IDnaStrand reverse() {
        // TODO Auto-generated method stub
        
        Node newNode = myLast;
        
        StringBuilder sb =  new StringBuilder(newNode.myInfo);
        
        IDnaStrand newStrand = new LinkStrand(sb.reverse().toString());
        
        
        while (newNode.prev != null){
            newNode = newNode.prev;
            sb = new StringBuilder(newNode.myInfo);
            newStrand.append(sb.reverse().toString());

        }
        return newStrand;
    }

    @Override
    public int getAppendCount() {
        // TODO Auto-generated method stub
        return myAppends;
    }

    @Override
public char charAt(int index) {
    if (index < 0 || index >= mySize) {
        throw new IndexOutOfBoundsException("Index is Out of Bounds: " + index);
    }

    if (myIndex > index) {
        myCurrent = myFirst;
        myLocalIndex = 0;
        myIndex = 0;
    }

    while (index >= myIndex + myCurrent.myInfo.length()) {
        myIndex += myCurrent.myInfo.length();
        myLocalIndex = 0;

        if (myCurrent.myNext == null) {
            throw new IndexOutOfBoundsException("Index is Out of Bounds: " + index);
        }

        myCurrent = myCurrent.myNext;
    }

    myLocalIndex = index - myIndex;
    myIndex = index;

    return myCurrent.myInfo.charAt(myLocalIndex);
}


    public String toString(){
        StringBuilder result = new StringBuilder();
        Node currentNode = myFirst;
        while(currentNode != null){
            result.append(currentNode.myInfo);
            currentNode = currentNode.myNext;
        }
        return result.toString();
    }
    
}
