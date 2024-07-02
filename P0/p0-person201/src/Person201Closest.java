






public class Person201Closest {
    public static void main(String[] args) throws Exception {
        String file = "data/large.txt";
        double min = Double.MAX_VALUE;
        Person201 a = null;
        Person201 b = null;
        // TODO: finish this method
        Person201[] people = Person201Utilities.readFile(file);
        
        for (Person201 p : people){
            for (Person201 j:people){
                double currentDist = Person201Utilities.distance(p.getLatitude(), p.getLongitude(), j.getLatitude(), j.getLongitude());
                if (j.equals(p)){
                    continue;
                }

                if (currentDist < min) {
                    min = currentDist;
                    a = p;
                    b = j;

                }

            }
            
        } 
        
        System.out.printf("closest distance is %3.2f between %s and %s\n",min,a.getName(),b.getName());
    }

    
}
