class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>(numCourses);
        for(int i=0; i<numCourses; i++){
            adj.add(new ArrayList<>());
        }
        System.out.println(adj);

        for(int[] pre: prerequisites){
            adj.get(pre[1]).add(pre[0]);
            indegree[pre[0]]++;
        }
        System.out.println(Arrays.toString(indegree));
        
        Queue<Integer> queue = new LinkedList<>();
        for(int i=0; i<numCourses; i++){
            if(indegree[i]==0){
                queue.offer(i);
            }
        }
        
        int nodesVisited=0;
        while(!queue.isEmpty()){
            int node = queue.poll();
            nodesVisited++;

            for(int nei: adj.get(node)){
                indegree[nei]--;
                if(indegree[nei]==0){
                    queue.offer(nei);
                }
            }
        }
        return nodesVisited==numCourses;

    }
}