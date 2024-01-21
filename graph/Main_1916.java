// 최소비용 구하기
package graph;

import java.util.*;
class Main_1916 {
    static int N;
    static int[][] map;
    static final int INF = 987654321;
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
        map = new int[N+1][N+1];
        for (int i=1; i<N+1; i++) Arrays.fill(map[i], INF);
        int M = sc.nextInt();
        for (int i=0; i<M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            if (c < map[a][b])
                map[a][b] = c;
        }
	    int start = sc.nextInt();
        int end = sc.nextInt();
        System.out.println(dijkstra(start, end));
        sc.close();
    }
    public static int dijkstra(int start, int end) {
        PriorityQueue<int[]> PQ = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] p1, int[] p2) {
                return p1[0] - p2[0];
            }
        });
        int[] distance = new int[N+1];
        Arrays.fill(distance, INF);
        distance[start] = 0;
        PQ.add(new int[] {0, start}); // distance, node
        while (!PQ.isEmpty()) {
            int dist = PQ.peek()[0];
            int node = PQ.peek()[1];
            PQ.poll();
            if (dist > distance[node]) { // 탐색할 필요 X
                continue;
            } else {
                for (int i=1; i<N+1; i++) {
                    if (distance[node] + map[node][i] < distance[i]) {
                        distance[i] = distance[node] + map[node][i];
                        PQ.add(new int[] {distance[i], i});
                    }
                }
            }
        }
        return distance[end];
    }
    
}
