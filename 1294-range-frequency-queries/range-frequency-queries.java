import java.util.*;

class RangeFreqQuery {

    private Map<Integer, List<Integer>> map;

    public RangeFreqQuery(int[] arr) {

        map = new HashMap<>();

        for (int i = 0; i < arr.length; i++) {
            map.computeIfAbsent(arr[i], k -> new ArrayList<>())
               .add(i);
        }
    }

    public int query(int left, int right, int value) {

        List<Integer> indices = map.get(value);

        if (indices == null) {
            return 0;
        }

        int start = lowerBound(indices, left);
        int end = lowerBound(indices, right + 1);

        return end - start;
    }

    private int lowerBound(List<Integer> list, int target) {

        int low = 0;
        int high = list.size();

        while (low < high) {

            int mid = low + (high - low) / 2;

            if (list.get(mid) < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        return low;
    }
}