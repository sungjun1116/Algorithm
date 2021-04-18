import collections
import sys

input = sys.stdin.readline


# 트라이의 노드
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(
            TrieNode)  # 존재하지 않는 키를 조회할 경우, 에러 메세지를 출력하는 대신 디폴트 값을 기준으로 해다 키에 대한 딕셔너리 아이템을 생성해준다.


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 단어 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 일관성 여부 체크
    def consistency(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.word:  # 다른 문자열을 포함하고 있다면
                return False
            node = node.children[char]
        return True


t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    trie = Trie()

    phone = []
    for _ in range(n):
        x = input().rstrip()
        phone.append(x)
        trie.insert(x)

    result = True
    for p in phone:
        result *= trie.consistency(p)

    print("YES" if result else "NO")
