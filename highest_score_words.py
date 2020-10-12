def get_score(words,letters,score):
    score = sorted(score,reverse=True)
    """最高分出现频率最高"""

if __name__ == '__main__':
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    get_score(words,letters,score)