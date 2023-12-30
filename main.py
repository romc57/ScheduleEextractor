from Schedule import Schedule


def run_questions(schedule):
    print_q_a('Which days has the lest arrangements',
              'a')


def print_q_a(q, a):
    print('Q:{}\nA:{}'.format(q, a))


if __name__ == '__main__':
    Src = Schedule('data.json')
    run_questions(Src)