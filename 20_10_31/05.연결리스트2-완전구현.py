## 함수 선언부
class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNode(head):
    current = head
    print(current.data, end='  ')
    while current.link != None:
        current = current.link
        print(current.data, end='  ')
    print()


def insert_node(findData, insertData):
    global memory, head, pre, current

    if findData == head.data:  # 첫노드가 찾는 값일때
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    # 두번째 노드 이후일때....
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 마지막까지 못찾을 때.. (=마지막에 삽입)
    node = Node()
    node.data = insertData
    current.link = node


def delete_node(deleteData):
    global memory, head, pre, current
    if deleteData == head.data:  # 첫노드가 찾는 값일때
        current = head
        head = head.link
        del (current)
        return
    # 두번째 노드 이후를 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del (current)
            return


def find_node(findData):
    pass  # 찾으면 True, 못찾으면 False  리턴


## 전역 변수부
memory = []
head, pre, current = None, None, None
dataAry = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
if __name__ == '__main__':
    # 첫번째 노드
    node = Node()
    node.data = dataAry[0]
    head = node  # 헤드 지정 (*중요)
    memory.append(node)

    # 두번째 노드 부터.....
    for data in dataAry[1:]:
        pre = node  # 이전노드 기억(*중요)
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNode(head)

    insert_node('다현', '화사')
    printNode(head)
    insert_node('사나', '솔라')
    printNode(head)
    insert_node('마동석', '문별')
    printNode(head)

    delete_node('화사')
    printNode(head)
    delete_node('솔라')
    printNode(head)
