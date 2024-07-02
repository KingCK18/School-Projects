import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HashListAutocomplete implements Autocompletor {
    
    private static final int MAX_PREFIX = 10;
    private Map<String, List<Term>> myMap;
    private int mySize;


    public HashListAutocomplete(String[] terms, double[] weights) {
        if(terms == null || weights == null){
            throw new NullPointerException("One or both terms are equal to null");
        }
        if(terms.length != weights.length){
            throw new IllegalArgumentException("Terms and Weights do not have the same lengths");
        }
        initialize(terms, weights);
    
    }

    @Override
    public List<Term> topMatches(String prefix, int k) {
        // TODO Auto-generated method stub
        if(prefix.length() > MAX_PREFIX){
            prefix = prefix.substring(0, MAX_PREFIX);
        }
        List<Term> finList = myMap.getOrDefault(prefix, Collections.emptyList());
        List<Term> l = finList.subList(0, Math.min(k, finList.size()));

        return l;
    }

    @Override
    public void initialize(String[] terms, double[] weights) {
        // TODO Auto-generated method stub
        myMap = new HashMap<>();
        mySize = 0;

        for(int i = 0; i < terms.length; i++){
            String term = terms[i];
            double weight = weights[i];

            Term t = new Term(term, weight);
            
            for(int j = 0; j < MAX_PREFIX; j++){
                String prefix = term.substring(0,j);
                if(!myMap.containsKey(prefix)){
                    myMap.put(prefix, new ArrayList<>());
                }
                myMap.get(prefix).add(t);
            }
        }
        for(String prefix : myMap.keySet()){
            Collections.sort(myMap.get(prefix), Collections.reverseOrder(Comparator.comparing(Term::getWeight)));
        }
    }

    @Override
    public int sizeInBytes() {
        // TODO Auto-generated method stub

        if(mySize == 0){
            for(String k : myMap.keySet()){
                mySize += BYTES_PER_CHAR * k.length();
                List<Term> val = myMap.get(k);
                for(Term v : val){
                    mySize += BYTES_PER_CHAR * v.getWord().length();
                    mySize += BYTES_PER_DOUBLE;                  
                }
            }
        }
        System.out.println(mySize);
        return mySize;
    }  
}

