# eval.py
class Evaluator:

    @staticmethod
    def zip_evaluate(words, coefs):
        if len(words) != len(coefs):
            return -1
        total = 0
        for word, coef in zip(words, coefs):
            total += len(word) * coef
        return total

    @staticmethod
    def enumerate_evaluate(words, coefs):
        if len(words) != len(coefs):
            return -1
        total = 0
        for i, word in enumerate(words):
            total += len(word) * coefs[i]
        return total
