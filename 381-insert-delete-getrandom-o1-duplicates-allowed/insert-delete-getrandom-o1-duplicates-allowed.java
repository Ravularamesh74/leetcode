import java.util.*;

class RandomizedCollection {

    private List<Integer> nums;
    private Map<Integer, Set<Integer>> map;
    private Random random;

    public RandomizedCollection() {
        nums = new ArrayList<>();
        map = new HashMap<>();
        random = new Random();
    }

    public boolean insert(int val) {

        boolean notPresent =
                !map.containsKey(val) || map.get(val).isEmpty();

        map.computeIfAbsent(val, k -> new HashSet<>())
           .add(nums.size());

        nums.add(val);

        return notPresent;
    }

    public boolean remove(int val) {

        if (!map.containsKey(val) || map.get(val).isEmpty()) {
            return false;
        }

        int removeIndex = map.get(val).iterator().next();

        map.get(val).remove(removeIndex);

        int lastIndex = nums.size() - 1;
        int lastValue = nums.get(lastIndex);

        if (removeIndex != lastIndex) {

            nums.set(removeIndex, lastValue);

            map.get(lastValue).remove(lastIndex);
            map.get(lastValue).add(removeIndex);
        }

        nums.remove(lastIndex);

        return true;
    }

    public int getRandom() {
        return nums.get(random.nextInt(nums.size()));
    }
}