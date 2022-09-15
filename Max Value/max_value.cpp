#include <vector>
#include <limits>

float maxValue(std::vector<float> numbers) {
  float max = -std::numeric_limits<float>::infinity();
  for (float num : numbers) {
    if (num > max) {
      max = num;
    }
  }
  return max;
}
