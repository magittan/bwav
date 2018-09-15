import Algorithmia

class Summarizer:
    client = None
    algo = None

    def __init__(self):
        client = Algorithmia.client('simVeHMWvc1HegdwTNkpem+O/fs1')
        algo = client.algo('nlp/Summarizer/0.1.8')

    def get_summary(self, input):
        return algo.pipe(input).result