import java.security.InvalidAlgorithmParameterException;
import java.io.*;
import java.util.*;


/**
 * Models a weighted graph of latitude-longitude points
 * and supports various distance and routing operations.
 * To do: Add your name(s) as additional authors
 * @author Brandon Fain
 * @author Owen Astrachan modified in Fall 2023
 *
 */
public class GraphProcessor {
    /**
     * Creates and initializes a graph from a source data
     * file in the .graph format. Should be called
     * before any other methods work.
     * @param file a FileInputStream of the .graph file
     * @throws Exception if file not found or error reading
     */

    // include instance variables here
    private HashMap<Point,HashSet<Point>> adjaceList;

    public GraphProcessor(){
        // TODO initialize instance variables

    }

    /**
     * Creates and initializes a graph from a source data
     * file in the .graph format. Should be called
     * before any other methods work.
     * @param file a FileInputStream of the .graph file
     * @throws IOException if file not found or error reading
     */

    public void initialize(FileInputStream file) throws IOException {
        // TODO implement by reading info and creating graph
        Scanner s =  new Scanner(file);
        adjaceList = new HashMap<>();

        String[] first =  s.nextLine().split(" ");
        
        int vertCounter = Integer.parseInt(first[0]);
        
        int edgeCounter = Integer.parseInt(first[1]);
        
        
        Point[] pArr = new Point[vertCounter];

        
        for(int i = 0; i < vertCounter; i++){
            String[] l = s.nextLine().split(" ");

            String name = l[0];
            Double latit = Double.parseDouble(l[1]);
            Double longit = Double.parseDouble(l[2]);

            Point p = new Point(latit, longit);
            adjaceList.put(p, new HashSet<Point>());
            pArr[i] = p;
        }

        for(int i = 0; i < edgeCounter; i++){
            String name = "";
            String[] l = s.nextLine().split(" ");

            int A1 = Integer.parseInt(l[0]);
            int A2 = Integer.parseInt(l[1]);
            
            if(l.length > 2){name = l[2];}

            Point point1 = pArr[A1];
            Point point2 = pArr[A2];

            adjaceList.get(point1).add(point1);
            adjaceList.get(point2).add(point2);
        }
    }

    /**
     * Searches for the point in the graph that is closest in
     * straight-line distance to the parameter point p
     * @param p is a point, not necessarily in the graph
     * @return The closest point in the graph to p
     */
    public Point nearestPoint(Point p) {
        // TODO implement nearestPoint
        Point closest = p;

        double shortest = Math.tan(Math.PI/2);


        for(Point k : adjaceList.keySet()){
            if(p.distance(k) < shortest){
                shortest = p.distance(k);
                closest = k;
            }
        }

        return closest;
    }

    /**
     * Calculates the total distance along the route, summing
     * the distance between the first and the second Points, 
     * the second and the third, ..., the second to last and
     * the last. Distance returned in miles.
     * @param start Beginning point. May or may not be in the graph.
     * @param end Destination point May or may not be in the graph.
     * @return The distance to get from start to end
     */
    public double routeDistance(List<Point> route) {
        double d = 0.0;
        // TODO implement routeDistance

        for(int i = 0; i < route.size(); i++){
            
            Point a1 = route.get(i);
            Point a2 = route.get(i + 1);
            
            d += a1.distance(a2);
        }

        return d;
    }
    

    /**
     * Checks if input points are part of a connected component
     * in the graph, that is, can one get from one to the other
     * only traversing edges in the graph
     * @param p1 one point
     * @param p2 another point
     * @return true if and onlyu if p2 is reachable from p1 (and vice versa)
     */
    public boolean connected(Point p1, Point p2) {
        // TODO implement connected
        Set<Point> visited = new HashSet<>(); 
        Stack<Point> toExplore = new Stack<>(); 


        Point current = p1;
        
        visited.add(current);
        
        toExplore.add(current);

        while(!toExplore.isEmpty()){ 
            current = toExplore.pop();
            
            for(Point neighbor: adjaceList.get(current)){
                
                if(neighbor.equals(p2)){ 
                    return true; 
                }
                
                if(!visited.contains(neighbor)){ 
                    toExplore.push(neighbor);
                    visited.add(neighbor); 
                }
            }
        }
        return false;
    }

    /**
     * Returns the shortest path, traversing the graph, that begins at start
     * and terminates at end, including start and end as the first and last
     * points in the returned list. If there is no such route, either because
     * start is not connected to end or because start equals end, throws an
     * exception.
     * @param start Beginning point.
     * @param end Destination point.
     * @return The shortest path [start, ..., end].
     * @throws IllegalArgumentException if there is no such route, 
     * either because start is not connected to end or because start equals end.
     */
    public List<Point> route(Point start, Point end) throws IllegalArgumentException {
        // TODO implement route
        Map<Point, Double> distance = new HashMap<>();
        Map<Point, Point> previous = new HashMap<>();
        Comparator<Point> comp = (a, b) -> (int) (distance.get(a) - distance.get(b));
        PriorityQueue<Point> toExplore = new PriorityQueue<>(comp);
        Point current = start;
        List<Point> ret = new ArrayList<>();
        distance.put(current, 0.0);
        toExplore.add(current);
        while (!toExplore.isEmpty()) {
            current = toExplore.remove();
            for (Point neighbor : adjaceList.get(current)) {
                double weight = neighbor.distance(current);
                if (!distance.containsKey(neighbor) ||
                        distance.get(neighbor) > distance.get(current) + weight) {
                    distance.put(neighbor, distance.get(current) + weight);
                    previous.put(neighbor, current);
                    toExplore.add(neighbor);
                }
            }
        }
        Point check = end;
        while (!check.equals(start)) {
            if (previous.containsKey(check)) {
                ret.add(check);
                check = previous.get(check);
            } else {
                throw new IllegalArgumentException();
            }
        }
        ret.add(start);
        Collections.reverse(ret);

        return ret;
    }
    public static void main(String[] args) throws FileNotFoundException, IOException {
        String name = "data/usa.graph";
        GraphProcessor gp = new GraphProcessor();
        gp.initialize(new FileInputStream(name));
        System.out.println("running GraphProcessor");
    }


    
}
