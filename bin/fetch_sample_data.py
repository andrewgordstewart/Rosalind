from bs4 import BeautifulSoup

START = 20


def extract_sample_data(problem_abbr):
    with open(f'webpage/problems/{problem_abbr}.html') as f:
        problem = BeautifulSoup(f.read(), 'html.parser')

    sample_in, sample_out = problem.find_all('div',
                                             attrs={'class': 'codehilite'})
    sample_in = sample_in.text.strip()
    sample_out = sample_out.text.strip()

    return sample_in, sample_out


def format_int(i):
    if i < 10:
        return '0' + str(i)
    else:
        return str(i)


if __name__ == '__main__':
    with open('webpage/list-view/index.html') as f:
        list_view = BeautifulSoup(f.read(), 'html.parser')

    problems = list_view.find_all('tr')[1:]
    for i, problem in enumerate(problems[START-1:], start=START):
        abbreviation = problem.find('td').text.lower()

        sample_in, sample_out = extract_sample_data(abbreviation)

        with open(f'test_data/input/{format_int(i)}.txt', 'w+') as test_input:
            test_input.write(sample_in)

        with open(f'test_data/output/{format_int(i)}.txt', 'w+') as test_output:
            test_output.write(sample_out)
