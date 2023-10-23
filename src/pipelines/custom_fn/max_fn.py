from apache_beam import CombineFn

class MaxFn(CombineFn):
    def create_accumulator(self):
      return {}

    def add_input(self, accumulator, input):
        if input not in accumulator:
            accumulator[input] = 0
        accumulator[input] += 1
        return accumulator

    def merge_accumulators(self, accumulators):
      merged = {}
      for accum in accumulators:
        for item, count in accum.items():
            if item not in merged:
                merged[item] = 0
            merged[item] += count
      return merged

    def extract_output(self, accumulator):
        """Customed solution to get the most active user by date"""
        sum_tweets = 0

        max_value = -1  # Initialize a dummy max value
        most_active_user = None
        for element, counter in accumulator.items():
           sum_tweets += counter
           if counter > max_value:
                most_active_user = element[1]
                max_value = counter

        return sum_tweets, most_active_user
