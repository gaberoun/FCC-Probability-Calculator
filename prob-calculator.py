import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    # {color: number}
    for key, value in kwargs.items():
      for _ in range(value):
        self.contents.append(key)

  def __str__(self):
    return self.contents

  def draw(self, number_of_draws):
    if number_of_draws > len(self.contents):
      return self.contents

    result = []
    for _ in range(number_of_draws):
      drawn_color = self.contents.pop(random.randrange(len(self.contents)))
      result.append(drawn_color)
    return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_count = 0
  for _ in range(num_experiments):
    hat_cp = copy.deepcopy(hat)
    drawn_colors = hat_cp.draw(num_balls_drawn)
    # expected_cp = copy.deepcopy(expected_balls)

    req_colors = 0
    for key, value in expected_balls.items():
      if drawn_colors.count(key) >= value:
        req_colors += 1

    if req_colors == len(expected_balls):
      success_count += 1

  return success_count / num_experiments
