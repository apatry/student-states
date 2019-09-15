#!/usr/bin/env python

import random

# TODO Select all states
# TODO Deal with invalid indices

# Map where the key is a state and the value its capital
STATE_CAPITALS = {
    "Connecticut": "Hartford",
    "Maine": "Augusta",
    "Massachusetts": "Boston",
    "New Hampshire": "Concord",
    "Rhode Island": "Providence",
    "Vermont": "Montpellier"
}

def main():
    """
    Execute the program.
    """
    state_list = list(STATE_CAPITALS.keys())
    studied_states = select_states(state_list)

    print("You selected {}".format(studied_states))

    while len(studied_states) > 0:
        # pick a random states
        random_state = random.choice(studied_states)
        good_answer = False
        while not good_answer:
            user_capital = input("What is the capital of {}? ".format(random_state))
            real_capital = STATE_CAPITALS[random_state]
            if user_capital == real_capital:
                print("Correct!\n")
                studied_states.remove(random_state )
                good_answer = True
            else:
                print("WRONG!!! The capital of {} is {}\n".format(random_state, real_capital))

def select_states(states):
    """
    Prompt the users for a set of states to study.

    :param states: List of states.
    :return: List of selected states.
    """
    prompt = "Pick many states (number separated by space) or press enter for all\n\n"
    for i, state in enumerate(states):
        prompt += "{i}. {state}\n".format(i = i, state = state)

    selected = input(prompt)
    selected_numbers = [int(x) for x in selected.split()]

    selected_states = []
    for i in selected_numbers:
        selected_states.append(states[i])

    if len(selected_states) == 0:
        selected_states = states

    return selected_states

if __name__ == '__main__':
    main()
