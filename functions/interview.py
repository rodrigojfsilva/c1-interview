from typing import List, Optional


def interview(my_input: int) -> Optional[List[int]]:
    if my_input < 0:
        print(f'Non positive integer used as input, aborting: {my_input}')
        return

    return_list: List[int] = []
    step_input = my_input
    while step_input > 1:
        return_list.append(step_input)
        is_step_input_even = not(bool(step_input % 2))
        if is_step_input_even:
            step_input //= 2
        else:
            step_input = (step_input * 3) + 1

    return_list.append(step_input)
    return return_list
