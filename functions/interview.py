from typing import List, Optional


def interview_calculations(int_to_calculate: int) -> List[int]:
    if int_to_calculate <= 1:
        return [int_to_calculate, ]

    return_list = [int_to_calculate, ]
    if not(bool(int_to_calculate % 2)):
        int_to_calculate //= 2
        return_list.extend(interview_calculations(int_to_calculate))
    else:
        int_to_calculate = (int_to_calculate * 3) + 1
        return_list.extend(interview_calculations(int_to_calculate))

    return return_list


def interview(my_input: int) -> Optional[List[int]]:
    if my_input < 0:
        print(f'Non positive integer used as input, aborting: {my_input}')
        return

    return interview_calculations(my_input)
